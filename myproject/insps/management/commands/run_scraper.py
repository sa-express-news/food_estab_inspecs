from django.core.management.base import BaseCommand, CommandError
from insps.scraper.scripts.scrape_inspections import initiate_scrape

class Command(BaseCommand):
    def handle(self, *args, **options):
        initiate_scrape()
        