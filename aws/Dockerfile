FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update \
  && apt-get install -y git python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 --no-cache-dir install --upgrade pip \
  && rm -rf /var/lib/apt/lists/*

ENV APP_HOME /usr/src/app

WORKDIR $APP_HOME

RUN python3 -m pip install awslambdaric

RUN set -e; pip install bs4 expiringdict Flask Flask-Cors html5lib PyYAML requests serverless_wsgi

COPY main.py config.yaml manifest.json sw.js index.html editor.html media.html ./
COPY static ./static

ENTRYPOINT [ "/usr/local/bin/python", "-m", "awslambdaric" ]
CMD ["main.handler"]
