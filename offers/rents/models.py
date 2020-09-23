from django.db.models import PositiveIntegerField, CharField, TextField

from offers.choices import Level, Comfort, BuildingType, PartitioningType
from offers.models import OfferImages, BaseOfferModel, WithRentPrice, WithHotelRegime, WithRoomsAndAnnexes, \
    WithHouseSurfaces, WithBuildingInfo, WithOtherDetails, WithDestination, WithExclusivity, HouseBaseModel


#######################################
# Model classes
class ApartmentRent(BaseOfferModel, WithHotelRegime):
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


class HouseRent(HouseBaseModel, WithHotelRegime):
    class Meta:
        verbose_name = 'casă'
        verbose_name_plural = 'case'


class LandRent(BaseOfferModel):
    class Meta:
        verbose_name = 'teren'
        verbose_name_plural = 'terenuri'


class CommercialSpaceRent(BaseOfferModel):
    class Meta:
        verbose_name = 'spaţiu comercial'
        verbose_name_plural = 'spaţii comerciale'


class OfficeRent(BaseOfferModel):
    class Meta:
        verbose_name = 'birou'
        verbose_name_plural = 'birouri'


class SpecialPropertyRent(BaseOfferModel):
    class Meta:
        verbose_name = 'proprietate specială'
        verbose_name_plural = 'proprietăţi speciale'


class IndustrialSpaceRent(BaseOfferModel):
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
