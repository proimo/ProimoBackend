"""
Django settings for main project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

from corsheaders.defaults import default_methods, default_headers
from decouple import config
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _

AdminSite.site_header = 'Proimo - panoul de administrare'
AdminSite.site_title = 'Proimo - panoul de administrare'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']
# Application definition

INSTALLED_APPS = [
    'offers.sales',
    'offers.rents',
    'administration',
    'crm',
    'common',

    'phonenumber_field',
    'rest_framework',
    'rest_framework_gis',
    'rest_framework_swagger',
    'drf_yasg',
    'ckeditor',
    'ckeditor_uploader',
    'corsheaders',
    'mapwidgets',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_METHODS = default_methods
CORS_ALLOW_HEADERS = default_headers

ROOT_URLCONF = 'main.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'main.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='5432')
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_USER_MODEL = 'administration.User'
AUTH_PROFILE_MODULE = 'administration.UserProfile'
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ro'
LANGUAGES = [
    ('ro', _('Romanian')),
]

TIME_ZONE = 'Europe/Athens'
USE_I18N = True
USE_L10N = True
USE_TZ = True

####################################
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')
MEDIA_URL = '/media/'

####################################
#    CKEDITOR CONFIGURATION

CKEDITOR_JQUERY_URL = 'https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': None,
    },
}

#######################################
# REST API Framework config
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

#######################################
# MAP CONFIGS
MAP_WIDGETS = {
    "GOOGLE_MAP_API_KEY": config('GMAPS_API_KEY'),
    "GooglePointFieldWidget": (
        ("zoom", 15),
        ("mapCenterLocationName", "bucharest"),
        ("GooglePlaceAutocompleteOptions", {'componentRestrictions': {'country': 'ro'}}),
        ("markerFitZoom", 12),
    ),
}

GOOGLE_MAPS_API_KEY = config('GMAPS_API_KEY')

#######################################
# THUMBNAIL CONFIGS
ADMIN_THUMBNAIL_DEFAULT_LABEL = 'Previzualizare'
ADMIN_THUMBNAIL_STYLE = {'display': 'block', 'width': '200px', 'height': 'auto'}
ADMIN_THUMBNAIL_BACKGROUND_STYLE = {'background': '#808080'}

#######################################
# LOGGING CONFIGS
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': False,
        },
    },
}


if not DEBUG:
    GDAL_LIBRARY_PATH = '/usr/lib/libgdal.so.27'
    GEOS_LIBRARY_PATH = '/usr/lib/libgeos_c.so.1'
