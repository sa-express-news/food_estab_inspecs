from django.core.management.base import BaseCommand, CommandError
from insps.models import GeocodedEstab
from googlegeocoder import GoogleGeocoder
import csv

class Command(BaseCommand):

    def handle(self, *args, **options):
        print("test")