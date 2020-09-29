FROM python:3.8-alpine

WORKDIR /app

ADD . /app/

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

RUN addgroup -g 101 -S django && adduser -u 101 -D -S -G django django
RUN apk add --update --no-cache su-exec
RUN apk add gdal geos libpq

RUN set -x && apk add --no-cache --virtual .build-deps \
    build-base \
    gcc \
    musl-dev \
    python3-dev \
    postgresql-dev \
    zlib-dev \
    jpeg-dev \
    && python -m pip install --upgrade pip \
    && pip install -U -r requirements.txt --no-cache-dir \
    && apk del .build-deps

EXPOSE 8000
ENV DEBUG=False
ENV DJANGO_SETTINGS_MODULE=main.settings.production

RUN chmod +x /app/entrypoint.sh
ENTRYPOINT [ "/app/entrypoint.sh" ]