import urllib2
import csv
import datetime
import os
import re
from os import environ

DJANGO_SETTINGS_MODULE = environ['DJANGO_SETTINGS_MODULE']
from insps.models import Description

BASEDIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'scraper/data/processed')
BASEURL = 'https://s3.amazonaws.com/inspections-csvs/'

def load_descs(new_descs_list, localpath_or_url):
    if re.search(r'https://s3', localpath_or_url):
        csv_resp = urllib2.urlopen(localpath_or_url)
        reader_o = csv.DictReader(csv_resp)
    else:
        reader_o = csv.DictReader(open(localpath_or_url))
    for o in reader_o:
        record = Description(**o)
        if record.inspection_key_id in new_descs_list:
            #print("saving new descriptions...")
            record.save()
    descs = Description.objects.all()
    final_count = len(descs)
    #print("Final Description model count: %d") % final_count


def get_new_descs_ids(reader_o, url):
    new_descs_list = []   
    descs = Description.objects.all()
    initial_count = len(descs) 
    #print("Initial Description model count: %d") % initial_count
    for o in reader_o:
        record = Description(**o)
        record_exists = descs.filter(inspection_key_id=record.inspection_key_id).exists() 
        if record_exists:
            continue
            #print("record exists")
        elif record.inspection_key_id not in new_descs_list:
            #print("adding id to list")
            new_descs_list.append(record.inspection_key_id)
    load_descs(new_descs_list, url)
            
def get_csv(filename, loadversion):
    if loadversion == 'initial':
        url = BASEURL + "01_00_00" + '/' + filename
        response = urllib2.urlopen(url)
        reader_o = csv.DictReader(response)
        return get_new_descs_ids(reader_o, url)
    elif loadversion == 'update':
        local_path = os.path.join(BASEDIR, filename) 
        reader_o = csv.DictReader(open(local_path))
        return get_new_descs_ids(reader_o, local_path) 

def load_csv_descriptions(loadversion):
    get_csv('descs_tbl.csv', loadversion)
