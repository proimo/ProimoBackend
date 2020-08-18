from django.contrib.auth.models import AbstractUser, Group as BaseGroup
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from main.models import BaseModel
from main.utils import get_file_name


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    phone_number = PhoneNumberField()


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Group(BaseGroup):
    def __str__(self):
        return self.name


class Setting(BaseModel):
    value = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to=get_file_name, null=True, blank=True)
