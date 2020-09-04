from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.gis.db.models import PointField
from django.db import models

from main.models import BaseModel


class RentOffer(BaseModel):
    slug = models.CharField(max_length=500, default=None, null=True)
    address = PointField('adresă', max_length=200, null=True)
    region = models.CharField('regiune', max_length=200, blank=True, default=None)
    price = models.CharField('preţ', max_length=15, blank=True, default=None)
    is_published = models.BooleanField('publicat?', default=False)
    content = RichTextUploadingField('conţinut', default=None, blank=True)

    class Meta:
        abstract = True
        verbose_name = 'ofertă închiriere'
        verbose_name_plural = 'oferte închiriere'


# class OfferImage(models.Model):
#     offer = models.ForeignKey(Offer, related_name='images', on_delete=models.CASCADE)
#     image = models.ImageField('Imagine', upload_to=get_file_name, blank=True, default=None)
#
#     def __str__(self):
#         return self.image.name


class ApartmentRent(RentOffer):
    class Meta:
        verbose_name = 'apartament'
        verbose_name_plural = 'apartamente'


class HouseRent(RentOffer):
    class Meta:
        verbose_name = 'casă'
        verbose_name_plural = 'case'


class LandRent(RentOffer):
    class Meta:
        verbose_name = 'teren'
        verbose_name_plural = 'terenuri'


class CommercialSpaceRent(RentOffer):
    class Meta:
        verbose_name = 'spaţiu comercial'
        verbose_name_plural = 'spaţii comerciale'


class OfficeRent(RentOffer):
    class Meta:
        verbose_name = 'birou'
        verbose_name_plural = 'birouri'


class SpecialPropertyRent(RentOffer):
    class Meta:
        verbose_name = 'proprietate specială'
        verbose_name_plural = 'proprietăţi speciale'


class IndustrialSpaceRent(RentOffer):
    class Meta:
        verbose_name = 'spaţiu industrial'
        verbose_name_plural = 'spaţii industriale'
