from django.urls import path, include
from rest_framework import routers

from website import views

router = routers.DefaultRouter()
router.register('announcements', views.AnnouncementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
