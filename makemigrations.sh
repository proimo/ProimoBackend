#!/usr/bin/env bash

if [ -z "$1" ]
  then
    echo "You must give name of the app to migrate!"
fi

python manage.py makemigrations "$1"