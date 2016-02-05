# -*- coding: utf-8 -*-
import os
import requests
import time
import csv

PROCESSED_ESTAB_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/processed')

def store_search_page(content, local_path, dir_path):
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    with open(local_path, 'wb') as f:
        print("Storing %s") % (local_path)
        f.write(content)

def get_content(url, dir_path, filename):
    filename = str(filename) + '.html'
    local_path = os.path.join(dir_path, filename)
    if not os.path.isfile(local_path):
        r = requests.get(url)
        time.sleep(1)
        content = r.content
        store_search_page(content, local_path, dir_path)
    else:
        print "File exists."

def write_to_csv(arr, table_name):
    if not os.path.isdir(PROCESSED_ESTAB_DIR):
        os.makedirs(PROCESSED_ESTAB_DIR)

    local_path = os.path.join(PROCESSED_ESTAB_DIR, table_name)
    with open(local_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(arr)

def write_to_csv_insps(arr, table_name):
    if not os.path.isdir(PROCESSED_ESTAB_DIR):
        os.makedirs(PROCESSED_ESTAB_DIR)

    local_path = os.path.join(PROCESSED_ESTAB_DIR, table_name)
    with open(local_path, 'a') as f:
        writer = csv.writer(f)
        writer.writerows(arr)





