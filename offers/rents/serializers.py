from offers.rents.models import ApartmentRent, ApartmentRentImages, HouseRentImages, LandRentImages, \
    CommercialSpaceRentImages, OfficeRentImages, SpecialPropertyRentImages, IndustrialSpaceRentImages, LandRent, \
    HouseRent, SpecialPropertyRent, OfficeRent, CommercialSpaceRent, IndustrialSpaceRent

#######################################
# Images serializers
from offers.serializers import BaseImagesSerializers, BaseOfferSerializer


class ApartmentRentImagesSerializer(BaseImagesSerializers):
    class Meta(BaseImagesSerializers.Meta):
        model = ApartmentRentImages


class HouseRentImagesSerializer(BaseImagesSerializers):
    class Meta(BaseImagesSerializers.Meta):
        model = HouseRentImages


class LandRentImagesSerializer(BaseImagesSerializers):
    class Meta(BaseImagesSerializers.Meta):
        model = LandRentImages


class CommercialSpaceRentImagesSerializer(BaseImagesSerializers):
    class Meta(BaseImagesSerializers.Meta):
        model = CommercialSpaceRentImages


class OfficeRentImagesSerializer(BaseImagesSerializers):
    class Meta(BaseImagesSerializers.Meta):
        model = OfficeRentImages


class SpecialPropertyRentImagesSerializer(BaseImagesSerializers):
    class Meta(BaseImagesSerializers.Meta):
        model = SpecialPropertyRentImages


class IndustrialSpaceRentImagesSerializer(BaseImagesSerializers):
    class Meta(BaseImagesSerializers.Meta):
        model = IndustrialSpaceRentImages


#######################################
# Models serializers
class ApartmentRentSerializer(BaseOfferSerializer):
    images = ApartmentRentImagesSerializer(many=True, read_only=True)

    class Meta(BaseOfferSerializer.Meta):
        model = ApartmentRent


class LandRentSerializer(BaseOfferSerializer):
    images = LandRentImagesSerializer(many=True, read_only=True)

    class Meta(BaseOfferSerializer.Meta):
        model = LandRent


class HouseRentSerializer(BaseOfferSerializer):
    images = HouseRentImagesSerializer(many=True, read_only=True)

    class Meta(BaseOfferSerializer.Meta):
        model = HouseRent


class SpecialPropertyRentSerializer(BaseOfferSerializer):
    images = SpecialPropertyRentImagesSerializer(many=True, read_only=True)

    class Meta(BaseOfferSerializer.Meta):
        model = SpecialPropertyRent


class OfficeRentSerializer(BaseOfferSerializer):
    images = OfficeRentImagesSerializer(many=True, read_only=True)

    class Meta(BaseOfferSerializer.Meta):
        model = OfficeRent


class CommercialSpaceRentSerializer(BaseOfferSerializer):
    images = CommercialSpaceRentImagesSerializer(many=True, read_only=True)

    class Meta(BaseOfferSerializer.Meta):
        model = CommercialSpaceRent


class IndustrialSpaceRentSerializer(BaseOfferSerializer):
    images = IndustrialSpaceRentImagesSerializer(many=True, read_only=True)

    class Meta(BaseOfferSerializer.Meta):
        model = IndustrialSpaceRent
