import urllib2
import csv
import datetime
import os
from os import environ

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
DJANGO_SETTINGS_MODULE = environ['DJANGO_SETTINGS_MODULE']
from insps.models import Inspection

BASEURL = 'https://s3.amazonaws.com/inspections-csvs/'

def make_today():
    today = datetime.datetime.now().strftime("%m_%d_%y")
    return today

def load(reader_o):
    inspections = Inspection.objects.all()
    inspections_length = len(inspections)
    print("Initial inspection length:%s") % inspections_length

    for o in reader_o:
        record = Inspection(**o)
        record_exists = inspections.filter(inspection_key=record.inspection_key).exists()
        if record_exists:
            print("record exists")

        else:
            print("new record")
            record.save() 

    inspections = Inspection.objects.all()
    final_inspections_length = len(inspections)
    print("Final inspection length: %s") % final_inspections_length


def get_csv(filename):
    # url = BASEURL + make_today() + '/' + filename
    url = BASEURL + "01_00_00" + '/' + filename

    response = urllib2.urlopen(url)
    reader_o = csv.DictReader(response)
    return load(reader_o)


def load_csv():
    get_csv('inspections_tbl.csv')