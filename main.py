#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Flask app for Juncture site.
Dependencies: bs4 expiringdict Flask Flask-Cors html5lib PyYAML requests serverless_wsgi
'''

import logging
logging.basicConfig(format='%(asctime)s : %(filename)s : \
  %(levelname)s : %(message)s', level=logging.DEBUG)
logger = logging.getLogger()

import os, re
SCRIPT_DIR = os.path.abspath(os.path.dirname(__file__))

from time import time as now
from flask import Flask, redirect, request, send_from_directory
from flask_cors import CORS
import argparse
import yaml
from urllib.parse import urlencode
from bs4 import BeautifulSoup
from expiringdict import ExpiringDict

import requests
logging.getLogger('requests').setLevel(logging.WARNING)

app = Flask(__name__, static_url_path='/docs', static_folder='docs')
CORS(app)

try:
  from serverless_wsgi import handle_request
  def handler(event, context):
    return handle_request(app, event, context)
except:
  pass

CONFIG = yaml.load(open(f'{SCRIPT_DIR}/config.yaml', 'r').read(), Loader=yaml.FullLoader)

API_ENDPOINT = 'https://api.juncture-digital.org'
DEFAULT_WC_ENDPOINT = 'https://cdn.jsdelivr.net/npm/juncture-digital/docs/js/index.js'
WC_ENDPOINT = 'https://cdn.jsdelivr.net/npm/juncture-digital/docs/js/index.js'
WC_VERSION = '2.0.0-beta.22'

PREFIX = 'juncture-digital/juncture' # Prefix for site content, typically Github username/repo
REF = ''                         # Github ref (branch)
LOCAL_CONTENT_ROOT = None

SEARCH_CACHE = ExpiringDict(max_len=1000, max_age_seconds=24 * 60 * 60)

def _add_link(soup, href, attrs=None):
  link = soup.new_tag('link')
  link.attrs = {**{'href':href}, **(attrs if attrs else {})}
  soup.head.append(link)

def _add_script(soup, src, attrs=None):
  script = soup.new_tag('script')
  script.attrs = {**{'src':src}, **(attrs if attrs else {})}
  soup.body.append(script)

def _set_favicon(soup):
  # Remove default favicon
  for el in soup.find_all('link', {'rel':'icon'}): el.decompose()
  # Add custom favicon
  # _add_link(soup, '/static/images/favicon.svg', {'rel': 'icon', 'type':'image/svg+xml'})
  # _add_link(soup, '/static/images/favicon.ico', {'rel':'icon', 'type':'image/png'})

def _set_style(soup):
  # Remove default favicon
  for el in soup.find_all('link', {'rel':'stylesheet'}): el.decompose()
  # Add custom stylesheet
  # _add_link(soup, '/static/css/custom.css', {'rel': 'stylesheet'})

def _make_pwa(soup):
  _add_link(soup, '/manifest.json', {'rel':'manifest'})
  
def _add_default_footer(soup):
  if not soup.find('ve-footer'):
    footer = soup.new_tag('ve-footer')
    footer.append(BeautifulSoup('''
      <ul>
        <li><a href="https://juncture-digital.org">Powered by: <img alt="" src="https://juncture-digital.github.io/juncture/static/images/juncture-logo.png"/></a></li>
        <li>view-code</li>
      </ul>''', 
    'html5lib'))
    soup.find('main').append(footer)

def _customize_response(html):
  '''Perform any post-processing of API-generated HTML.'''
  # parse API-generated HTML with BeautifulSoup
  #   https://beautiful-soup-4.readthedocs.io/en/latest/
  soup = BeautifulSoup(html, 'html5lib')
  # perform custom updates to api-generated html
  # _set_favicon(soup)
  # _set_style(soup)
  _make_pwa(soup)
  _add_default_footer(soup)
  return str(soup)

def _get_local_content(path):
  '''For local development and testing.'''
  if path.endswith('/'): path = path[:-1]
  _paths = [f'{LOCAL_CONTENT_ROOT}{path}.md', f'{LOCAL_CONTENT_ROOT}{path}/README.md']
  for _path in _paths:
    if os.path.exists(_path):
      return open(_path, 'r').read()
  logger.warn(f'Local content not found: path={path}')

juncture_path_roots = set('docs examples showcase'.split())
logger.info(juncture_path_roots)
def _get_html(path, base_url, ref=None, host=None, **kwargs):
  ref = ref or ('dev' if host in ('dev.juncture-digital.org', 'localhost') and path.split('/')[1] in juncture_path_roots else '')
  logger.info(f'_get_html: path=={path} base_url=={base_url} ref={ref} prefix={PREFIX} is_juncture_path_root={path.split("/")[1] in juncture_path_roots} host={host}')
  html = ''
  status_code = 404
  if LOCAL_CONTENT_ROOT:
    md = _get_local_content(path)
    if md: # Markdown found, convert to HTML using API
      api_url = f'{API_ENDPOINT}/html/?prefix={PREFIX}&base={base_url}'
      resp = requests.post(api_url, json={'markdown':md, 'prefix':PREFIX})
      status_code, html =  resp.status_code, resp.text if resp.status_code == 200 else ''
  else:
    api_url = f'{API_ENDPOINT}/html{path}?prefix={PREFIX}&base={base_url}'
    if ref: api_url += f'&ref={ref}'
    logger.info(api_url)
    resp = requests.get(api_url)
    status_code, html =  resp.status_code, resp.text if resp.status_code == 200 else ''
  if status_code == 200:
    if host == 'localhost':
      if WC_ENDPOINT != DEFAULT_WC_ENDPOINT:
        html = html.replace(DEFAULT_WC_ENDPOINT, WC_ENDPOINT)
        html = re.sub(r'.*https:\/\/cdn\.jsdelivr\.net\/npm\/juncture-digital\/docs\/css\/index\.css.*', '', html)
    elif host == 'dev.juncture-digital.org':
      html = html.replace(DEFAULT_WC_ENDPOINT, 'https://juncture-digital.github.io/web-components/js/index.js')
    else:
      html = html.replace('https://cdn.jsdelivr.net/npm/juncture-digital/docs', f'https://cdn.jsdelivr.net/npm/juncture-digital@{WC_VERSION}/docs')

  return status_code, html

@app.route('/favicon.ico')
def favicon():
  return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/robots.txt')
def pwa_sw():
  return send_from_directory(os.path.join(app.root_path, 'static'), 'robots.txt', mimetype='text/plain')

@app.route('/sw.js')
def robots_txt():
  return send_from_directory(os.path.join(app.root_path), 'sw.js', mimetype='text/javascript')

@app.route('/sitemap.txt')
def sitemap_txt():
  return send_from_directory(os.path.join(app.root_path, 'static'), 'sitemap.txt', mimetype='text/plain')

@app.route('/manifest.json')
def pwa_manifest():
  return send_from_directory(os.path.join(app.root_path), 'manifest.json', mimetype='application/json')

@app.route('/static/css/<path:path>')
def css(path):
  # logger.info(f'{os.path.join(app.root_path, "static", "css")}/{path}')
  return send_from_directory(os.path.join(app.root_path, 'static', 'css'), path, mimetype='text/css')

@app.route('/images/<path:path>')
def images(path):
  return redirect(f'https://juncture-digital.github.io/juncture/static/images/{path}')

@app.route('/<path:path>')
@app.route('/<path:path>/')
def render_html(path=None):
  host = request.host.split(':')[0]
  start = now()
  qargs = dict([(k, request.args.get(k)) for k in request.args])
  base_url = f'/{"/".join(request.base_url.split("/")[3:])}'
  if base_url != '/' and not base_url.endswith('/'): base_url += '/'
  path = f'/{path}' if path else '/'
  status, html = _get_html(path, base_url, host=host, **qargs)
  if status == 200:
    html = _customize_response(html)
  logger.info(f'render: api_endpoint={API_ENDPOINT} base_url={base_url} prefix={PREFIX} path={path} status={status} elapsed={round(now()-start, 3)}')
  if status == 404:
    return redirect(f'/#{path}')
  else:
    return html, status

@app.route('/annotator/<path:path>')
@app.route('/editor/<path:path>')
@app.route('/media/<path:path>')
@app.route('/editor/')
@app.route('/media/')
@app.route('/editor')
@app.route('/media')
def render_app(path=None):
  host = request.host.split(':')[0]
  route = request.path.split('/')[1] if path else (request.path.split('/')[1] or 'index')
  logger.info(f'host={host} route={route} path={path} request.path={request.path}')
  if host == 'localhost':
    html = open(f'{app.root_path}/{route}.html', 'r').read()
  else:
    html = open(f'{app.root_path}/{route}.html', 'r').read()

  if host == 'localhost':
    html = html.replace('https://api.juncture-digital.org', API_ENDPOINT)
    html = html.replace(DEFAULT_WC_ENDPOINT, WC_ENDPOINT)
    html = re.sub(r'.*https:\/\/cdn\.jsdelivr\.net\/npm\/juncture-digital\/docs\/css\/index\.css.*', '', html)
    html = html.replace('https://raw.githubusercontent.com/juncture-digital/juncture/main', '' )
  elif host == 'dev.juncture-digital.org':
    html = html.replace('https://cdn.jsdelivr.net/npm/juncture-digital/docs', 'https://juncture-digital.github.io/web-components')
  else:
    html = html.replace('https://cdn.jsdelivr.net/npm/juncture-digital/docs', f'https://cdn.jsdelivr.net/npm/juncture-digital@{WC_VERSION}/docs')
    
  return html

@app.route('/')
def root():
  global PREFIX
  host = request.host.split(':')[0]
  if host.endswith('plant-humanities.org'):
    PREFIX = 'jstor-labs/plant-humanities'
    return render_html()
  else:
    return render_app()

@app.route('/search')
def search():
  qargs = dict([(k, request.args.get(k)) for k in request.args])
  if 'domain' in qargs and qargs['domain'] in CONFIG['google_search']:
    args = {**CONFIG['google_search'][qargs['domain']], **dict(request.args)}
    url = f'https://www.googleapis.com/customsearch/v1?{urlencode(args)}'
    if url not in SEARCH_CACHE:
      SEARCH_CACHE[url] = requests.get(url).json()
    return SEARCH_CACHE[url]
  else:
    return [], 404

if __name__ == '__main__':
  logger.setLevel(logging.INFO)
  parser = argparse.ArgumentParser(description='Image Info')
  parser.add_argument('--port', help='Port', type=int, default=8080)
  parser.add_argument('--api', help='API Endpoint', default=API_ENDPOINT)
  parser.add_argument('--wc', help='Web Components Endpoint', default=WC_ENDPOINT)
  parser.add_argument('--prefix', help='Content URL prefix', default=PREFIX)
  parser.add_argument('--content', help='Local content root', default=None)
  args = parser.parse_args()
  API_ENDPOINT = args.api
  WC_ENDPOINT = args.wc
  PREFIX = args.prefix
  LOCAL_CONTENT_ROOT = os.path.abspath(args.content) if args.content else None
  print(f'\nAPI_ENDPOINT: {API_ENDPOINT}\nWC_ENDPOINT: {WC_ENDPOINT}\nLOCAL_CONTENT_ROOT: {LOCAL_CONTENT_ROOT}\n')
  app.run(debug=True, host='0.0.0.0', port=args.port)
