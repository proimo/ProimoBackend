from django.contrib import admin

from offers.models import Offer, OfferImage


class OfferImageInline(admin.TabularInline):
    model = OfferImage
    extra = 1


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'region', 'address', 'price', 'surface', 'created', 'updated')
    list_filter = ['region', 'created', 'updated']
    search_fields = ['title', 'address', 'surface']
    inlines = [OfferImageInline]
