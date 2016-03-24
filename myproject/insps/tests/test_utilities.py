import unittest
import os
from insps.scraper.lib.utilities import write_to_csv, write_to_csv_insps, store_search_page, get_content

class UtilitiesTestCase(unittest.TestCase):
    def test_store_search_page(self):
        PROCESSED_ESTAB_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data/processed')
        self.fail()

