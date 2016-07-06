import unittest

from insps.scraper.scripts.get_estab_pages import get_estab_pages


class GetEstabPagesTestCase(unittest.TestCase):
    def test_get_estab_pages(self):
        self.assertTrue(len(get_estab_pages()) > 0)
