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
    other_fieldsets = (None, {'fields': ('price', 'content', 'is_published',)})
    location_fieldsets = ('Localizare', {'fields': ('county', 'locality', 'address',)})

    formfield_overrides = {
        PointField: {'widget': GooglePointFieldInlineWidget},
    }

    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        location_fieldsets,
        other_fieldsets,
        BaseOfferAdmin.time_fieldsets
    )

    list_display = ('name', 'slug', 'address', 'price')
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
    fieldsets = (
        SaleOfferAdmin.basic_info_fieldsets,
        (None, {'fields': ('is_residential_complex', 'residential_complex_link')}),
        SaleOfferAdmin.location_fieldsets,
        SaleOfferAdmin.other_fieldsets,
        SaleOfferAdmin.time_fieldsets
    )

    # class Media:
    #     js = ['/static/common/js/show-hide.js']


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
