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
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

import administration
from main import settings
from administration.urls import router
from offers import sales, rents
from offers.sales import urls
from offers.rents import urls

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

urlpatterns = i18n_patterns(
    path('', RedirectView.as_view(url='/api/admin/')),
    path('api/', include(administration.urls)),
    path('api/sales/', include(sales.urls)),
    path('api/rents/', include(rents.urls)),
    path('api/admin/', admin.site.urls, name='index'),
    path('api/ckeditor/', include('ckeditor_uploader.urls')),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
    prefix_default_language=False,
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
