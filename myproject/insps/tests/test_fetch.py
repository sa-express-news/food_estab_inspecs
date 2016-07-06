import unittest
import requests
import os

from mock import MagicMock
from insps.scraper.scripts.fetch import get_final_page_count

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'test_data')


def get_stub(*args, **kwargs):
    r = requests.get.return_value
    with open(os.path.join(TEST_DATA_DIR, 'test_main_search.html'), 'r') as f:
        r.content = f.read()
        return r

requests.get = MagicMock(side_effect=get_stub)


class FetchTestCase(unittest.TestCase):
    def test_get_final_page_count(self):
        self.assertEqual(get_final_page_count(), 797)

    def test_stucture_of_city_page(self):
        self.assertTrue(get_final_page_count())
