from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.gis.db.models import PointField
from django.db import models

from main.models import BaseModel


class Offer(BaseModel):
    class IsForSale(models.TextChoices):
        FOR_SELLING = 'selling', 'Voi vinde'
        FOR_RENT = 'rent', 'Voi închiria'

    is_for_sale = models.CharField('', choices=IsForSale.choices, max_length=10, default=IsForSale.FOR_RENT, null=True)
    slug = models.CharField(max_length=500, default=None, null=True)
    address = PointField('Adresă', max_length=200, null=True)
    region = models.CharField('Regiune', max_length=200, blank=True, default=None)
    price = models.CharField('Preţ', max_length=15, blank=True, default=None)
    is_published = models.BooleanField('Publicat?', default=False)
    content = RichTextUploadingField('Conţinut', default=None, blank=True)

    class Meta:
        abstract = True
        verbose_name = 'Ofertă'
        verbose_name_plural = 'Oferte'


# class OfferImage(models.Model):
#     offer = models.ForeignKey(Offer, related_name='images', on_delete=models.CASCADE)
#     image = models.ImageField('Imagine', upload_to=get_file_name, blank=True, default=None)
#
#     def __str__(self):
#         return self.image.name


class Apartment(Offer):
    class Meta:
        verbose_name = 'Apartament'
        verbose_name_plural = 'Apartamente'


class House(Offer):
    class Meta:
        verbose_name = 'Casă'
        verbose_name_plural = 'Case'


class Land(Offer):
    class Meta:
        verbose_name = 'Teren'
        verbose_name_plural = 'Terenuri'


class CommercialSpace(Offer):
    class Meta:
        verbose_name = 'Spaţiu comercial'
        verbose_name_plural = 'Spaţii comerciale'


class Office(Offer):
    class Meta:
        verbose_name = 'Birou'
        verbose_name_plural = 'Birouri'


class SpecialProperty(Offer):
    class Meta:
        verbose_name = 'Proprietate specială'
        verbose_name_plural = 'Proprietăţi speciale'


class IndustrialSpace(Offer):
    class Meta:
        verbose_name = 'Spaţiu industrial'
        verbose_name_plural = 'Spaţii industriale'
