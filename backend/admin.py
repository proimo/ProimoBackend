from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from backend.models import User, UserProfile

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
