import unittest

from insps.scraper.scripts.fetch import get_final_page_count

class FetchTestCase(unittest.TestCase):
    def test_get_final_page_count(self):
        self.assertTrue(get_final_page_count())