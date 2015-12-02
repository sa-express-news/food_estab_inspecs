import urllib2
import csv
import datetime
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
from insps.models import GeocodedEstab

BASEURL = 'https://s3.amazonaws.com/inspections-csvs/'

def make_today():
    today = datetime.datetime.now().strftime("%m_%d_%y")
    return today

def load(reader_o):
    estabs = GeocodedEstab.objects.all()
    initial_estab_count = len(estabs)
    print('Initial estab count %s') % initial_estab_count 

    for o in reader_o:
        record = GeocodedEstab(**o)
        record_exists = estabs.filter(estab_id=record.estab_id).exists()
        if record_exists:
            print("record exists")
        else:
            record.save()
            print("record saved")

    estabs = GeocodedEstab.objects.all()
    final_estab_count = len(estabs)
    print('Final estab count %s') % final_estab_count 



def get_csv(filename):
    # url = BASEURL + make_today() + '/' + filename
    url = BASEURL + "11_22_15" + '/' + filename

    response = urllib2.urlopen(url)
    reader_o = csv.DictReader(response)
    return load(reader_o)


def load_csv():
    get_csv('estabs_tbl.csv')