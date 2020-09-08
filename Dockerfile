## The first instruction is what image we want to base our container on
## We Use an official Python runtime as a parent image
#FROM python:3.8-slim
#
## The enviroment variable ensures that the python output is set straight
## to the terminal with out buffering it first
#ENV PYTHONUNBUFFERED 1
#RUN apt-get -y update
#RUN apt-get install -y binutils gdal-bin python3-gdal
#RUN apt-get install -y libproj-dev libgdal-dev libpq-dev gcc musl-dev python3-dev
#
#RUN mkdir /app
#
## Set the working directory to /music_service
#WORKDIR /app
#
## Copy the current directory contents into the container at /music_service
#ADD . /app/
#
## Install any needed packages specified in requirements.txt
#RUN pip install -r requirements.txt --no-cache-dir
##RUN apk del .build-deps
##RUN apt-get clean
#
#CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8008


# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8-alpine

WORKDIR /app

ADD . /app/

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

RUN apk add gdal geos libpq

RUN set -x && apk add --no-cache --virtual .build-deps \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
    binutils gcc musl-dev python3-dev postgresql-dev zlib-dev jpeg-dev \
    && python -m pip install --upgrade pip \
    && pip install -U -r requirements.txt --no-cache-dir \
    && apk del .build-deps

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8008