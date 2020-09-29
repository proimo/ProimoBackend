#!/bin/sh

python manage.py check --deploy
python manage.py collectstatic --no-input --verbosity 0
python manage.py makemigrations --check --dry-run || (echo "Run makemigrations before deploying." && false)
python manage.py migrate --no-input

APP_ROOT=/app
chmod -R u=rwX,g=rX,o= ${APP_ROOT}/*
chown -RL root:django ${APP_ROOT}
chown -RL django:django ${APP_ROOT}/logs ${APP_ROOT}/media
find /usr/src -type d -exec chmod g+s {} +

export PORT=8000
su-exec django gunicorn main.wsgi --timeout 180 --log-file -
