from urllib.parse import urlparse

from .base import *

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

GDAL_LIBRARY_PATH = '/usr/lib/libgdal.so.27'
GEOS_LIBRARY_PATH = '/usr/lib/libgeos_c.so.1'

SILENCED_SYSTEM_CHECKS = [
    'security.W004',  # SECURE_HSTS_SECONDS
    'security.W008',  # SECURE_SSL_REDIRECT
    'security.W012',  # SESSION_COOKIE_SECURE
    'security.W016',  # CSRF_COOKIE_SECURE
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MIDDLEWARE.insert(0, 'whitenoise.middleware.WhiteNoiseMiddleware')

USE_X_FORWARDED_PORT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
EXTERNAL_URL = config('EXTERNAL_URL')
SESSION_COOKIE_SECURE = urlparse(EXTERNAL_URL).scheme == 'https'
CSRF_COOKIE_SECURE = urlparse(EXTERNAL_URL).scheme == 'https'