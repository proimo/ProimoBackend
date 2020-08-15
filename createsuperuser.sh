#!/usr/bin/env bash

username='admin'
email='admin@proimo.ro'
password='admin'

imports='from backend.models import User;'
create_superuser='User.objects.create_superuser('$username', '$email', '$password')'

echo "$imports $create_superuser" | python manage.py shell
