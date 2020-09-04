import admin_thumbnails
from django.contrib import admin
from django.contrib.gis.db.models import PointField
from mapwidgets import GooglePointFieldInlineWidget

from offers.sales.models import ApartmentSale, HouseSale, LandSale, CommercialSpaceSale, OfficeSale, \
    SpecialPropertySale, IndustrialSpaceSale, ApartmentSaleImages, HouseSaleImages, LandSaleImages, \
    CommercialSpaceSaleImages, SpecialPropertySaleImages, IndustrialSpaceSaleImages, OfficeSaleImages


#######################################
# Model's base admin inline / model
@admin_thumbnails.thumbnail('image', background=True)
class OfferImageInline(admin.TabularInline):
    extra = 0

    class Meta:
        abstract = True


class SaleOfferAdmin(admin.ModelAdmin):
    basic_info_fieldsets = (None, {'fields': ('name', 'slug')})
    other_fieldsets = (None, {'fields': ('price', 'content',)})
    location_fieldsets = ('Localizare', {'fields': ('region', 'address')})
    time_fieldsets = ('Creat/Modificat', {
        'classes': ('collapse',),
        'fields': ('created', 'updated',)
    })

    formfield_overrides = {
        PointField: {'widget': GooglePointFieldInlineWidget},
    }

    fieldsets = (
        basic_info_fieldsets,
        location_fieldsets,
        other_fieldsets,
        time_fieldsets
    )

    list_display = ('name', 'slug', 'region', 'address', 'price')
    list_display_links = ['name']
    prepopulated_fields = {'slug': ['name', ]}
    list_filter = ['region', 'created', 'updated']
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
        SaleOfferAdmin.location_fieldsets,
        SaleOfferAdmin.other_fieldsets,
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
