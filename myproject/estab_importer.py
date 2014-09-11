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
    print(len(estabs))

    for o in reader_o:
        record = GeocodedEstab(**o)
        record_exists = estabs.filter(estab_id=record.estab_id).exists()
        if record_exists:
            print("record exists")
        else:
            record.save()


def get_csv(filename):
    url = BASEURL + today + '/' + filename

    response = urllib2.urlopen(url)
    reader_o = csv.DictReader(response)
    return load(reader_o)


def load_csv():
    get_csv('estabs_tbl.csv')


if __name__ == '__main__':
    load_csv()