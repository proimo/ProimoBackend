from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from main.models import BaseModel
from main.utils import get_file_name


class Offer(BaseModel):
    address = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    price = models.CharField(max_length=15, null=True)
    surface = models.IntegerField(default=0, null=True)
    published = models.BooleanField(default=False)
    content = RichTextUploadingField(null=True)

    class Meta:
        verbose_name = 'ofertă'
        verbose_name_plural = 'oferte'


class OfferImage(models.Model):
    offer = models.ForeignKey(Offer, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_file_name, null=True)

    def __str__(self):
        return self.image.name
