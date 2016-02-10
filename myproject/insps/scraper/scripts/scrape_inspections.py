import shutil;
import os;
from insps.scraper.scripts.fetch import fetch_pages
from insps.scraper.scripts.get_estab_pages import get_estab_pages
from insps.scraper.scripts.process_estabs import iterate_raw_pages
from insps.lib.import_estabs import load_csv_estabs
from insps.lib.import_inspections import load_csv_inspections
from insps.lib.import_descriptions import load_csv_descriptions


DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/')

def initiate_scrape():
    print('initiate scrape')  
    print('clearing out contents of data dir, if necessary...')

    if os.path.isdir(DATA_DIR):
        shutil.rmtree(DATA_DIR)
    
    print('begin fetching pages')
    fetch_pages()
    get_estab_pages()    
    iterate_raw_pages()
    load_csv_estabs('update')
    load_csv_inspections('update')
    load_csv_descriptions('update')