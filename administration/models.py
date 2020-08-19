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
    phone_number = PhoneNumberField(verbose_name='Număr de telefon')
    image = models.ImageField('Imagine profil', default=None, upload_to='profile_pics')

    def __str__(self):
        return (f'{self.user.first_name} {self.user.last_name}' or f'{self.user.username}') + ' Profile'

    # def save(self, *args, **kwargs):
    #     """ On save, update timestamps """
    #     if not self.id and not self.image:
    #         self.image = Setting.objects.get(slug='default-profile-pic').image
    #     return super(self).save(*args, **kwargs)

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
    value = models.CharField('Valoare', max_length=200, null=True, blank=True)
    image = models.ImageField('Imagine', upload_to=get_file_name, null=True, blank=True)

    class Meta:
        verbose_name = 'Setare'
        verbose_name_plural = 'Setări'
