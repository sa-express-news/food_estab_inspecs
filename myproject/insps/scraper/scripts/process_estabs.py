# -*- coding: utf-8 -*-
import os
import glob
import re
from bs4 import BeautifulSoup
from datetime import datetime 
from insps.scraper.lib.utilities import write_to_csv, write_to_csv_insps

ESTAB_PAGE_CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/estabs')
write_to_csv(["estab_id","name","address"],'estabs_tbl.csv')
write_to_csv(["estab_id_id","date","demerits","demerits_nums","inspection_key"], 'inspections_tbl.csv')
write_to_csv(["estab_id_id","inspection_key_id","viol_text"], 'descs_tbl.csv')

def process_estabs(file):
    estabs = []

    pattern = re.compile("(?<=licenseID=)\d+")
    estab_id = pattern.search(file).group(0)
    estabs.append(estab_id.encode("utf-8"))

    soup = BeautifulSoup(open(file, 'r'), "html.parser")

    print(file)

    if soup.find('b', style='font-size:14px;') is not None:
        name = soup.find('b', style='font-size:14px;').text.encode("utf-8") 

        estabs.append(name)

        init_addy = soup.find('i').text
        clean_addy = init_addy.replace(u"« Back", u"")
        cleaner_addy = re.sub(r'\t|\r|\n', "", clean_addy)
        cleanest_addy = re.sub(r'[\s]{2,}', " ", cleaner_addy)
        addy = re.sub(r'\s(?=,)', '', cleanest_addy)
        estabs.append(addy.encode("utf-8"))

        write_to_csv(estabs, 'estabs_tbl.csv')

        inspections = soup.find_all('div', style='border:1px solid #003399;width:95%;margin-bottom:10px;')
        
        for inspection in inspections:
            inspec = []
            dd_bits = inspection.find('div', style='padding:5px;').text
            cleaner_bits = re.sub(r'\t|\r|\n', '', dd_bits)
            date_str = re.search(r'\d\d\/\d\d\/\d\d\d\d', cleaner_bits).group(0)
            date_object = datetime.strptime(date_str, '%m/%d/%Y')
            date = date_object.strftime('%Y-%m-%d').encode("utf-8")   
            inspec_key_date = re.sub(r'-', '_', date)
            inspection_key = "%s-%s" % (estab_id, inspec_key_date.encode("utf-8") )
            demerits = re.search(r'Demerits\s\d+', cleaner_bits).group(0).encode("utf-8") 
            demerits_nums = re.search(r'\d+', demerits).group(0).encode("utf-8") 
            
            inspec.append(estab_id)
            inspec.append(date)
            inspec.append(demerits)
            inspec.append(demerits_nums)
            inspec.append(inspection_key)

            write_to_csv(inspec, 'inspections_tbl.csv')

            descriptions = inspection.find_all('div', style='background-color:#EFEFEF;padding:5px;')
            for description in descriptions:
                descs = []
                desc_text = ''
                viol_text = ''
                desc_text = re.sub(r'"|\'|\n|\r|\t', '', description.text.encode('utf-8'))
                if desc_text == '':
                    viol_text = 'No Descriptions'
                else:
                    viol_text = desc_text

                descs.append(estab_id)
                descs.append(inspection_key)
                descs.append(viol_text)

                write_to_csv(descs, 'descs_tbl.csv')
    return 

def iterate_raw_pages():
    os.chdir(ESTAB_PAGE_CACHE_DIR)
    for file in glob.glob("*.html"):
        process_estabs(file)






