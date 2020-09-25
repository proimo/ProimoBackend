#######################################
# Offer images admin register with thumbnails
import admin_thumbnails
from django.contrib.admin import TabularInline
from django.contrib.gis.db.models import PointField
from mapwidgets import GooglePointFieldInlineWidget

from administration.models import UserProfile
from common.admin import BaseModelAdmin
from offers.fieldsets import hotel_services_fieldsets, building_services_fieldsets, building_features_fieldsets, \
    diverse_fieldsets, appliances_fieldsets, furnished_fieldsets, counters_fieldsets, kitchen_fieldsets, \
    walls_fieldsets, interior_doors_fieldsets, floor_fieldsets, heat_isolation_fieldsets, entrance_door_fieldsets, \
    rolls_fieldsets, louver_fieldsets, windows_fieldsets, interior_state_fieldsets, internet_fieldsets, \
    climate_fieldsets, heating_system_fieldsets, other_zone_details_fieldsets, exclusivity_fieldsets, \
    destination_fieldsets, other_fieldsets, rooms_fieldsets, sale_price_fieldsets


def remove_agent_field_from(fieldsets):
    for fieldset in fieldsets:
        fieldset[1]['fields'] = [field for field in fieldset[1]['fields'] if not field.__eq__('agent')]


@admin_thumbnails.thumbnail('image', background=True)
class OfferImageInline(TabularInline):
    extra = 0

    class Meta:
        abstract = True


class BaseOfferAdmin(BaseModelAdmin):
    basic_info_fieldsets = (
        None, {
            'fields': ('name', 'slug', 'agent', 'description')})
    location_fieldsets = (
        'Localizare şi poziţionare pe hartă', {
            'fields': ('county', 'locality', 'sector', 'hide_address_on_imobiliare', 'address',
                       'hide_exact_location_on_imobiliare', 'postal_code', 'neighborhood')})
    is_published_fieldsets = (
        None, {
            'fields': ('is_published',)})

    autocomplete_fields = ('agent', 'county', 'locality')
    formfield_overrides = {
        PointField: {'widget': GooglePointFieldInlineWidget},
    }

    list_display = ('name', 'slug', 'address')
    list_filter = ['created', 'updated']
    search_fields = ['name', 'slug', 'address']

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


class HouseBaseAdmin(BaseOfferAdmin):
    building_fieldsets = (
        'Imobil', {
            'fields': (('has_basement', 'has_semi_basement', 'has_ground_floor', 'levels_nr', 'has_mansard'),
                       'building_year', 'building_period', 'resistance_structure', 'roof_cover')})
    surfaces_fieldsets = (
        'Suprafeţe', {
            'fields': ('util_surface', 'constructed_surface', 'unfolded_surface', 'terrain_surface', 'street_fronts_nr',
                       'street_front', 'terrace_nr', 'terrace_surface')})
    general_utilities_fieldsets = (
        'Utilităţi generale', {
            'fields': (('has_current', 'has_three_phase_current', 'has_water', 'has_sewerage', 'has_septic_tank',
                        'has_gas', 'has_catv', 'has_phone', 'has_phone_station', 'has_international_phone'),)})
    other_util_spaces = (
        'Alte spaţii utile', {
            'fields': (('has_cellar', 'has_wine_cellar', 'has_service_wc', 'has_storage_space', 'has_dressing',
                        'has_annexes', 'has_dependencies'),)})

    list_display = ('name', 'slug', 'address')
    list_filter = ['created', 'updated']
    search_fields = ['name', 'slug', 'address']

    readonly_fields = ['has_ground_floor']
    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        BaseOfferAdmin.location_fieldsets,
        rooms_fieldsets,
        surfaces_fieldsets,
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
        windows_fieldsets,
        louver_fieldsets,
        rolls_fieldsets,
        entrance_door_fieldsets,
        heat_isolation_fieldsets,
        floor_fieldsets,
        interior_doors_fieldsets,
        walls_fieldsets,
        other_util_spaces,
        kitchen_fieldsets,
        counters_fieldsets,
        furnished_fieldsets,
        appliances_fieldsets,
        diverse_fieldsets,
        building_features_fieldsets,
        building_services_fieldsets,
        hotel_services_fieldsets,
        BaseOfferAdmin.time_fieldsets
    )


class LandBaseAdmin(BaseOfferAdmin):
    terrain_characteristics_fieldsets = (
        'Caracteristici teren', {
            'fields': (('land_type', 'street_fronts_nr'), ('classification', 'street_front'),
                       ('terrain_surface', 'terrain_surface_type'), 'terrain_angle', ('pot', 'cut'),
                       ('height_regime', 'urban_coefficients_source'), ('constructed_surface', 'access_road_width'),
                       'terrain_construction', 'documents', 'plots_lot', 'plots_lot_name')})
    utilities_fieldsets = (
        'Utilităţi', {
            'fields': (('has_water', 'has_current', 'has_three_phase_current', 'has_sewerage', 'has_irrigation_system',
                        'has_gas', 'has_utilities_nearby'),)})
    other_characteristics_fieldsets = (
        'Alte caracteristici', {
            'fields': (('has_investment_opportunity', 'can_be_demolished', 'can_be_splitted', 'is_near_road',
                        'has_auto_access', 'is_surrounded_terrain'),)})

    fieldsets = (
        BaseOfferAdmin.basic_info_fieldsets,
        BaseOfferAdmin.location_fieldsets,
        terrain_characteristics_fieldsets,
        other_fieldsets,
        destination_fieldsets,
        exclusivity_fieldsets,
        utilities_fieldsets,
        other_zone_details_fieldsets,
        other_characteristics_fieldsets,
        BaseOfferAdmin.time_fieldsets
    )
