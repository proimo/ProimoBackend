from django.contrib.auth.models import AbstractUser, Group as BaseGroup
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from main.models import BaseModel
from main.utils import get_file_name


class User(AbstractUser):
    class Meta:
        verbose_name = 'Utilizator'
        verbose_name_plural = 'Utilizatori'


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    phone_number = PhoneNumberField(verbose_name='Număr de telefon', default=None, blank=True)
    image = models.ImageField('Imagine profil', default=None, blank=True, upload_to='profile_pics')
    description = models.TextField('Descriere', default=None, blank=True)

    def __str__(self):
        return (f'{self.user.first_name} {self.user.last_name}' or f'{self.user.username}') + ' Profile'

    class Meta:
        verbose_name = 'Profil'
        verbose_name_plural = 'Profile'


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


class Group(BaseGroup):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Grup'
        verbose_name_plural = 'Grupuri'


class Setting(BaseModel):
    slug = models.CharField(max_length=500, default=None)
    value = models.CharField('Valoare', max_length=200, default=None, blank=True)
    image = models.ImageField('Imagine', upload_to=get_file_name, default=None, blank=True)

    class Meta:
        verbose_name = 'Setare'
        verbose_name_plural = 'Setări'
