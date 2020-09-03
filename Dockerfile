# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8-slim

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
RUN apt-get -y update
RUN apt-get install -y binutils libproj-dev gdal-bin libgdal-dev libpq-dev gcc musl-dev python3-dev python3-gdal
#RUN apk add --no-cache \
#    --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
#    --repository http://dl-cdn.alpinelinux.org/alpine/edge/community \
#    --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
#    --virtual .build-deps build-base linux-headers python3-dev postgresql-dev jpeg-dev zlib-dev gdal-dev
#
#RUN apk add gdal libpq
#RUN pip install --upgrade pip

#RUN apk update && apk add --no-cache \
#    --repository http://dl-cdn.alpinelinux.org/alpine/edge/community \
#    --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
#    --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
#    gdal binutils libpq

RUN mkdir /app

# Set the working directory to /music_service
WORKDIR /app

# Copy the current directory contents into the container at /music_service
ADD . /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
#RUN apk del .build-deps
#RUN apt-get clean

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8008