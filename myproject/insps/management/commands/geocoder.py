from django.core.management.base import BaseCommand, CommandError
from insps.models import GeocodedEstab
from googlegeocoder import GoogleGeocoder
import time

class Command(BaseCommand):
    def handle(self, *args, **options):
        geocoder = GoogleGeocoder()

        estabs_to_geocode = GeocodedEstab.objects.filter(latitude=None)
        for estab in estabs_to_geocode:
            #print("Address to geocode: %s") % estab.address
            try:
                search = geocoder.get(estab.address)
                time.sleep(1.5)
                estab.latitude = search[0].geometry.location.lat
                estab.longitude = search[0].geometry.location.lng
                #print("Latitude: %s, Longitude: %s \n") % (estab.latitude, estab.longitude)
                estab.save()
            except:
                print(("Couldn't geocode."))
        