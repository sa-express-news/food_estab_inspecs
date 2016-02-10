import urllib2
import csv
import datetime
import os
from os import environ


DJANGO_SETTINGS_MODULE = environ['DJANGO_SETTINGS_MODULE']
from insps.models import GeocodedEstab

BASEDIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'scraper/data/processed')
BASEURL = 'https://s3.amazonaws.com/inspections-csvs/'

def load(reader_o):
    estabs = GeocodedEstab.objects.all()
    initial_estab_count = len(estabs)
    #print('Initial estab count %s') % initial_estab_count 

    for o in reader_o:
        record = GeocodedEstab(**o)
        record_exists = estabs.filter(estab_id=record.estab_id).exists()
        if record_exists:
            continue
            #print("record exists")
        else:
            record.save()
            #print("record saved")

    estabs = GeocodedEstab.objects.all()
    final_estab_count = len(estabs)
    #print('Final estab count %s') % final_estab_count 



def get_csv(filename, loadversion):
    if loadversion == 'initial':
        url = BASEURL + "01_00_00" + '/' + filename
        response = urllib2.urlopen(url)
        reader_o = csv.DictReader(response)
        return load(reader_o)
    elif loadversion == 'update':
        reader_o = csv.DictReader(open(os.path.join(BASEDIR, filename)))
        return load(reader_o)

def load_csv_estabs(loadversion):
    get_csv('estabs_tbl.csv', loadversion)