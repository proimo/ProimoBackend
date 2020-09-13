#!/usr/bin/env bash

imports='from administration.models import User;'
create_superuser='User.objects.create_superuser("admin", "admin@proimo.ro", "admin")'

echo "$imports $create_superuser" | python manage.py shell
