from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.gis.db.models import PointField
from django.db import models

from main.models import BaseModel
from main.utils import get_upload_path


class SaleOffer(BaseModel):
    slug = models.CharField(max_length=500, default=None, null=True)
    address = PointField('adresă', max_length=200, null=True)
    region = models.CharField('regiune', max_length=200, blank=True, default=None)
    price = models.CharField('preţ', max_length=15, blank=True, default=None)
    is_published = models.BooleanField('publicat?', default=False)
    content = RichTextUploadingField('conţinut', default=None, blank=True)

    class Meta:
        abstract = True
        verbose_name = 'ofertă vânzare'
        verbose_name_plural = 'oferte vânzare'


class ApartmentSale(SaleOffer):
    class Meta:
        verbose_name = 'apartament'
        verbose_name_plural = 'apartamente'


class HouseSale(SaleOffer):
    class Meta:
        verbose_name = 'casă'
        verbose_name_plural = 'case'


class LandSale(SaleOffer):
    class Meta:
        verbose_name = 'teren'
        verbose_name_plural = 'terenuri'


class CommercialSpaceSale(SaleOffer):
    class Meta:
        verbose_name = 'spaţiu comercial'
        verbose_name_plural = 'spaţii comerciale'


class OfficeSale(SaleOffer):
    class Meta:
        verbose_name = 'birou'
        verbose_name_plural = 'birouri'


class SpecialPropertySale(SaleOffer):
    class Meta:
        verbose_name = 'proprietate specială'
        verbose_name_plural = 'proprietăţi speciale'


class IndustrialSpaceSale(SaleOffer):
    class Meta:
        verbose_name = 'spaţiu industrial'
        verbose_name_plural = 'spaţii industriale'


class OfferImages(models.Model):
    image = models.ImageField('imagine', upload_to=get_upload_path, blank=True, default=None)

    def __str__(self):
        return self.image.name

    class Meta:
        abstract = True
        verbose_name = 'imagine'
        verbose_name_plural = 'imagini'


class ApartmentSaleImages(OfferImages):
    offer = models.ForeignKey(ApartmentSale, related_name='images', on_delete=models.CASCADE)
