#!/usr/bin/env bash

if [ -z "$1" ]
  then
    echo "You must give the name of the app to migrate!"
elif [ -z "$2" ]; then
    python manage.py makemigrations "$1"
    else python manage.py makemigrations -n "$1" "$2"
fi

