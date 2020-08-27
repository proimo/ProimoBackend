from django.contrib import admin

from offers.models import Apartment, House, Land, CommercialSpace, Office, SpecialProperty, IndustrialSpace, Offer


# class OfferImageInline(admin.TabularInline):
#     model = OfferImage
#     extra = 0


class OfferAdmin(admin.ModelAdmin):
    basic_info_fieldsets = (None, {'fields': ('is_for_sale', 'name', 'slug')})
    other_fieldsets = (None, {'fields': ('price', 'content')})
    location_fieldsets = ('Localizare', {'fields': ('region', 'address')})
    time_fieldsets = ('Creat/Modificat', {
        'classes': ('collapse',),
        'fields': ('created', 'updated',)
    })

    fieldsets = (
        basic_info_fieldsets,
        location_fieldsets,
        other_fieldsets,
        time_fieldsets
    )
    list_display = ('is_for_sale', 'name', 'slug', 'region', 'address', 'price')
    list_display_links = ['name']
    prepopulated_fields = {'slug': ['name', ]}
    list_filter = ['is_for_sale', 'region', 'created', 'updated']
    search_fields = ['name', 'slug', 'address']


#     inlines = [OfferImageInline]


@admin.register(Apartment)
class ApartmentAdmin(OfferAdmin):
    fieldsets = (
        OfferAdmin.basic_info_fieldsets,
        OfferAdmin.location_fieldsets,
        OfferAdmin.other_fieldsets,
        OfferAdmin.time_fieldsets
    )


@admin.register(House)
class HouseAdmin(OfferAdmin):
    pass


@admin.register(Land)
class LandAdmin(OfferAdmin):
    pass


@admin.register(CommercialSpace)
class CommercialSpaceAdmin(OfferAdmin):
    pass


@admin.register(Office)
class OfficeAdmin(OfferAdmin):
    pass


@admin.register(SpecialProperty)
class SpecialPropertyAdmin(OfferAdmin):
    pass


@admin.register(IndustrialSpace)
class IndustrialSpaceAdmin(OfferAdmin):
    pass
