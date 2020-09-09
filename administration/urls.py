from django.urls import path, include
from rest_framework import routers

from administration import views
from administration.views import FaviconView

router = routers.DefaultRouter()
router.register('settings', views.SettingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('favicon.ico', FaviconView.as_view(), name='favicon-view'),
    path('dumpdata/', views.generate_seed),
    path('loaddata/', views.load_seed),
    path('downloaddata/', views.download_seed),
]
