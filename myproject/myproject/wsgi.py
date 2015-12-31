import os
from os import environ

DJANGO_SETTINGS_MODULE = environ['DJANGO_SETTINGS_MODULE']
#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
