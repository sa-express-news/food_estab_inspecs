import urllib2
import csv
import datetime

BASEURL = 'https://s3.amazonaws.com/inspections-csvs/'

test_today = '08_25_14'

def make_today():
    today = datetime.datetime.now().strftime("%m_%d_%y")
    return today

def get_csv():

    files = [ 'desc_tbl.csv', 'estabs_tbl.csv', 'inspections_tbl.csv' ]

    url = BASEURL + test_today + '/' + 'descs_tbl.csv'

    response = urllib2.urlopen(url)
    csv_file = csv.reader(response)

    for row in csv_file:
        print(row)

if __name__ == '__main__':
    get_csv()
