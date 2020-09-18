import admin_thumbnails
from django.contrib.admin import TabularInline
from django.contrib.gis.db.models import PointField, ForeignKey, CharField, BooleanField, SET_NULL, ImageField, CASCADE, \
    Model, TextField
from django.db.models.base import ModelBase
from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet

from administration.models import UserProfile
from common.admin import BaseModelAdmin
from common.models import County, Locality
from common.models import BaseModel
from common.utils import get_upload_path


def remove_agent_field_from(fieldsets):
    for fieldset in fieldsets:
        fieldset[1]['fields'] = [field for field in fieldset[1]['fields'] if not field.__eq__('agent')]


#######################################
# Base classes both for models and admin
class BaseOfferModel(BaseModel):
    agent = ForeignKey(UserProfile, on_delete=SET_NULL, null=True)
    is_published = BooleanField('publicat?', default=False)
    address = PointField('adresă', max_length=200, null=True)
    hide_address_on_imobiliare = BooleanField('ascunde adresa în imobiliare.ro', default=False)
    county = ForeignKey(County, related_name='%(class)ss', related_query_name='%(class)s', on_delete=SET_NULL,
                        null=True, verbose_name='judeţ')
    locality = ForeignKey(Locality, related_name='%(class)ss', related_query_name='%(class)s', on_delete=SET_NULL,
                          null=True, verbose_name='localitate')

    class Meta:
        abstract = True


class WithPrice(Model):
    price = CharField('preţ', max_length=15, blank=True, default=None)
    not_include_vat = BooleanField('nu include TVA', default=False)
    price_details = TextField('alte detalii preţ', blank=True, default=None)
    zero_commission = BooleanField('comision 0%', default=False)
    buyer_commission = CharField('comision cumpărător', max_length=50, blank=True, default=None)

    class Meta:
        abstract = True


class BaseOfferAdmin(BaseModelAdmin):
    basic_info_fieldsets = (None, {'fields': ('name', 'slug', 'agent',)})
    location_fieldsets = (
        'Localizare şi poziţionare pe hartă',
        {'fields': ('county', 'locality', 'hide_address_on_imobiliare', 'address')})
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


class OfferImagesMetaclass(ModelBase):
    """The class extending OfferImages should get a foreign key to the model"""

    def __new__(mcs, name, bases, attrs):
        model = super(OfferImagesMetaclass, mcs).__new__(mcs, name, bases, attrs)
        for b in bases:
            if b.__name__ == "OfferImages":
                foreign_key_name = attrs.pop('foreign_key_name', None)
                if not foreign_key_name:
                    image_index = name.index('Images')
                    foreign_key_name = name[:image_index]
                has_offer = attrs.pop('offer', None)
                if not has_offer:
                    model.add_to_class('offer', ForeignKey(foreign_key_name, related_name='images', on_delete=CASCADE))

        return model


class OfferImages(Model, metaclass=OfferImagesMetaclass):
    image = ImageField('imagine', upload_to=get_upload_path, blank=True, default=None)

    def __str__(self):
        return self.image.name

    class Meta:
        abstract = True
        verbose_name = 'imagine'
        verbose_name_plural = 'imagini'


#######################################
# Offer images admin register with thumbnails
@admin_thumbnails.thumbnail('image', background=True)
class OfferImageInline(TabularInline):
    extra = 0

    class Meta:
        abstract = True


#######################################
# Base serializers class
class BaseReadOnlyOfferViewSet(ReadOnlyModelViewSet):
    """
        retrieve:
            Return an offer instance.

        list:
            Return all offers, ordered by most recently add.
    """

    permission_classes = [permissions.AllowAny]
