from rest_framework import serializers

from offers.sales.models import OfferImage


class OfferImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfferImage
        fields = '__all__'


# class OfferSerializer(serializers.ModelSerializer):
#     images = OfferImageSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Offer
#         fields = ['id', 'name', 'slug', 'region', 'price', 'surface', 'address', 'content', 'images', 'created']
