import requests
import os
from bs4 import BeautifulSoup
from insps.scraper.lib.utilities import store_search_page, get_content

SEARCH_PAGE_COUNT = 0
SEARCH_PAGE_CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/search_pages')
SEARCH_URL = 'http://samhd.tx.gegov.com/San%20Antonio/search.cfm?start='

def get_final_page_count():
    url = 'http://samhd.tx.gegov.com/San%20Antonio/search.cfm'
    r = requests.get(url)
    content = r.content
    soup = BeautifulSoup(content, "html.parser")
    anchors = soup.findAll("a", { "class" : "buttN" })
    search_page_count = int(anchors[-1].text)
    return search_page_count

def fetch_pages():
    counter = 1
    start_number = 1

    SEARCH_PAGE_COUNT = get_final_page_count()


    print(SEARCH_PAGE_COUNT)

    while (counter <= SEARCH_PAGE_COUNT):

        print("On search page: %d.") % (counter)
        url = "%s%d" % (SEARCH_URL, start_number)
        get_content(url, SEARCH_PAGE_CACHE_DIR, start_number)
        counter += 1
        start_number += 10

    return





