from django.urls import path, include
from rest_framework import routers

from administration import views
from administration.views import FaviconView

router = routers.DefaultRouter()
router.register('settings', views.SettingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/favicon.ico', FaviconView.as_view(), name='favicon-view'),
    path('api/admin/edit-profile', views.edit_profile, name='edit-profile'),
    # path('api/current-user', views.current_user, name='current-user'),
]
