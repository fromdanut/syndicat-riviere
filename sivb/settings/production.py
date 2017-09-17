#-*- coding: utf-8 -*-

"""Production settings for Heroku"""

import os
from django.conf import settings
import dj_database_url

# Disable debug mode.
DEBUG = False
TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']
DATABASES = settings.DATABASES
SECRET_KEY = os.environ['SECRET_KEY']
SESSION_COOKIE_SECURE = True

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# Extra places for collectstatic to find static files.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),
                   )
# S3 media files service
STATICFILES_LOCATION = 'static'
MEDIAFILES_LOCATION = 'media'

AWS_QUERYSTRING_AUTH = False
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
STATIC_ROOT = "https://%s/static" % AWS_S3_CUSTOM_DOMAIN


MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'


# Heroku need to get GDLA and GEOS library for the map app.
DATABASES['default'] =  dj_database_url.config()
DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'
GDAL_LIBRARY_PATH = os.getenv('GDAL_LIBRARY_PATH')
GEOS_LIBRARY_PATH = os.getenv('GEOS_LIBRARY_PATH')
