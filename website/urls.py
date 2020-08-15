from django.urls import path, include
from rest_framework import routers

from website import views
from website.views import FaviconView

router = routers.DefaultRouter()
router.register('announcements', views.AnnouncementViewSet)
router.register('settings', views.SettingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('favicon.ico', FaviconView.as_view(), name='favicon-view'),
]