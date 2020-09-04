import admin_thumbnails
from django.contrib import admin
from django.contrib.gis.db.models import PointField
from mapwidgets import GooglePointFieldInlineWidget

from offers.sales.models import ApartmentSale, HouseSale, LandSale, CommercialSpaceSale, OfficeSale, \
    SpecialPropertySale, IndustrialSpaceSale, ApartmentSaleImages


@admin_thumbnails.thumbnail('image', background=True)
class OfferImageInline(admin.TabularInline):
    extra = 0

    class Meta:
        abstract = True


class ApartmentSaleImageInline(OfferImageInline):
    model = ApartmentSaleImages


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


@admin.register(ApartmentSale)
class ApartmentSaleAdmin(SaleOfferAdmin):
    inlines = (ApartmentSaleImageInline,)
    fieldsets = (
        SaleOfferAdmin.basic_info_fieldsets,
        SaleOfferAdmin.location_fieldsets,
        SaleOfferAdmin.other_fieldsets,
        SaleOfferAdmin.time_fieldsets
    )


@admin.register(HouseSale)
class HouseSaleAdmin(SaleOfferAdmin):
    pass


@admin.register(LandSale)
class LandSaleAdmin(SaleOfferAdmin):
    pass


@admin.register(CommercialSpaceSale)
class CommercialSpaceSaleAdmin(SaleOfferAdmin):
    pass


@admin.register(OfficeSale)
class OfficeSaleAdmin(SaleOfferAdmin):
    pass


@admin.register(SpecialPropertySale)
class SpecialPropertySaleAdmin(SaleOfferAdmin):
    pass


@admin.register(IndustrialSpaceSale)
class IndustrialSpaceSaleAdmin(SaleOfferAdmin):
    pass
