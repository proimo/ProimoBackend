"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from main import settings
from website import views

schema_view = get_schema_view(
    openapi.Info(
        title="Proimo API",
        default_version='v1',
        description="https://proimo.ro",
        contact=openapi.Contact(email="danpercic86@gmail.com"),
        license=openapi.License(name="MIT"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('announcement', views.AnnouncementViewSet)

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('admin/ckeditor/', include('ckeditor_uploader.urls')),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  path('api/', include(router.urls)),
                  path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
