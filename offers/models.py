import admin_thumbnails
from django.contrib.admin import TabularInline
from django.db import models

from main.utils import get_upload_path


#######################################
# Base classes both for models and admin
class OfferImages(models.Model):
    image = models.ImageField('imagine', upload_to=get_upload_path, blank=True, default=None)

    def __str__(self):
        return self.image.name

    class Meta:
        abstract = True
        verbose_name = 'imagine'
        verbose_name_plural = 'imagini'


@admin_thumbnails.thumbnail('image', background=True)
class OfferImageInline(TabularInline):
    extra = 0

    class Meta:
        abstract = True
