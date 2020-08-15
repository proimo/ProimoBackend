import uuid

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from main.utils import get_file_name


class Announcement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(_('Title'), max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=15, null=True)
    surface = models.IntegerField(default=0, null=True)
    published = models.BooleanField(default=False)
    content = RichTextUploadingField(null=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Announcement, self).save(*args, **kwargs)


class AnnouncementImage(models.Model):
    announcement = models.ForeignKey(Announcement, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_file_name, null=True)

    def __str__(self):
        return self.image.name


class Setting(models.Model):
    slug = models.CharField(max_length=200)
    value = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to=get_file_name, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()
        self.updated = timezone.now()
        return super(Setting, self).save(*args, **kwargs)
