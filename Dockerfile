# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8-alpine

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/community \
    --repository http://dl-cdn.alpinelinux.org/alpine/edge/main \
    --virtual .build-deps build-base linux-headers python3-dev postgresql-dev jpeg-dev zlib-dev libmaxminddb gdal-dev

RUN pip install --upgrade pip

#
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
RUN pip install -r requirements.txt --global-option=build_ext --global-option="-I/usr/include/gdal"
RUN apk del .build-deps

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8008