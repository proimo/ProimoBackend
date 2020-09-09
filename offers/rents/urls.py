from django.urls import path, include
from rest_framework import routers

from offers.rents import views

router = routers.DefaultRouter()
router.register('apartments', views.ApartmentRentViewSet)
router.register('houses', views.HouseRentViewSet)
router.register('lands', views.LandRentViewSet)
router.register('commercial-spaces', views.CommercialSpaceRentViewSet)
router.register('offices', views.OfficeRentViewSet)
router.register('special-properties', views.SpecialPropertyRentViewSet)
router.register('industrial-spaces', views.IndustrialSpaceRentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
