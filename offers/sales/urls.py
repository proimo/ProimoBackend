from django.urls import path, include
from rest_framework import routers

from offers.sales import views

router = routers.DefaultRouter()
router.register('apartments', views.ApartmentSaleViewSet)

urlpatterns = [
    path('api/sales/', include(router.urls)),
]
