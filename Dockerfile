FROM        python:3-alpine@sha256:5a824eb82cc75361f98611f3cfc5091ea33f10a6ccea4d4ebdabbc523b9a1614

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
