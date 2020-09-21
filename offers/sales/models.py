from django.db.models import BooleanField, URLField, CharField, PositiveIntegerField, TextField, IntegerField, \
    DecimalField
from offers.choices import ApartmentType, PartitioningType, Level, Comfort, BuildingType, RoofCover, LandType, \
    LandClassification, SurfaceType, URBAN_COEFF_SOURCES, OFFICE_BUILDING_TYPE, PURPOSE_RECOMMENDATION, Currencies, \
    OFFICE_CLASS, BUILDING_STAGE, BUILDING_STATE, COMMERCIAL_BUILDING_TYPE
from offers.models import OfferImages, BaseOfferModel, WithPrice, WithExclusivity, WithSellingPrice, \
    WithRoomsAndAnnexes, WithBuildingInfo, WithOtherDetails, WithDestination, WithOtherZoneDetails, WithHeatingSystem, \
    WithConditioning, WithInternetAccess, WithFinishes, WithFeatures, WithServices, WithSpaceSellingPrice, \
    WithPropertyInfo, WithAdditionalSpaceInfo


#######################################
# Base classes
class SaleOfferModel(BaseOfferModel):
    description = TextField('descriere emoţională', default=None, blank=True)

    class Meta:
        abstract = True
        verbose_name = 'ofertă vânzare'
        verbose_name_plural = 'oferte vânzare'


#######################################
# Model classes
class ApartmentSale(SaleOfferModel, WithSellingPrice, WithExclusivity, WithRoomsAndAnnexes, WithBuildingInfo,
                    WithOtherDetails, WithDestination, WithOtherZoneDetails, WithHeatingSystem, WithConditioning,
                    WithInternetAccess, WithFinishes, WithFeatures, WithServices):
    apartment_type = CharField('tip locuinţă', max_length=11, choices=ApartmentType.choices,
                               default=ApartmentType.APARTAMENT)
    partitioning_type = CharField('tip compartimentare', max_length=15, choices=PartitioningType.choices, default=None,
                                  blank=True)
    level = CharField('etaj', max_length=17, choices=Level.choices, default=None, blank=True)
    comfort = CharField('confort', max_length=3, choices=Comfort.choices, default=None, blank=True)
    util_surface = PositiveIntegerField('suprafaţa utilă (mp)', default=None, blank=True)
    total_util_surface = PositiveIntegerField('suprafaţa utilă totală (mp)', default=None, blank=True)
    constructed_surface = PositiveIntegerField('suprafaţa construită (mp)', default=None, blank=True)

    building_type = CharField('tip imobil', max_length=20, choices=BuildingType.choices,
                              default=BuildingType.APARTMENTS_BUILDING)

    has_current = BooleanField('curent', default=False)
    has_water = BooleanField('apă', default=False)
    has_sewerage = BooleanField('canalizare', default=False)
    has_gas = BooleanField('gaz', default=False)
    has_catv = BooleanField('CATV', default=False)
    has_phone = BooleanField('telefon', default=False)
    has_international_phone = BooleanField('telefon internaţional', default=False)

    has_terrace = BooleanField('terasă', default=False)
    has_service_wc = BooleanField('WC serviciu', default=False)
    has_basement_box = BooleanField('boxă la subsol', default=False)
    has_storage_closet = BooleanField('debara', default=False)

    class Meta:
        verbose_name = 'apartament'
        verbose_name_plural = 'apartamente'


class HouseSale(SaleOfferModel, WithSellingPrice, WithRoomsAndAnnexes, WithBuildingInfo, WithOtherDetails,
                WithDestination, WithExclusivity, WithOtherZoneDetails, WithHeatingSystem, WithConditioning,
                WithInternetAccess, WithFinishes, WithFeatures, WithServices):
    util_surface = PositiveIntegerField('suprafaţa utilă (mp)', default=None, blank=True)
    constructed_surface = PositiveIntegerField('suprafaţa construită (amprentă la sol) (mp)', default=None, blank=True)
    unfolded_surface = PositiveIntegerField('suprafaţă desfăşurată (mp)', default=None, blank=True)
    terrain_surface = PositiveIntegerField('suprafaţă teren (mp)', default=None, blank=True)
    street_fronts_nr = PositiveIntegerField('nr. fronturi stradale', default=None, blank=True)
    street_front = PositiveIntegerField('front stradal (m)', default=None, blank=True)
    terrace_nr = PositiveIntegerField('nr. terase', default=None, blank=True)
    terrace_surface = PositiveIntegerField('suprafaţă terase (mp)', default=None, blank=True)

    roof_cover = CharField('învelitoare acoperiş', max_length=10, choices=RoofCover.choices, default=None, blank=True)

    has_current = BooleanField('curent', default=False)
    has_three_phase_current = BooleanField('curent trifazic', default=False)
    has_water = BooleanField('apă', default=False)
    has_sewerage = BooleanField('canalizare', default=False)
    has_septic_tank = BooleanField('fosă septică', default=False)
    has_gas = BooleanField('gaz', default=False)
    has_catv = BooleanField('CATV', default=False)
    has_phone = BooleanField('telefon', default=False)
    has_phone_station = BooleanField('centrală telefonică', default=False)
    has_international_phone = BooleanField('telefon internaţional', default=False)

    has_cellar = BooleanField('pivniţă', default=False)
    has_wine_cellar = BooleanField('cramă', default=False)
    has_service_wc = BooleanField('WC serviciu', default=False)
    has_storage_space = BooleanField('spaţiu depozitare', default=False)
    has_dressing = BooleanField('dressing', default=False)
    has_annexes = BooleanField('anexe', default=False)
    has_dependencies = BooleanField('dependinţe', default=False)

    class Meta:
        verbose_name = 'casă'
        verbose_name_plural = 'case'


class LandSale(SaleOfferModel, WithSellingPrice, WithOtherDetails, WithDestination, WithExclusivity,
               WithOtherZoneDetails):
    land_type = CharField('tip teren', max_length=12, choices=LandType.choices, default=LandType.CONSTRUCTII)
    street_fronts_nr = PositiveIntegerField('nr. fronturi stradale', default=None, blank=True)
    classification = CharField('clasificare', max_length=12, choices=LandClassification.choices,
                               default=LandClassification.INTRAVILAN)
    street_front = PositiveIntegerField('front stradal (m)', default=None, blank=True)
    terrain_surface = PositiveIntegerField('suprafaţă teren', default=None, blank=True)
    terrain_surface_type = CharField('', max_length=3, choices=SurfaceType.choices, default=SurfaceType.M)
    terrain_angle = IntegerField('înclinaţie teren (%)', default=None, blank=True)
    pot = IntegerField('P.O.T (%)', default=None, blank=True,
                       help_text='Procentajul de ocupare al terenului (suprafaţa ocupată/suprafaţa totală * 100')
    cut = IntegerField('C.U.T (%)', default=None, blank=True,
                       help_text='Coeficientul de utilizare al terenului (suma suprafeţelor desfăşurate/suprafaţa totală * 100')
    height_regime = PositiveIntegerField('regim înălţime (m)', default=None, blank=True)
    urban_coefficients_source = CharField('sursă informaţii coef. urbanistici', max_length=25,
                                          choices=URBAN_COEFF_SOURCES, default=None, blank=True)
    terrain_construction = BooleanField('construcţie pe teren', default=False)
    constructed_surface = PositiveIntegerField('suprafaţă construită (mp)', default=None, blank=True)
    access_road_width = PositiveIntegerField('lăţime drum de acces (m)', default=None, blank=True)
    documents = TextField('acte/avize', default=None, blank=True)
    plots_lot = BooleanField('lot parcele', default=False)
    plots_lot_name = CharField('nume lot parcele', max_length=100, default=None, blank=True)

    has_current = BooleanField('curent', default=False)
    has_three_phase_current = BooleanField('curent trifazic', default=False)
    has_water = BooleanField('apă', default=False)
    has_sewerage = BooleanField('canalizare', default=False)
    has_irrigation_system = BooleanField('sistem irigaţie', default=False)
    has_gas = BooleanField('gaz', default=False)
    has_utilities_nearby = BooleanField('utilităţi în zonă', default=False)

    has_investment_opportunity = BooleanField('oportunitate de investiţie', default=False)
    can_be_demolished = BooleanField('construcţie demolabilă', default=False)
    can_be_splitted = BooleanField('parcelabil', default=False)
    is_near_road = BooleanField('la şosea', default=False)
    has_auto_access = BooleanField('acces auto', default=False)
    is_surrounded_terrain = BooleanField('teren  împrejmuit', default=False)

    class Meta:
        verbose_name = 'teren'
        verbose_name_plural = 'terenuri'


class CommercialSpaceSale(SaleOfferModel, WithExclusivity, WithSpaceSellingPrice, WithPropertyInfo,
                          WithAdditionalSpaceInfo):
    building_type = CharField('tip imobil', max_length=20, choices=COMMERCIAL_BUILDING_TYPE, default=None)
    purpose_recommendation = CharField('recomandare utilizare proprietate', max_length=30,
                                       choices=PURPOSE_RECOMMENDATION, default=None, blank=True)

    space_height = DecimalField('înalţime spaţiu', max_digits=4, decimal_places=2, default=None, blank=True)
    has_show_window = BooleanField('vitrină', default=False)

    has_current = BooleanField('curent', default=False)
    has_water = BooleanField('apă', default=False)
    has_sewerage = BooleanField('canalizare', default=False)
    has_gas = BooleanField('gaz', default=False)
    has_heating = BooleanField('căldură', default=False)
    has_conditioning = BooleanField('climă', default=False)

    class Meta:
        verbose_name = 'spaţiu comercial'
        verbose_name_plural = 'spaţii comerciale'


class OfficeSale(SaleOfferModel, WithSpaceSellingPrice, WithExclusivity, WithPropertyInfo, WithAdditionalSpaceInfo):
    building_type = CharField('tip imobil', max_length=20, choices=OFFICE_BUILDING_TYPE, default=None)
    purpose_recommendation = CharField('recomandare utilizare proprietate', max_length=30,
                                       choices=PURPOSE_RECOMMENDATION, default=None, blank=True)

    office_class = CharField('clasă birouri', max_length=2, choices=OFFICE_CLASS, default=None, blank=True)

    class Meta:
        verbose_name = 'birou'
        verbose_name_plural = 'birouri'


class SpecialPropertySale(SaleOfferModel):
    class Meta:
        verbose_name = 'proprietate specială'
        verbose_name_plural = 'proprietăţi speciale'


class IndustrialSpaceSale(SaleOfferModel):
    class Meta:
        verbose_name = 'spaţiu industrial'
        verbose_name_plural = 'spaţii industriale'


#######################################
# Model classes' images tables
class ApartmentSaleImages(OfferImages):
    foreign_key_name = 'ApartmentSale'


class HouseSaleImages(OfferImages):
    pass


class LandSaleImages(OfferImages):
    pass


class CommercialSpaceSaleImages(OfferImages):
    pass


class OfficeSaleImages(OfferImages):
    pass


class SpecialPropertySaleImages(OfferImages):
    pass


class IndustrialSpaceSaleImages(OfferImages):
    pass
