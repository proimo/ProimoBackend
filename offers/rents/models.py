from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.gis.db.models import PointField
from django.db import models

from main.models import BaseModel
from offers.models import OfferImages


#######################################
# Base classes
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


#######################################
# Model classes
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


#######################################
# Model classes' images tables
class ApartmentRentImages(OfferImages):
    offer = models.ForeignKey(ApartmentRent, related_name='images', on_delete=models.CASCADE)


class HouseRentImages(OfferImages):
    offer = models.ForeignKey(HouseRent, related_name='images', on_delete=models.CASCADE)


class LandRentImages(OfferImages):
    offer = models.ForeignKey(LandRent, related_name='images', on_delete=models.CASCADE)


class CommercialSpaceRentImages(OfferImages):
    offer = models.ForeignKey(CommercialSpaceRent, related_name='images', on_delete=models.CASCADE)


class OfficeRentImages(OfferImages):
    offer = models.ForeignKey(OfficeRent, related_name='images', on_delete=models.CASCADE)


class SpecialPropertyRentImages(OfferImages):
    offer = models.ForeignKey(SpecialPropertyRent, related_name='images', on_delete=models.CASCADE)


class IndustrialSpaceRentImages(OfferImages):
    offer = models.ForeignKey(IndustrialSpaceRent, related_name='images', on_delete=models.CASCADE)
