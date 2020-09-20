from django.contrib import admin
from django.contrib.gis.db.models import PointField
from mapwidgets import GooglePointFieldInlineWidget

from offers.models import OfferImageInline, BaseOfferAdmin
from offers.sales.models import ApartmentSale, HouseSale, LandSale, CommercialSpaceSale, OfficeSale, \
    SpecialPropertySale, IndustrialSpaceSale, ApartmentSaleImages, HouseSaleImages, LandSaleImages, \
    CommercialSpaceSaleImages, SpecialPropertySaleImages, IndustrialSpaceSaleImages, OfficeSaleImages


#######################################
# Model's base admin inline / model
class SaleOfferAdmin(BaseOfferAdmin):
    other_fieldsets = (None, {'fields': ('is_published',)})
    location_fieldsets = ('Localizare', {'fields': ('county', 'locality', 'address',)})
    price_fieldsets = ('Preţ', {'fields': (
        ('total_price', 'total_price_currency'), ('util_price', 'util_price_currency'),
        'not_include_vat', 'price_details', 'zero_commission', 'buyer_commission'
    )})

    formfield_overrides = {
        PointField: {'widget': GooglePointFieldInlineWidget},
    }

    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        location_fieldsets,
        price_fieldsets,
        other_fieldsets,
        BaseOfferAdmin.time_fieldsets
    )

    list_display = ('name', 'slug', 'address')
    list_filter = ['created', 'updated']
    search_fields = ['name', 'slug', 'address']

    class Meta:
        abstract = True


#######################################
# Model's inlines
class ApartmentSaleImagesInline(OfferImageInline):
    model = ApartmentSaleImages


class HouseSaleImagesInline(OfferImageInline):
    model = HouseSaleImages


class LandSaleImagesInline(OfferImageInline):
    model = LandSaleImages


class CommercialSpaceSaleImagesInline(OfferImageInline):
    model = CommercialSpaceSaleImages


class OfficeSaleImagesInline(OfferImageInline):
    model = OfficeSaleImages


class SpecialPropertySaleImagesInline(OfferImageInline):
    model = SpecialPropertySaleImages


class IndustrialSpaceSaleImagesInline(OfferImageInline):
    model = IndustrialSpaceSaleImages


#######################################
# Model's admin configs
@admin.register(ApartmentSale)
class ApartmentSaleAdmin(SaleOfferAdmin):
    inlines = (ApartmentSaleImagesInline,)
    apartment_characteristics_fieldsets = ('Caracteristici apartament', {'fields': (
        'apartment_type', 'partitioning_type', 'level', 'comfort', 'util_surface', 'total_util_surface',
        'constructed_surface', 'description')})
    rooms_fieldsets = ('Încăperi şi anexe', {'fields': (('rooms_nr', 'garages_nr'), ('kitchens_nr', 'parking_lots_nr'),
                                                        ('balconies_nr', 'closed_balconies_nr'), 'bathrooms_nr')})
    building_fieldsets = ('Imobil', {'fields': (
        'building_type', ('has_basement', 'has_semi_basement', 'has_ground_floor', 'levels_nr', 'has_mansard'),
        'building_year', 'building_period', 'resistance_structure'
    )})
    other_fieldsets = ('Alte detalii', {'fields': ('other_details', 'vices', 'display_expiry_date', 'disponibility')})
    destination_fieldsets = (
        'Destinaţie', {'fields': (('is_residential', 'is_comercial', 'for_offices', 'for_vacation'),)})
    exclusivity_fieldsets = ('Exclusivitate',
                             {'fields': ('has_exclusivity', 'contract', 'validity_from', 'validity_up_to'),
                              'classes': ('collapse',)})
    other_zone_details_fieldsets = ('Alte detalii zonă', {
        'fields': (('asphalted_street', 'concreted_street', 'paved_street', 'soil_street', 'undeveloped_street'),
                   ('has_illuminated_street', 'public_transport'))})
    general_utilities_fieldsets = ('Utilităţi generale', {'fields': (
        ('has_current', 'has_water', 'has_sewerage'),
        ('has_gas', 'has_catv', 'has_phone', 'has_international_phone'))})
    heating_system_fieldsets = ('Sistem încălzire', {'fields': (
        ('has_heating', 'has_own_boiler', 'has_building_boiler'),
        ('has_fireplace_or_terracotta', 'has_radiator', 'has_flooring_heating'))})
    climate_fieldsets = ('Climatizare', {'fields': (('has_air_conditioning', 'has_fan', 'has_air_heater'),)})
    internet_fieldsets = (
        'Acces internet', {'fields': (('has_wired_net', 'has_fiber', 'has_wireless', 'has_dial_up'),)})
    interior_state_fieldsets = ('Stare interior', {'fields': (('is_renovated', 'is_good', 'need_renovation'),)})

    readonly_fields = ['has_ground_floor']
    fieldsets = (
        SaleOfferAdmin.basic_info_fieldsets,
        (None, {'fields': ('is_residential_complex', 'residential_complex_link')}),
        SaleOfferAdmin.location_fieldsets,
        SaleOfferAdmin.price_fieldsets,
        apartment_characteristics_fieldsets,
        rooms_fieldsets,
        building_fieldsets,
        other_fieldsets,
        destination_fieldsets,
        exclusivity_fieldsets,
        other_zone_details_fieldsets,
        general_utilities_fieldsets,
        heating_system_fieldsets,
        climate_fieldsets,
        internet_fieldsets,
        interior_state_fieldsets,
        SaleOfferAdmin.time_fieldsets
    )


@admin.register(HouseSale)
class HouseSaleAdmin(SaleOfferAdmin):
    inlines = (HouseSaleImagesInline,)


@admin.register(LandSale)
class LandSaleAdmin(SaleOfferAdmin):
    inlines = (LandSaleImagesInline,)


@admin.register(CommercialSpaceSale)
class CommercialSpaceSaleAdmin(SaleOfferAdmin):
    inlines = (CommercialSpaceSaleImagesInline,)


@admin.register(OfficeSale)
class OfficeSaleAdmin(SaleOfferAdmin):
    inlines = (OfficeSaleImagesInline,)


@admin.register(SpecialPropertySale)
class SpecialPropertySaleAdmin(SaleOfferAdmin):
    inlines = (SpecialPropertySaleImagesInline,)


@admin.register(IndustrialSpaceSale)
class IndustrialSpaceSaleAdmin(SaleOfferAdmin):
    inlines = (IndustrialSpaceSaleImagesInline,)
