#######################################
# Offer images admin register with thumbnails
import admin_thumbnails
from django.contrib.admin import TabularInline

from administration.models import UserProfile
from common.admin import BaseModelAdmin


def remove_agent_field_from(fieldsets):
    for fieldset in fieldsets:
        fieldset[1]['fields'] = [field for field in fieldset[1]['fields'] if not field.__eq__('agent')]


@admin_thumbnails.thumbnail('image', background=True)
class OfferImageInline(TabularInline):
    extra = 0

    class Meta:
        abstract = True


class BaseOfferAdmin(BaseModelAdmin):
    basic_info_fieldsets = (None, {'fields': ('name', 'slug', 'agent', 'description')})
    location_fieldsets = ('Localizare şi poziţionare pe hartă', {'fields': (
        'county', 'locality', 'sector', 'hide_address_on_imobiliare', 'address',
        'hide_exact_location_on_imobiliare', 'postal_code', 'neighborhood')})
    autocomplete_fields = ('agent', 'county', 'locality')

    def get_queryset(self, request):
        """if it's not superuser get only current agent's offers"""
        queryset = super(BaseOfferAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        user_profile = UserProfile.objects.get(user=request.user)
        return queryset.filter(agent=user_profile)

    def get_fieldsets(self, request, obj=None):
        """if it's not superuser remove 'agent' field"""
        fieldsets = super(BaseOfferAdmin, self).get_fieldsets(request, obj)
        if request.user.is_superuser is not True:
            remove_agent_field_from(fieldsets)
        return fieldsets

    def save_model(self, request, obj, form, change):
        if obj.agent is None:
            obj.agent = UserProfile.objects.get(user=request.user)
        super(BaseOfferAdmin, self).save_model(request, obj, form, change)

    class Meta:
        abstract = True
