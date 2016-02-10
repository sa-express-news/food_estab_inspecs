import urllib2
import csv
import datetime
import os
from os import environ

DJANGO_SETTINGS_MODULE = environ['DJANGO_SETTINGS_MODULE']
from insps.models import Inspection

BASEDIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'scraper/data/processed')
BASEURL = 'https://s3.amazonaws.com/inspections-csvs/'

def load(reader_o):
    inspections = Inspection.objects.all()
    inspections_length = len(inspections)
    #print("Initial inspection length:%s") % inspections_length

    for o in reader_o:
        record = Inspection(**o)
        record_exists = inspections.filter(inspection_key=record.inspection_key).exists()
        if record_exists:
            continue
            #print("record exists")
        else:
            #print("new record")
            record.save() 

    inspections = Inspection.objects.all()
    final_inspections_length = len(inspections)
    #print("Final inspection length: %s") % final_inspections_length

def get_csv(filename, loadversion):
    if loadversion == 'initial':
        url = BASEURL + "01_00_00" + '/' + filename
        response = urllib2.urlopen(url)
        reader_o = csv.DictReader(response)
        return load(reader_o)
    elif loadversion == 'update':
        reader_o = csv.DictReader(open(os.path.join(BASEDIR, filename)))
        return load(reader_o)

def load_csv_inspections(loadversion):
    get_csv('inspections_tbl.csv', loadversion)