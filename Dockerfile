FROM        python:3-alpine@sha256:31da4cb527055e4e3d7e9e006dffe9329f84ebea79eaca0a1f1c27ce61e40ca5

ENV         DEBIAN_FRONTEND noninteractive
ENV         PYTHONPATH /usr/local/src

RUN         apk add --no-cache --update \
                --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
                binutils build-base python3-dev gdal geos \
                && rm -rf /var/cache/apk/*

COPY        . /usr/local/src
WORKDIR     /usr/local/src
RUN         pip install -U pip setuptools \
                && pip install -r requirements.txt

VOLUME      /usr/local/src
CMD         ["sh"]
