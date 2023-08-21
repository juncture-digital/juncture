#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Python app for Juncture site.
Dependencies: bs4 expiringdict fastapi html5lib lxml mangum Markdown==3.3.6 mdx-breakless-lists prependnewline pymdown-extensions PyYAML requests uvicorn git+https://github.com/rdsnyder/mdx_outline.git git+https://github.com/rdsnyder/markdown-customblocks.git
'''

import logging
logging.basicConfig(format='%(asctime)s : %(filename)s : %(levelname)s : %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

WC_VERSION = '2.0.0-beta.42'

import argparse, base64, json, os, re, sys, time, traceback
from datetime import datetime

BASEDIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(BASEDIR)

from bs4 import BeautifulSoup, Comment
import markdown
from expiringdict import ExpiringDict

from typing import Optional

import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import Response
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(title='Juncture', root_path='/')
if os.path.exists(f'{BASEDIR}/static'):
  app.mount('/static', StaticFiles(directory='static'), name='static')
app.add_middleware(
  CORSMiddleware,
  allow_origins=['*'],
  allow_methods=['*'],
  allow_headers=['*'],
  allow_credentials=True,
)

import requests
logging.getLogger('requests').setLevel(logging.INFO)

PREFIX = os.environ.get('JUNCTURE_PREFIX', 'juncture-digital/juncture')
LOCAL_CONTENT_ROOT = os.environ.get('LOCAL_CONTENT_ROOT')
LOCAL_WC = os.environ.get('LOCAL_WC', 'false').lower() == 'true'
CREDS = json.loads(os.environ.get('JUNCTURE_CREDS', '{}'))
ENV = os.environ.get('ENV')

### Customblocks Config ###

positional_defaults = {
  've-card': ['label', 'image', 'href', 'description'],
  've-header': ['label', 'background', 'subtitle', 'options', 'position'],
  've-iframe': ['src'],
  've-image': ['src', 'options', 'seq', 'fit'],
  've-map': ['center', 'zoom', 'overlay'],
  've-media': ['src'],
  've-meta': ['title', 'description'],
  've-spacer': ['height'],
  've-plant-specimen': ['qid', 'max'],
  've-style': ['src'],
  've-video': ['src', 'caption'],
}

class_args = {
  've-component': [],
  've-entities': ['text-left', 'text-right'],
  've-image': ['text-left', 'text-right', 'col2', 'col3'],
  've-map': ['text-left', 'text-right'],
  've-media': ['text-left', 'text-right', 'col2', 'col3'],
  've-video': ['text-left', 'text-right'],
}

boolean_attrs = {
  've-component': ['sticky',],
  've-entities': ['full', 'left', 'right', 'sticky'],
  've-footer': ['sticky',],
  've-header': ['sticky',],
  've-iframe': ['allow', 'allowfullscreen', 'full', 'left', 'right', 'sticky'],
  've-image': ['cards', 'compare', 'curtain', 'full', 'grid', 'left', 'right', 'sticky', 'sync', 'zoom-on-scroll'],
  've-map': ['cards', 'full', 'left', 'marker', 'prefer-geojson', 'popup-on-hover', 'right', 'sticky', 'zoom-on-scroll', 'zoom-on-click'],
  've-media': ['autoplay', 'cards', 'compare', 'full', 'grid', 'left', 'muted', 'no-caption', 'no-info-icon', 'right', 'small', 'static', 'sticky'],
  've-media-selector': ['full', 'left', 'right', 'sticky'],
  've-mermaid': ['full', 'left', 'right', 'sticky'],
  've-plant-specimen': ['full', 'left', 'right', 'sticky'],
  've-video': ['full', 'left', 'right', 'sticky']
}

def customblocks_default(ctx, *args, **kwargs):
  logger.debug(f'args={args} kwargs={kwargs}')
  if len(args) > 0:
    _classes = []
    idx = 0
    for arg in args:
      if ctx.type in boolean_attrs and arg in boolean_attrs[ctx.type]:
        kwargs[arg] = 'true'
      elif ctx.type in class_args and arg in class_args[ctx.type]:
        _classes.append(arg)
      elif ctx.type in positional_defaults and idx < len(positional_defaults[ctx.type]):
        kwargs[positional_defaults[ctx.type][idx]] = arg
        idx += 1
    if len(_classes) > 0:
      kwargs['class'] = ' '.join(_classes)
  logger.debug(f'{ctx.type} {kwargs}')
  # kwargs = [f'{k}="{quote(v)}"' for k,v in kwargs.items()]
  kwargs = [f'{k}="{v}"' for k,v in kwargs.items()]
  if ctx.type == 've-iframe':
    kwargs = [v.replace('&','&amp;') for v in kwargs]
  
  html = f'<{ctx.type} {" ".join(kwargs)}>{markdown.markdown(ctx.content)}</{ctx.type}>'
  return html

### End Customblocks Config ###

_cache = ExpiringDict(max_len=1000, max_age_seconds=24 * 60 * 60)
def get_gh_file(url, ref='main', refresh=False, **kwargs):
  logger.debug(f'get_gh_file {url} ref={ref} refresh={refresh}')
  if not refresh and url in _cache:
    return _cache[url]
  content = None
  if 'github.io' in url:
    resp = requests.get(url)
    if resp.status_code == 200:
      content = resp.text
  else:  
    acct, repo, *path_elems = url.split('/')
    url = f'https://api.github.com/repos/{acct}/{repo}/contents/{"/".join(path_elems)}?ref={ref}'
    resp = requests.get(url, headers={
        'Authorization': f'Token {CREDS.get("gh_unscoped_token")}',
        'Accept': 'application/vnd.github.v3+json',
        'User-agent': 'JSTOR Labs visual essays client'
    })
    if resp.status_code == 200:
      resp = resp.json()
      content = base64.b64decode(resp['content'])
      try:
        content = content.decode('utf-8')
      except:
        pass
    '''
    url = f'https://raw.githubusercontent.com/{acct}/{repo}/{ref}/{"/".join(path_elems)}'
    resp = requests.get(url)
    logger.info(f'{url} {resp.status_code}')
    if resp.status_code == 200:
      content = resp.text
    '''
  if content:
    _cache[url] = content
  return content

def parse_email(s):
    match = re.search(r'<(\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b)>', s)
    return {'name': s.split('<')[0].strip(), 'email': match.group(1)} if match else {'email': s.strip()}

def _sendmail(**kwargs):
  api_token = CREDS['sendinblue_api_token']
  '''
  referrer_whitelist = set(CREDS['referrer_whitelist'])
  referrer = '.'.join(urllib.parse.urlparse(kwargs['referrer']).netloc.split('.')[-2:]) if 'referrer' in kwargs else None
  if referrer not in referrer_whitelist:
      return 'Forbidden', 403
  '''
  data = {
      'sender': parse_email(kwargs['from']),
      'to': [parse_email(to) for to in kwargs['to']] if isinstance(kwargs['to'],list) else [parse_email(kwargs['to'])],
      'subject': kwargs['subject'],
      'htmlContent': kwargs['message']
  }
  logger.debug(json.dumps(data, indent=2))
  resp = requests.post(
      'https://api.sendinblue.com/v3/smtp/email',
      headers = {
          'Content-type': 'application/json; charset=utf-8', 
          'Accept': 'application/json',
          'api-key': api_token
      },
      data = json.dumps(data))
  return resp.content, resp.status_code

def convert_urls(soup, base, acct, repo, ref, prefix=None, ghp=False):
  logger.info(f'convert_urls: base={base} acct={acct} repo={repo} ref={ref} prefix={prefix} ghp={ghp}')
  path_elems = [pe for pe in base.split('/') if pe] if base else []
  if ghp:
    path_elems = [repo] + path_elems
  if len(path_elems) >= 2 and '/'.join(path_elems[:2]) == prefix: path_elems = path_elems[2:]
  # convert absolute links
  for elem in soup.find_all(href=True):
    if elem.attrs['href'].startswith('http'):
      elem.attrs['target'] = '_blank'
    else:
      orig = elem.attrs['href']
      if elem.attrs['href'].startswith('/'):
        if ghp:
          base = f'/{repo}/'
        else:
          if f'{acct}/{repo}' == prefix:
            base = '/'
          elif acct and repo:
            base = f'/{acct}/{repo}/'
        converted = base + elem.attrs['href'][1:] + (f'?ref={ref}' if ref != 'main' else '')
        elem.attrs['href'] = converted
      if elem.attrs['href'].startswith('#'):
        # elem.attrs['href'] = f'http://localhost:8080/showcase/bedroom-in-arles{elem.attrs["href"]}'
        elem.attrs['href'] = f'{base.replace(prefix, "")}{elem.attrs["href"]}'
      else:
        if len(path_elems) > 0:
          elem.attrs['href'] = f'/{"/".join(path_elems)}/{elem.attrs["href"]}'
        else:
          elem.attrs['href'] = f'/{elem.attrs["href"]}'
        if ref != 'main':
          elem.attrs['href'] += f'?ref={ref}'
      logger.debug(f'orig={orig} base={base} converted={elem.attrs["href"]}')
  
  # convert image URLs
  for elem in soup.find_all(url=True) + soup.find_all(src=True):
    attr_name = 'url' if 'url' in elem.attrs else 'src'
    if elem.attrs[attr_name].startswith('http') or elem.name.startswith('ve-'): continue
    base_elems = base.split('/')[6:-1] if base else []
    src_elems = [pe for pe in re.sub(r'^\.\/', '', elem.attrs[attr_name]).split('/') if pe]
    up = src_elems.count('..')
    gh_path = '/'.join(base_elems[:-up] + src_elems[up:])
    elem.attrs[attr_name] = f'https://raw.githubusercontent.com/{acct}/{repo}/{ref}/{gh_path}'

def _config_tabs(soup):
  for el in soup.find_all('section', class_='tabs'):
    # el_heading = next(el.children) 
    # el_heading.decompose()
    for idx, tab in enumerate(el.find_all('section', recursive=False)):
      heading = next(tab.children)
      # tab_id = tab.attrs['id'] if 'id' in tab.attrs else sha256(heading.text.encode('utf-8')).hexdigest()[:8]
      tab_id = f'tab{idx+1}'
      content_id = f'content{idx+1}'
      input = soup.new_tag('input')
      input.attrs = {'type': 'radio', 'name': 'tabs', 'id': tab_id}
      tab.attrs['class'].append('tab')
      if idx == 0:
        input.attrs['checked'] = ''
      label = soup.new_tag('label')
      label.string = heading.text
      label.attrs = {'for': tab_id}
      el.insert(idx*2, input)
      el.insert(idx*2+1, label)
      tab.attrs['class'].append(content_id)
      heading.decompose()
  
def _config_cards(soup):
  for el in soup.find_all('section', class_='cards'):
    cards_wrapper = soup.new_tag('section')
    el.attrs['class'] = [cls for cls in el.attrs['class'] if cls != 'cards']
    cards_wrapper.attrs['class'] = ['cards', 'wrapper']
    for card in el.find_all('section', recursive=False):
      heading = next(card.children)
      if 'href' in card.attrs:
        card_title = soup.new_tag('a')
        card_title.attrs['href'] = card.attrs['href']
        if card.attrs.get('target') == '_blank' or card.attrs['href'].startswith('http'):
          card_title.attrs['target'] = '_blank'
      else:
        card_title = soup.new_tag('span')
      card_title.attrs['class'] = 'card-title'
      card_title.string = heading.text
      card.insert(0,card_title)
      heading.decompose()

      if card.p.img:
        
        img_style = {
          'background-image': f"url('{card.p.img.attrs['src']}')",
          'background-repeat': 'no-repeat',
          'background-size': 'cover',
          'background-position': 'center'
        }
        style = '; '.join([f'{key}:{value}' for key,value in img_style.items()]) + ';'
        img = soup.new_tag('div')
        img.attrs['class'] = 'card-image'
        img.attrs['style'] = style
        card.insert(1,img)
        card.p.decompose()

      if card.ul:
        card.ul.attrs['class'] = 'card-metadata'
        for li in card.ul.find_all('li'):
          if li.text.split(':')[0].lower() in ('coords', 'eid', 'qid'):
            li.attrs['class'] = 'hide'
  
      if card.p:
        card.p.attrs['class'] = 'card-abstract'

      card.attrs['class'].append('card')
      cards_wrapper.append(card)
    el.append(cards_wrapper)

mark_regexes = {
  'anno': re.compile(r'^[0-9a-f]{8}$'),
  'zoomto': re.compile(r'^(pct:)?\d+,\d+,\d+,\d+(,[0-9a-f]{8})?$'),
  'play': re.compile(r'^[0-9:]+(,[0-9:]+)?$'),
  'flyto': re.compile(r'^[\-+]?[0-9\.]+,[\-+]?[0-9\.]+(,[0-9\.]+)?$'),
  'qid': re.compile(r'^Q[0-9]+$')
}

def _set_mark_attrs(soup):
  for mark in soup.find_all('mark'):
    _revised = {}
    for k,v in mark.attrs.items():
      if k in mark_regexes:
        _revised[k] = v
      elif v.split(':',1)[0] in mark_regexes:
        _revised[v.split(':',1)[0]] = v.split(':',1)[1]
      else:
        regex_match = None
        for attr_key, regex in mark_regexes.items():
          regex_match = regex.match(v)
          if regex_match:
            _revised[attr_key] = v
            break
        if not regex_match:
          _revised[k] = v
    mark.attrs = _revised
    # logger.info(mark.attrs)

def add_link(soup, href, attrs=None):
  link = soup.new_tag('link')
  link.attrs = {**{'href':href}, **(attrs if attrs else {})}
  soup.head.append(link)

def add_script(soup, src, attrs=None):
  script = soup.new_tag('script')
  script.attrs = {**{'src':src}, **(attrs if attrs else {})}
  soup.body.append(script)

def add_meta(soup, attrs=None):
  meta = soup.new_tag('meta')
  meta.attrs = attrs
  soup.head.append(meta)

def merge_entities(tag, qids=None):
  qids = qids or []
  qids = qids + [qid for qid in tag.attrs.get('entities','').split() if qid not in qids]
  return merge_entities(tag.parent, qids) if tag.parent else qids

def find_qids(text):
  return re.findall(r'\b(Q[0-9]+)\b', text) if text else []

def set_entities(soup):
  for p in soup.find_all('p'):
    if p.parent.name == 've-mermaid': continue
    qids = find_qids(p.string)
    if qids:
      p.string = re.sub(r'\b(Q[0-9]+)\b', '', p.string).rstrip()
      if p.string:
        p.attrs['entities'] = ' '.join(qids)
      else:
        p.parent.attrs['entities'] = ' '.join(qids)
        p.decompose()
    
    if p.string:
      lines = [line.strip() for line in p.string.split('\n')]
      if len(lines) > 1:
        cursor = 1
        match = re.match(r'\d{2}:\d{2}:\d{2}', lines[0])
        if match:
          new_p = BeautifulSoup(f'<p data-start={match[0]} entities="{" ".join(qids)}"><mark play="{match[0]}"><b>{lines[0]}</b></mark></br>{" ".join(lines[1:2])}</p>', 'html5lib')
          cursor = 2
        else:
          new_p = BeautifulSoup(f'<p entities="{" ".join(qids)}">{" ".join(lines[:1])}</p>', 'html5lib')
        new_p = new_p.find('p')
        new_p.attrs = {**new_p.attrs, **p.attrs}
        if len(lines) > cursor:
          new_p.attrs['data-media'] = ' '.join(lines[cursor:])
        p.replace_with(new_p)
  
  for tag in ('p', 'section', 'main'):
    for el in soup.find_all(tag):
      qids = merge_entities(el)
      if qids:
        el.attrs['entities'] = ' '.join(qids)
        for child in el.find_all(recursive=False):
          if child.name.startswith('ve-'):
            child.attrs['entities'] = ' '.join(qids)

def parse_md(md, acct, repo, ref, path, prefix, ghp):
  def replace_empty_headings(match):
    return re.sub(r'(#+)(.*)', r'\1 &nbsp;\2', match.group(0))
  
  md = re.sub(r'^#{1,6}(\s+)(\{.*\}\s*)?$', replace_empty_headings, md, flags=re.M)
  
  # md = md.replace('&', '&amp;')
  html = markdown.markdown(
    md,
    extensions=[
      'customblocks',
      'extra',
      'pymdownx.mark',
      'mdx_outline',
      'codehilite',
      'prependnewline',
      'fenced_code',
      'mdx_breakless_lists',
      'sane_lists'
    ],
    extension_configs = {
      'customblocks': {
        'fallback': customblocks_default,
        'generators': {
          'default': 'md.generators:default'
        }
      }
    }
  )

  def em_repl(match):
    return match.group(0).replace('<em>','_').replace('</em>','_')

  html = re.sub(r'<h[1-6]>\s*&nbsp;\s*<\/h[1-6]>', '', html)
  html = re.sub(r'(\bwc:\S*<\/?em>.*\b)', em_repl, html)
  
  soup = BeautifulSoup(html, 'html5lib')

  # remove Github badges
  for img in soup.find_all('img'):
    if 've-button.png' in img.attrs['src']:
      img.parent.decompose()
  
  convert_urls(soup, path, acct, repo, ref, prefix, ghp)

  for el in soup.findAll(re.compile("^ve-.+")):
    el.attrs = dict([(k,v if v != 'true' else None) for k,v in el.attrs.items()])
  
    if el.name in ('ve-image', 've-video'):
      el.name = 've-media'

  _config_tabs(soup)
  _config_cards(soup)
  _set_mark_attrs(soup)

 # insert a 'main' wrapper element around the essay content
  main = soup.html.body
  main.attrs = soup.html.body.attrs
  main.name = 'main'
  main.attrs['id'] = 'juncture'
  body = soup.new_tag('body')
  contents = main.replace_with(body)
  body.append(contents)

  footnotes = soup.find('div', class_='footnote')
  if footnotes:
    footnotes.name = 'section'
    contents.append(footnotes)

  is_v2 = soup.find('param') is None
  if is_v2:
    footer = soup.find('ve-footer')
    if not footer:
      # default footer
      footer = soup.new_tag('ve-footer')
      footer.append(BeautifulSoup('''
        <ul>
          <li><a href="https://juncture-digital.org">Powered by: <img alt="" src="https://juncture-digital.github.io/juncture/static/images/juncture-logo.png"/></a></li>
          <li>view-code</li>
        </ul>''', 
      'html5lib'))
    main.append(footer)

  set_entities(soup)
  
  return soup

def j1_to_j2_md(src):
  """Convert Juncture version 1 markdown to HTML"""
  return ''

def j1_md_to_html(src, **args):
  """Convert Juncture version 1 markdown to HTML"""
  ghp = args.pop('ghp', False)
  acct = args.pop('acct', None)
  repo = args.pop('repo', None)
  ref = args.pop('ref', 'main')
  path = args.pop('path', None)
  env = args.pop('env', 'prod')
  refresh = args.pop('refresh', False)
  prefix = args.pop('prefix', PREFIX)

  logger.info(f'j1_md_to_html: ghp={ghp} acct={acct} repo={repo} ref={ref} path={path} env={env} prefix={prefix}')

  if not acct and prefix:
    acct, repo = prefix.split('/')
  path = f'{acct}/{repo}/{path}' if prefix == 'juncture-digital/juncture' else path
  soup = parse_md(src, acct, repo, ref, path, prefix, ghp)

  first_heading = soup.find(re.compile('^h[1-6]$'))
  
  path_elems = [pe for pe in path.split('/') if pe] if path else []
  if len(path_elems) >= 2 and '/'.join(path_elems[:2]) == f'{acct}/{repo}': path_elems = path_elems[2:]
  essay_base = '/' + '/'.join(path_elems)
  logger.info(f'essay_base={essay_base}')
  
  if env == 'local':
    template = open(f'{BASEDIR}/static/v1.html', 'r').read()
    template = template.replace('https://juncture-digital.github.io/juncture/static/v1.js', f'/static/v1.js?cachebuster={time.time()}')
  else:
    template = get_gh_file('juncture-digital/juncture/static/v1.html', ref='dev' if env == 'dev' else 'main', refresh=refresh)
  template = template.replace('window.PREFIX = null', f"window.PREFIX = '{acct}/{repo}';")
  template = template.replace('window.IS_JUNCTURE = null', f"window.IS_JUNCTURE = {'true' if prefix == 'juncture-digital/juncture' else 'false'};")
  template = template.replace('window.ESSAY_BASE = null', f"window.ESSAY_BASE = '{essay_base}';")
  if ref: template = template.replace('window.REF = null', f"window.REF = '{ref}';")
  template = BeautifulSoup(template, 'html5lib')
  
  main = soup.html.body.main
  for el in template.find_all('component'):
    if 'v-bind:is' in el.attrs and el.attrs['v-bind:is'] == 'mainComponent':
      el.append(main)
      break

  meta = soup.find('param', ve_config='')
  if meta:
    for name in meta.attrs:
      if name == 'title':
        if not template.head.title:
          template.head.append(template.new_tag('title'))
        template.head.title.string = meta.attrs[name]
      elif name not in ('author', 'banner', 'layout'):
        add_meta(template, {'name': name, 'content': meta.attrs[name]})
    if meta.name == 've-meta':
      meta.decompose()
  
  if not (template.head.title and template.head.title.string) and first_heading:
    title = soup.new_tag('title')
    title.string = first_heading.text
    template.head.append(title)

  html = str(template)
  # html = template.prettify()
  html = re.sub(r'\s+<p>\s+<\/p>', '', html) # removes empty paragraphs
  return html

def j2_md_to_html(src, **args):
  """Convert Juncture version 2 markdown to HTML"""
  ghp = args.pop('ghp', False)
  acct = args.pop('acct', None)
  repo = args.pop('repo', None)
  ref = args.pop('ref', 'main')
  path = args.pop('path', None)
  env = args.pop('env', 'prod')
  refresh = args.pop('refresh', False)
  prefix = args.pop('prefix', PREFIX)
  
  logger.info(f'j2_md_to_html: ghp={ghp}, acct={acct}, repo={repo}, ref={ref}, path={path}, env={env} prefix={prefix} PREFIX={PREFIX}')

  path = f'{acct}/{repo}/{path}' if prefix == 'juncture-digital/juncture' else path
  soup = parse_md(src, acct, repo, ref, path, prefix, ghp)

  css = ''
  meta = soup.find('ve-meta')
  add_hypothesis = soup.find('ve-add-hypothesis') or soup.find('ve-annotate')
  custom_style = soup.find('ve-style')
  
  if custom_style:
    css_src = custom_style.attrs.get('src')
    if css_src:
      if css_src.startswith('http'):
        css = requests.get(css_src).text
      else:
        if css_src.startswith('/'):
          gh_path = css_src[1:]
        else:
          gh_path_elems = [pe for pe in path.split('/') if pe]
          if len(gh_path_elems) >= 2 and '/'.join(gh_path_elems[:2]) == f'{acct}/{repo}': gh_path_elems = gh_path_elems[2:]
          css_path_elems = [pe for pe in css_src.split('/') if pe and pe != '.']
          pop = len([pe for pe in css_path_elems if pe == '..'])
          path_elems = gh_path_elems[pop:] + css_path_elems[pop:]
          gh_path = f'{acct}/{repo}/{"/".join(path_elems)}'
        css = get_gh_file(gh_path, ref=ref, refresh=refresh)
    custom_style.decompose()

  path_elems = [pe for pe in path.split('/') if pe] if path else []
  if len(path_elems) >= 2 and '/'.join(path_elems[:2]) == f'{acct}/{repo}': path_elems = path_elems[2:]
  for el in soup.find_all('ve-media'):
    el.attrs['anno-base'] = f'{acct}/{repo}/{"/".join(path_elems)}'
  for el in soup.find_all('ve-map'):
    if prefix:
      el.attrs['essay-base'] = f'{acct}/{repo}/{"/".join(path_elems)}'
  
  if env == 'local':
    template = open(f'{BASEDIR}/static/v2.html', 'r').read()
    if LOCAL_WC:
      template = re.sub(r'https:\/\/cdn\.jsdelivr\.net\/npm\/juncture-digital\/docs\/js\/index\.js', 'http://localhost:5173/src/main.ts', template)
      # template = re.sub(r'.*https:\/\/cdn\.jsdelivr\.net\/npm\/juncture-digital\/docs\/css\/index\.css.*', '', template)
  else:
    template = get_gh_file('juncture-digital/juncture/static/v2.html', ref='dev' if env == 'dev' else 'main', refresh=refresh)
    if env == 'dev':
      template = template.replace('https://cdn.jsdelivr.net/npm/juncture-digital/docs', 'https://juncture-digital.github.io/web-components')
    else: # prod
      template = template.replace('https://cdn.jsdelivr.net/npm/juncture-digital/docs', f'https://cdn.jsdelivr.net/npm/juncture-digital@{WC_VERSION}/docs')

  template = template.replace('window.PREFIX = null', f"window.PREFIX = '{acct}/{repo}';")
  template = template.replace('window.REF = null', f"window.REF = '{ref}';")
  template = BeautifulSoup(template, 'html5lib')
  template.body.insert(0, soup.html.body.main)
  
  if add_hypothesis:
    add_hypothesis.decompose()
    add_script(template, 'https://hypothes.is/embed.js', {'async': 'true'})
    
  if soup.head.style:
    template.body.insert(0, soup.head.style)
  
  if css:
    # add css as style tag
    style = soup.new_tag('style')
    style.attrs['data-id'] = 'default'
    style.string = css
    # template.head.append(style)
    template.body.insert(0, style)

  if meta:
    for name in meta.attrs:
      if name == 'title':
        if not template.head.title:
          template.head.append(template.new_tag('title'))
        template.head.title.string = meta.attrs[name]
      elif name not in ('author', 'banner', 'layout'):
        add_meta(template, {'name': name, 'content': meta.attrs[name]})
    if meta.name == 've-meta':
      meta.decompose()
  # else:
    # add_meta(template, {'name': 'robots', 'content': 'noindex'})
  
  first_heading = soup.find(re.compile('^h[1-6]$'))
  if not (template.head.title and template.head.title.string) and first_heading:
    title = soup.new_tag('title')
    title.string = first_heading.text
    template.head.append(title)
    
  html = str(template)
  # html = template.prettify()
  html = re.sub(r'\s+<p>\s+<\/p>', '', html) # removes empty paragraphs
  
  return html

wxr_prefix = '''<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0"
	xmlns:excerpt="http://wordpress.org/export/1.2/excerpt/"
	xmlns:content="http://purl.org/rss/1.0/modules/content/"
	xmlns:wfw="http://wellformedweb.org/CommentAPI/"
	xmlns:dc="http://purl.org/dc/elements/1.1/"
	xmlns:wp="http://wordpress.org/export/1.2/"
>
  <channel>
    <wp:wxr_version>1.2</wp:wxr_version>
    <item>

      <title><![CDATA[%s]]></title>
      <dc:creator><![CDATA[{%s]]></dc:creator>
      <wp:post_type><![CDATA[post]]></wp:post_type>
      <wp:status><![CDATA[publish]]></wp:status>
      <wp:post_date><![CDATA[%s]]></wp:post_date> <!-- Needs to be unique for each post -->
      <category domain="category" nicename="%s"><![CDATA[%s]]></category>

      <content:encoded><![CDATA[
'''

wxr_suffix = '''
]]></content:encoded>		
    </item>
	</channel>
</rss>
'''

def html_to_wp(html, **kwargs):
  """Convert HTML to WordPress"""
  soup = BeautifulSoup(html, 'html5lib').body
  
  title = kwargs.get('title', 'Imported')
  creator = kwargs.get('creator', 'Unknown')
  post_date = kwargs.get('date', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
  category = kwargs.get('category', 'Unknown')

  wxr_wrappers = [
    # {'tags': ['section', 'div'], 'before': 'wp:group {"layout":{"type":"constrained"}}', 'after': '/wp:group'},
    {'tags': ['section', 'div'], 'before': 'wp:group', 'after': '/wp:group'},
    {'tags': ['h1','h2','h3','h4','h5','h6'], 'before': 'wp:heading', 'after': '/wp:heading'},
    {'tags': ['p'], 'before': 'wp:paragraph', 'after': '/wp:paragraph'},
    {'tags': ['ul'], 'before': 'wp:list', 'after': '/wp:list'},
    {'tags': ['li'], 'before': 'wp:list-item', 'after': '/wp:list-item'},
  ]
  for wrapper in wxr_wrappers:
    for tag in wrapper['tags']:
      for el in soup.find_all(tag):
        el.insert_before(Comment(f' {wrapper["before"]} '))
        el.insert_after(Comment(f' {wrapper["after"]} '))
    
  for el in soup.findAll(re.compile("^ve-.+")):
    el.insert_before(Comment(' wp:html '))
    el.insert_after(Comment(f' /wp:html '))

  prefix = wxr_prefix % (title, creator, post_date, category, category)
  return prefix + soup.prettify().replace('<body>\n','').replace('\n</body>','') + wxr_suffix

def detect_format(src):
  """Detect format of source file"""
  params = re.findall(r'<param', src)
  return 'md_j1' if params else 'md_j2'

def read(src):
  """Read source file"""
  if src.startswith('https://raw.githubusercontent.com'):
    acct, repo, ref, *path = [pe for pe in src.split('/')[3:] if pe != '']
    if not src.endswith('.md'):
      path += ['README.md']
    content = get_gh_file(f'{acct}/{repo}/{"/".join(path)}', ref=ref)
    if content is None and not src.endswith('.md'):
      path = path[:-1]
      path[-1] += '.md'
      content = get_gh_file(f'{acct}/{repo}/{"/".join(path)}', ref=ref)
    return '/'.join(path[:-1]), content
  else:
    src = src[:-1] if src.endswith('/') else src
    src = src[:-3] if src.endswith('.md') else src
    for ext in ('', '.md', '/README.md'):
      path = f'{src}{ext}'
      if os.path.isfile(path):
        with open(path, 'r') as f:
          return path, f.read()

def convert(src, fmt='html', env='prod', **args):
  """Convert source file to specified format"""
  if src.startswith('https://raw.githubusercontent.com'):
    acct, repo, ref, *_ = src.split('/')[3:]
    args = {**args, 'acct': acct, 'repo': repo, 'ref': ref, 'env': env}
  else:
    args = {**args, 'env': env}
  
  args['path'], content = read(src)
  if not content: return None

  in_fmt = detect_format(content)

  out_fmt = fmt
  if out_fmt in ('html', 'md', 'wp'):
    out_fmt += f'_j{in_fmt[-1]}'
  
  if in_fmt == 'md_j1':
    if out_fmt.endswith('_j2'):
      content = j1_to_j2_md(content)
    if out_fmt.startswith('md'):
      return content
    html = j1_md_to_html(content, **args) if out_fmt.endswith('_j1') else j2_md_to_html(content, **args)
    if out_fmt.startswith('html'):
      return html
    else: # wp
      return html_to_wp(html, **args)
  
  elif in_fmt == 'md_j2':
    if out_fmt.startswith('html'):
      return j2_md_to_html(content, **args)
    elif out_fmt.startswith('wp'):
      return html_to_wp(j2_md_to_html(content, **args))
    else:
      return content

template = '''<!doctype html>
<html lang="en">
  <head>
    <title>Markdown</title>
  </head>
  <body>
    <ve-source-viewer src="%s"></ve-source-viewer>
    <script src="https://cdn.jsdelivr.net/npm/juncture-digital/docs/js/index.js" type="module"></script>
  </body>
</html>'''

@app.get('/favicon.ico')
async def ignore():
  return Response(status_code=404)

@app.get('/manifest.json')
def pwa_manifest():
  return Response(status_code=200, content=get_gh_file('juncture-digital/juncture/static/manifest.json'), media_type='application/json')

'''
@app.get('/env')
async def environ():
  return Response(status_code=200, content=json.dumps(dict(os.environ)), media_type='application/json')
'''

@app.get('/healthcheck')
async def healthcheck():
  return Response(status_code=200, content='OK', media_type='text/plain')

@app.get('/gh-token')
async def gh_token(code: Optional[str] = None, hostname: Optional[str] = None):
  token = CREDS['gh_unscoped_token']
  status_code = 200
  if code:
    if hostname in ('127.0.0.1','localhost') or hostname.startswith('192.168.'):
      token = CREDS['gh_auth_token']
    elif hostname in CREDS['gh_secrets']:
      resp = requests.post(
        'https://github.com/login/oauth/access_token',
        headers={'Accept': 'application/json'},
        data={
          'client_id': CREDS['gh_secrets'][hostname]['gh_client_id'],
          'client_secret': CREDS['gh_secrets'][hostname]['gh_client_secret'],
          'code': code
        }
      )
      status_code = resp.status_code
      token_obj = resp.json()
      token = token_obj['access_token'] if status_code == 200 else ''
  return Response(status_code=status_code, content=token, media_type='text/plain')

media_types = {
  'md': 'text/markdown',
  'jpg': 'image/jpeg',
  'jpeg': 'image/jpeg',
  'png': 'image/png',
  'html': 'text/html',
  'txt': 'text/plain',
  'css': 'text/css',
  'js': 'text/javascript',
  'json': 'application/json',
  'yaml': 'application/x-yaml'
}
@app.get('/gh-file/{path:path}')
async def gh_file(
    path: Optional[str] = None,
    ref: Optional[str] = 'main',
  ):
  acct, repo, *path_elems = path.split('/')
  gh_path = '/'.join(path_elems)
  media_type = media_types[gh_path.split('.')[-1]]
  if media_type.split('/')[0] == 'image':
    return RedirectResponse(url=f'https://raw.githubusercontent.com/{acct}/{repo}/{ref}/{gh_path}')
  else:
    return Response(status_code=200, content=get_gh_file(path, ref), media_type=media_type)

@app.get('/html/{path:path}')
@app.get('/{path:path}')
async def serve(
    request: Request,
    base: Optional[str] = None,
    path: Optional[str] = None,
    ref: Optional[str] = 'main',
    fmt: Optional[str] = 'html',
    prefix: Optional[str] = PREFIX,
    ghp: Optional[bool] = False,
    refresh: Optional[bool] = False
  ):
  url_path = request.url.path
  path_elems = [elem for elem in url_path.split('/') if elem]
  path_elems = path_elems[1:] if len(path_elems) > 0 and path_elems[0] == 'html' else path_elems
  '''
  if len(path_elems) > 1 and path_elems[-2] == 'showcase':
    path_elems = path_elems[:-2] + path_elems[-1:]
    RedirectResponse(url=f'/{"/".join(path_elems)}')
  '''
  if ENV:
    env = ENV
  else:
    env = 'local' if request.url.hostname == 'localhost' else 'dev' if request.url.hostname == 'dev.juncture-digital.org' else 'prod'
  logger.info(f'path_elems={path_elems} base={base} env={env} ref={ref} fmt={fmt} prefix={prefix} ghp={ghp} refresh={refresh}')
  
  if prefix == 'juncture-digital/juncture':
    path_root = path_elems[0] if path_elems else 'index'
    if path_root in ('index', 'editor', 'media'):
      if env == 'local':
        content = open(f'{BASEDIR}/static/{path_root}.html', 'r').read()
      else:
        content = get_gh_file(f'juncture-digital/juncture/static/{path_root}.html', ref='dev' if env == 'dev' else 'main', refresh=refresh)

      if env == 'local':
        if LOCAL_WC:
          content = re.sub(r'https:\/\/cdn\.jsdelivr\.net\/npm\/juncture-digital\/docs\/js\/index\.js', 'http://localhost:5173/src/main.ts', content)
          content = re.sub(r'.*https:\/\/cdn\.jsdelivr\.net\/npm\/juncture-digital\/docs\/css\/index\.css.*', '', content)
      elif env == 'dev':
        content = content.replace('https://cdn.jsdelivr.net/npm/juncture-digital/docs', 'https://juncture-digital.github.io/web-components')
      else: # prod
        content = content.replace('https://cdn.jsdelivr.net/npm/juncture-digital/docs', f'https://cdn.jsdelivr.net/npm/juncture-digital@{WC_VERSION}/docs')
      return Response(status_code=200, content=content, media_type='text/html')
    
    else:
      if path_root in ['docs', 'examples', 'showcase'] or len(path_elems) < 2:
        path_elems = ['juncture-digital', 'juncture'] + path_elems
        ref = 'dev' if env == 'dev' else 'main'
      try:
        acct, repo, *path_elems = path_elems
        file_path = '/'.join(path_elems)
        if env == 'local':
          if LOCAL_CONTENT_ROOT:
            src = f'{LOCAL_CONTENT_ROOT}/{path}'
          elif path_root in ['docs', 'examples', 'showcase']:
            src = f'{BASEDIR}/{path.replace("docs/showcase", "showcase")}' if not path.endswith('showcase.md') else f'{BASEDIR}/{path}'
          else:
            src = f'https://raw.githubusercontent.com/{acct}/{repo}/{ref}/{file_path}'
        else:
          if acct == 'juncture-digital' and repo == 'juncture':
            src = f'https://raw.githubusercontent.com/{acct}/{repo}/{"main" if env == "prod" else "dev"}/{file_path}'
          else:
            src = f'https://raw.githubusercontent.com/{acct}/{repo}/{ref}/{file_path}'
        if path_root in ['docs']:
          if len(path_elems) >= 2 and path_elems[1] == 'showcase':
            content = convert(src=src, fmt=fmt, env=env, prefix=prefix, refresh=refresh)
          else:
            _, content = read(src)
        else:
          logger.debug(f'path={path} src={src} file_path={file_path}')
          content = convert(src=src, fmt=fmt, env=env, prefix=prefix, refresh=refresh)
      except:
        logger.error(traceback.format_exc())
        content = None
      if content:
        if fmt.startswith('html') and not request.url.path.startswith('//html'):
          media_type = 'text/html'
        elif fmt.startswith('md'):
          media_type = 'text/markdown'
        else:
          media_type = 'text/plain' #
        return Response(status_code=200, content=content, media_type=media_type)
      else:
        return RedirectResponse(url=f'/#/{path}')
        # return Response(status_code=200, content=path, media_type='text/plain')

  else:
    acct, repo = prefix.split('/')
    args = {'acct': acct, 'repo': repo, 'path': base, 'env': env, 'ghp': ghp}
    if LOCAL_CONTENT_ROOT:
      src = f'{LOCAL_CONTENT_ROOT}/{path}'
    else:
      if len(path_elems) >= 2 and '/'.join(path_elems[:2]) == prefix: path_elems = path_elems[2:]
      src = f'https://raw.githubusercontent.com/{prefix}/{ref}/{"/".join(path_elems)}'
    content = convert(src=src, fmt=fmt, refresh=refresh, prefix=prefix, **args)
    if content:
      media_type = 'text/html' if fmt.startswith('html') else 'text/markdown' if fmt.startswith('md') else 'text/plain'
      return Response(status_code=200, content=content, media_type=media_type)

@app.post('/html/')
async def convert_md_to_html(request: Request):
  if ENV:
    env = ENV
  else:
    env = 'local' if request.url.hostname == 'localhost' else 'dev' if request.url.hostname == 'dev.juncture-digital.org' else 'prod'
  args = await request.body()
  args = json.loads(args)
  args['src'] = args.pop('markdown')
  args['ref'] = args.get('ref', env == 'dev' and 'dev' or 'main')
  args['env'] = env
  if 'acct' not in args and args.get('prefix'):
    args['acct'], args['repo'] = args['prefix'].split('/')
  is_v1 = re.search(r'<param', args['src'])
  html = j1_md_to_html(**args) if is_v1 else j2_md_to_html(**args)
  return Response(status_code=200, content=html, media_type='text/html')

@app.post('/wxr/')
@app.post('/wp/')
async def convert_html_to_wxr(request: Request):
  if ENV:
    env = ENV
  else:
    env = 'local' if request.url.hostname == 'localhost' else 'dev' if request.url.hostname == 'dev.juncture-digital.org' else 'prod'
  payload = await request.body()
  payload = json.loads(payload)
  ref = payload.get('ref', env == 'dev' and 'dev' or 'main')
  wxr = html_to_wp(payload['html'], ref=ref, env=env)
  return Response(status_code=200, content=wxr, media_type='text/xml')

@app.post('/sendmail/')
async def sendmail(request: Request):
  referrer = request.headers.get('referer')
  body = await request.body()
  args = json.loads(body)
  content, status_code = _sendmail(**{**args, **{'referrer': referrer}})
  return Response(status_code=status_code, content=content)

if __name__ == '__main__':
  logger.setLevel(logging.INFO)
  parser = argparse.ArgumentParser(description='Juncture content converters')  
  parser.add_argument('--env', type=str, help='Environment')
  parser.add_argument('--localwc', type=bool, default=False, help='Use local web components')
  parser.add_argument('--prefix', default='juncture-digital/juncture', help='Github path')
  parser.add_argument('--serve', type=bool, default=False, help='Serve converted content')
  parser.add_argument('--reload', type=bool, default=False, help='Reload on change')
  parser.add_argument('--port', type=int, default=8080, help='HTTP port')
  parser.add_argument('--content', help='Local content root')

  args = vars(parser.parse_args())
  os.environ['JUNCTURE_PREFIX'] = args['prefix']
  os.environ['LOCAL_WC'] = str(args['localwc'])
  if args['env']: os.environ['ENV'] = args['env']
  if  args['content']:
    root = os.path.abspath(args['content'])
    os.environ['LOCAL_CONTENT_ROOT'] = root
  
  if args['serve']:
    print(f'\nENV: {os.environ.get("ENV")}\nPREFIX: {os.environ["JUNCTURE_PREFIX"]}\nLOCAL_CONTENT_ROOT: {os.environ.get("LOCAL_CONTENT_ROOT")}\nLOCAL_WC: {os.environ.get("LOCAL_WC")}\n')
    uvicorn.run('main:app', port=args['port'], log_level='info', reload=args['reload'])

elif 'VERCEL' not in os.environ:
  from mangum import Mangum
  handler = Mangum(app)