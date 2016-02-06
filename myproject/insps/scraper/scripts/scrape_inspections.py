import shutil;
import os;
from insps.scraper.scripts.fetch import fetch_pages
from insps.scraper.scripts.get_estab_pages import get_estab_pages
from insps.scraper.scripts.process_estabs import iterate_raw_pages

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/')

def initiate_scrape():
    print('initiate scrape')  
    print('clearing out contents of data dir, if necessary...')   
    shutil.rmtree(DATA_DIR)
    print('begin fetching pages')
    fetch_pages()
    get_estab_pages()    
    iterate_raw_pages()