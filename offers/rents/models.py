from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models import PositiveIntegerField, CharField, BooleanField, TextField

from offers.choices import Currencies, Level, Comfort, BuildingType, PartitioningType
from offers.models import OfferImages, BaseOfferModel, WithRentPrice


#######################################
# Base classes
class RentOfferModel(BaseOfferModel):
    content = RichTextUploadingField('conţinut', default=None, blank=True)

    class Meta:
        abstract = True
        verbose_name = 'ofertă închiriere'
        verbose_name_plural = 'oferte închiriere'


#######################################
# Model classes
class ApartmentRent(RentOfferModel, WithRentPrice):
    zero_commission = BooleanField('Comision 0%', default=False)
    buyer_commission = TextField('Comision cumpărător', blank=True, default=None)

    hotel_regime = BooleanField('regim hotelier', default=False)
    hotel_regime_price = CharField('chirie / zi', max_length=15, blank=True, default=None)
    hotel_regime_currency = CharField('', max_length=4, choices=Currencies.choices, default=Currencies.EUR)

    rooms_nr = PositiveIntegerField('nr. camere', default=0)
    util_surface = CharField('suprafaţa utilă', max_length=50, default=None, blank=True)
    constructed_surface = CharField('suprafaţa construită', max_length=50, default=None, blank=True)
    level = CharField('etaj', max_length=17, choices=Level.choices, default=None, blank=True)
    levels_nr = PositiveIntegerField('nr. niveluri', blank=True, default=None)
    building_type = CharField('tip imobil', max_length=20, choices=BuildingType.choices,
                              default=BuildingType.APARTMENTS_BUILDING)
    bathrooms_nr = PositiveIntegerField('nr. băi', blank=True, default=None)
    partitioning_type = CharField('tip compartimentare', max_length=15, choices=PartitioningType.choices, default=None,
                                  blank=True)
    comfort = CharField('confort', max_length=3, choices=Comfort.choices, default=None, blank=True)

    other_details = TextField('alte detalii', max_length=500, blank=True, default=None)

    class Meta:
        verbose_name = 'apartament'
        verbose_name_plural = 'apartamente'


class HouseRent(RentOfferModel):
    class Meta:
        verbose_name = 'casă'
        verbose_name_plural = 'case'


class LandRent(RentOfferModel):
    class Meta:
        verbose_name = 'teren'
        verbose_name_plural = 'terenuri'


class CommercialSpaceRent(RentOfferModel):
    class Meta:
        verbose_name = 'spaţiu comercial'
        verbose_name_plural = 'spaţii comerciale'


class OfficeRent(RentOfferModel):
    class Meta:
        verbose_name = 'birou'
        verbose_name_plural = 'birouri'


class SpecialPropertyRent(RentOfferModel):
    class Meta:
        verbose_name = 'proprietate specială'
        verbose_name_plural = 'proprietăţi speciale'


class IndustrialSpaceRent(RentOfferModel):
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
