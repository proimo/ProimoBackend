from django.urls import path, include
from rest_framework import routers

from offers.sales import views

router = routers.DefaultRouter()
router.register('apartments', views.ApartmentSaleViewSet)
router.register('houses', views.HouseSaleViewSet)
router.register('lands', views.LandSaleViewSet)
router.register('commercial-spaces', views.CommercialSpaceSaleViewSet)
router.register('offices', views.OfficeSaleViewSet)
router.register('special-properties', views.SpecialPropertySaleViewSet)
router.register('industrial-spaces', views.IndustrialSpaceSaleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
