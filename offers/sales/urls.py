from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('offers', views.OfferViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
