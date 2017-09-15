import os
from django.conf import settings

DEBUG = False 
TEMPLATE_DEBUG = False 
#ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = ['127.0.0.1','redelan.hd.free.fr/sivr','redelan.hd.free.fr']
DATABASES = settings.DATABASES
#SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY = 'bonjour'
SESSION_COOKIE_SECURE = None 

# in order map app to work ! find a better way to do it
SERIALIZATION_MODULES = {
    "geojson": "django.contrib.gis.serializers.geojson", 
 }
# database
"""
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
"""

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# Extra places for collectstatic to find static files.
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),
#DOMAINE_NAME = 'redelan.hd.free.fr/sivr/'
#STATICFILES_LOCATION = 'static'
#MEDIAFILES_LOCATION = 'media'
#STATIC_URL = "https://%s/%s/" % (DOMAINE_NAME, STATICFILES_LOCATION)
#STATIC_ROOT = "https://%s/static" % DOMAINE_NAME
#MEDIA_URL = "https://%s/%s/" % (DOMAINE_NAME, MEDIAFILES_LOCATION)
