from rest_framework import serializers

from offers.sales.models import ApartmentSale, ApartmentSaleImages


class ApartmentSaleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentSaleImages
        fields = '__all__'


class ApartmentSaleSerializer(serializers.ModelSerializer):
    images = ApartmentSaleImageSerializer(many=True, read_only=True)

    class Meta:
        model = ApartmentSale
        fields = '__all__'
