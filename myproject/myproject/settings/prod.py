from .base import * 

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': environ['NAME'],
        'USER': environ['USER'],
        'PASSWORD': environ['PASSWORD'],
        'HOST': environ['DATABASE_HOST'],
        'PORT': environ['DBPORT'],
    }
}

TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates'),)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
###########################################################

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
