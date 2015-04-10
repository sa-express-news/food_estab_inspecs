import urllib2
import csv
import datetime
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
from insps.models import Description

BASEURL = 'https://s3.amazonaws.com/inspections-csvs/'

def make_today():
    today = datetime.datetime.now().strftime("%m_%d_%y")
    return today

def load_descs(new_descs_list, url):
    csv_resp = urllib2.urlopen(url)
    reader_o = csv.DictReader(csv_resp)
    for o in reader_o:
        record = Description(**o)
        if record.inspection_key_id in new_descs_list:
            print("saving new descriptions...")
            record.save()

    descs = Description.objects.all()
    final_count = len(descs)
    print("Final Description model count: %d") % final_count


def get_new_descs_ids(reader_o, url):
    new_descs_list = []   
    descs = Description.objects.all()
    initial_count = len(descs) 
    print("Initial Description model count: %d") % initial_count

    for o in reader_o:
        record = Description(**o)
        record_exists = descs.filter(inspection_key_id=record.inspection_key_id).exists() 
        if record_exists:
            print("record exists")
        elif record.inspection_key_id not in new_descs_list:
            print("adding id to list")
            new_descs_list.append(record.inspection_key_id)

    load_descs(new_descs_list, url)
            
def get_csv(filename):
    # url = BASEURL + make_today() + '/' + filename
    url = BASEURL + "04_01_15" + '/' + filename
    
    csv_resp = urllib2.urlopen(url)
    reader_o = csv.DictReader(csv_resp)
    return get_new_descs_ids(reader_o, url)

def load_csv():
    get_csv('descs_tbl.csv')


if __name__ == '__main__':
    load_csv()
