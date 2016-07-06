import os
import glob
import re
from bs4 import BeautifulSoup
from insps.scraper.lib.utilities import get_content

SEARCH_PAGE_CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/search_pages')
ESTAB_PAGE_CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/estabs')
ESTAB_URL = "http://samhd.tx.gegov.com/San%20Antonio/"


def get_estab_pages():
    os.chdir(SEARCH_PAGE_CACHE_DIR)
    estab_pages_list = []
    for file in glob.glob("*.html"):
        soup = BeautifulSoup(open(file, 'r'), "html.parser")
        links = soup.select('table td a')
        hrefs = map(lambda v: v['href'], links)
        pattern = re.compile("^estab.cfm\?licenseID=")
        for href in hrefs:
            if pattern.match(href):
                estab_pages_list.append(href)
    return estab_pages_list


def loop_estab_pages():
    for estab_url_slug in get_estab_pages():
        url = "%s%s" % (ESTAB_URL, estab_url_slug)
        get_content(url, ESTAB_PAGE_CACHE_DIR, estab_url_slug)
