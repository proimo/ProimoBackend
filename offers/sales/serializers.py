from offers.sales.models import ApartmentSale, ApartmentSaleImages, HouseSaleImages, LandSaleImages, \
    CommercialSpaceSaleImages, OfficeSaleImages, SpecialPropertySaleImages, IndustrialSpaceSaleImages, LandSale, \
    HouseSale, SpecialPropertySale, OfficeSale, CommercialSpaceSale, IndustrialSpaceSale

from offers.serializers import BaseImagesSerializers, BaseOfferSerializer


#######################################
# Images serializers
class ApartmentSaleImagesSerializer(BaseImagesSerializers):
    class Meta(BaseImagesSerializers.Meta):
        model = ApartmentSaleImages


class HouseSaleImagesSerializer(BaseImagesSerializers):
    class Meta(BaseImagesSerializers.Meta):
        model = HouseSaleImages


class LandSaleImagesSerializer(BaseImagesSerializers):
    class Meta(BaseImagesSerializers.Meta):
        model = LandSaleImages


class CommercialSpaceSaleImagesSerializer(BaseImagesSerializers):
    class Meta(BaseImagesSerializers.Meta):
        model = CommercialSpaceSaleImages


class OfficeSaleImagesSerializer(BaseImagesSerializers):
    class Meta(BaseImagesSerializers.Meta):
        model = OfficeSaleImages


class SpecialPropertySaleImagesSerializer(BaseImagesSerializers):
    class Meta(BaseImagesSerializers.Meta):
        model = SpecialPropertySaleImages


class IndustrialSpaceSaleImagesSerializer(BaseImagesSerializers):
    class Meta(BaseImagesSerializers.Meta):
        model = IndustrialSpaceSaleImages


#######################################
# Models serializers
class ApartmentSaleSerializer(BaseOfferSerializer):
    images = ApartmentSaleImagesSerializer(many=True, read_only=True)

    class Meta(BaseOfferSerializer.Meta):
        model = ApartmentSale


class LandSaleSerializer(BaseOfferSerializer):
    images = LandSaleImagesSerializer(many=True, read_only=True)

    class Meta(BaseOfferSerializer.Meta):
        model = LandSale


class HouseSaleSerializer(BaseOfferSerializer):
    images = HouseSaleImagesSerializer(many=True, read_only=True)

    class Meta(BaseOfferSerializer.Meta):
        model = HouseSale


class SpecialPropertySaleSerializer(BaseOfferSerializer):
    images = SpecialPropertySaleImagesSerializer(many=True, read_only=True)

    class Meta(BaseOfferSerializer.Meta):
        model = SpecialPropertySale


class OfficeSaleSerializer(BaseOfferSerializer):
    images = OfficeSaleImagesSerializer(many=True, read_only=True)

    class Meta(BaseOfferSerializer.Meta):
        model = OfficeSale


class CommercialSpaceSaleSerializer(BaseOfferSerializer):
    images = CommercialSpaceSaleImagesSerializer(many=True, read_only=True)

    class Meta(BaseOfferSerializer.Meta):
        model = CommercialSpaceSale


class IndustrialSpaceSaleSerializer(BaseOfferSerializer):
    images = IndustrialSpaceSaleImagesSerializer(many=True, read_only=True)

    class Meta(BaseOfferSerializer.Meta):
        model = IndustrialSpaceSale
