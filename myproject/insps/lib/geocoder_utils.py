from insps.models import GeocodedEstab
from googlegeocoder import GoogleGeocoder
import time

def geocoder():
    geocoder = GoogleGeocoder()
    estabs_to_geocode = GeocodedEstab.objects.filter(latitude=None)
    for estab in estabs_to_geocode:
        try:
            #print("Address to geocode: %s") % estab.address
            search = geocoder.get(estab.address)
            time.sleep(1.5)
        except ValueError:
            #print("Couldn't geocode. %d") % (estab.estab_id)
            continue
        estab.latitude = search[0].geometry.location.lat
        estab.longitude = search[0].geometry.location.lng
        #print("Latitude: %s, Longitude: %s \n") % (estab.latitude, estab.longitude)
        estab.save()
        