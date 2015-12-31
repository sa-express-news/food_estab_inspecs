#!/usr/bin/env python
import os
from os import environ
import sys
#from myproject.settings.secrets_json import get_secret

if __name__ == "__main__":

    DJANGO_SETTINGS_MODULE = environ['DJANGO_SETTINGS_MODULE']
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
