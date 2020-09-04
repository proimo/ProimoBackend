from django.contrib.auth.models import AbstractUser, Group as BaseGroup
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

from main.models import BaseModel
from main.utils import get_upload_path


def get_default_profile_pic():
    try:
        default_pic_setting = Setting.objects.get(slug='default-profile-pic')
        if default_pic_setting.image:
            return default_pic_setting.image.name
        return 'Setarea "Default profile pic" nu are o imagine atribuită'
    except Exception:
        return 'Nu a fost setată o poză implicită de profil'


class User(AbstractUser):
    class Meta:
        verbose_name = 'utilizator'
        verbose_name_plural = 'utilizatori'


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    phone_number = PhoneNumberField(verbose_name='număr de telefon', default=None, blank=True, null=True)
    image = models.ImageField('imagine profil', default=get_default_profile_pic, blank=True, upload_to='profile_pics',
                              null=True)
    description = models.TextField('descriere', default=None, blank=True, null=True)

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return f'{self.user.first_name} {self.user.last_name}'
        return f'{self.user.username}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.image:
            try:
                default_pic_setting = Setting.objects.get(slug='default-profile-pic')
                if default_pic_setting.image:
                    self.image = default_pic_setting.image
                else:
                    self.image.name = 'Setarea "Default profile pic" nu are o imagine atribuită'
            except Exception:
                self.image.name = "Nu a fost setată o poză implicită de profil"

        super(UserProfile, self).save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = 'profil'
        verbose_name_plural = 'profiluri'


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance: User, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()


class Group(BaseGroup):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'grup'
        verbose_name_plural = 'grupuri'


class Setting(BaseModel):
    slug = models.CharField(max_length=500, default=None)
    value = models.CharField('valoare', max_length=200, default=None, blank=True)
    image = models.ImageField('imagine', upload_to=get_upload_path, default=None, blank=True)

    class Meta:
        verbose_name = 'setare'
        verbose_name_plural = 'setări'
