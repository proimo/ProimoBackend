from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

#######################################
# Base classes
from offers.models import OfferImages, BaseOfferModel


class SaleOffer(BaseOfferModel):
    content = RichTextUploadingField('conţinut', default=None, blank=True)

    class Meta:
        abstract = True
        verbose_name = 'ofertă vânzare'
        verbose_name_plural = 'oferte vânzare'


#######################################
# Model classes
class ApartmentSale(SaleOffer):
    class Meta:
        verbose_name = 'apartament'
        verbose_name_plural = 'apartamente'


class HouseSale(SaleOffer):
    class Meta:
        verbose_name = 'casă'
        verbose_name_plural = 'case'


class LandSale(SaleOffer):
    class Meta:
        verbose_name = 'teren'
        verbose_name_plural = 'terenuri'


class CommercialSpaceSale(SaleOffer):
    class Meta:
        verbose_name = 'spaţiu comercial'
        verbose_name_plural = 'spaţii comerciale'


class OfficeSale(SaleOffer):
    class Meta:
        verbose_name = 'birou'
        verbose_name_plural = 'birouri'


class SpecialPropertySale(SaleOffer):
    class Meta:
        verbose_name = 'proprietate specială'
        verbose_name_plural = 'proprietăţi speciale'


class IndustrialSpaceSale(SaleOffer):
    class Meta:
        verbose_name = 'spaţiu industrial'
        verbose_name_plural = 'spaţii industriale'


#######################################
# Model classes' images tables
class ApartmentSaleImages(OfferImages):
    offer = models.ForeignKey(ApartmentSale, related_name='images', on_delete=models.CASCADE)


class HouseSaleImages(OfferImages):
    offer = models.ForeignKey(HouseSale, related_name='images', on_delete=models.CASCADE)


class LandSaleImages(OfferImages):
    offer = models.ForeignKey(LandSale, related_name='images', on_delete=models.CASCADE)


class CommercialSpaceSaleImages(OfferImages):
    offer = models.ForeignKey(CommercialSpaceSale, related_name='images', on_delete=models.CASCADE)


class OfficeSaleImages(OfferImages):
    offer = models.ForeignKey(OfficeSale, related_name='images', on_delete=models.CASCADE)


class SpecialPropertySaleImages(OfferImages):
    offer = models.ForeignKey(SpecialPropertySale, related_name='images', on_delete=models.CASCADE)


class IndustrialSpaceSaleImages(OfferImages):
    offer = models.ForeignKey(IndustrialSpaceSale, related_name='images', on_delete=models.CASCADE)
