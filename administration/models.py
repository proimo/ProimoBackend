from django.contrib.auth.models import AbstractUser, Group as BaseGroup
from django.db import models
from django.db.models import SlugField, BooleanField, TextField, CharField, ForeignKey, SET_NULL, TextChoices, Index, Q
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

from common.base_models import OrderableModel, WithImageField
from common.models import BaseModel
from common.utils import get_upload_path


class MenuItemType(TextChoices):
    INTERNAL_LINK = 'InternalLink', 'Internal Link'
    EXTERNAL_LINK = 'ExternalLink', 'External Link'
    SCROLL_TO = 'ScrollTo', 'Scroll To'


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
        verbose_name_plural = 'profiluri utilizatori'


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
    value = models.CharField('valoare', max_length=200, default=None, blank=True)
    image = models.ImageField('imagine', upload_to=get_upload_path, default=None, blank=True)

    class Meta:
        verbose_name = 'setare'
        verbose_name_plural = 'setări'


class MenuItem(BaseModel, OrderableModel, WithImageField):
    slug = SlugField(max_length=300, db_index=True, blank=True, default=None)
    is_long = BooleanField(default=False)
    description = TextField(default=None, blank=True, null=True)
    link = CharField(max_length=200, default=None, blank=True)
    type = CharField(max_length=12, choices=MenuItemType.choices, default=MenuItemType.INTERNAL_LINK)
    parent = ForeignKey('self', on_delete=SET_NULL, null=True, blank=True, related_name='children')
    is_published = BooleanField(default=False)

    # https://medium.com/@tnesztler/recursive-queries-as-querysets-for-parent-child-relationships-self-manytomany-in-django-671696dfe47
    def get_children(self, include_self=True):
        return MenuItem.objects.filter(self.get_children_filter(include_self))

    def get_children_filter(self, include_self=True):
        filters = Q(pk=0)
        if include_self:
            filters |= Q(pk=self.pk)
        for item in MenuItem.objects.filter(parent=self):
            if children_filter := item.get_children_filter(include_self=True):
                filters |= children_filter
        return filters

    class Meta(OrderableModel.Meta):
        indexes = [Index(fields=['id', 'slug', 'is_published', 'order_index'])]
