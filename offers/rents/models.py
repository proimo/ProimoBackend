from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from offers.models import OfferImages, BaseOfferModel


#######################################
# Base classes
class RentOffer(BaseOfferModel):
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
    pass


class HouseRentImages(OfferImages):
    pass


class LandRentImages(OfferImages):
    pass


class CommercialSpaceRentImages(OfferImages):
    pass


class OfficeRentImages(OfferImages):
    pass


class SpecialPropertyRentImages(OfferImages):
    pass


class IndustrialSpaceRentImages(OfferImages):
    pass
