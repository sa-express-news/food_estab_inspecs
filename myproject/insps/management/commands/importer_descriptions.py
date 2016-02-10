from django.core.management.base import BaseCommand, CommandError
from insps.lib.import_descriptions import load_csv_descriptions

class Command(BaseCommand):
    def handle(self, *args, **options):
        load_csv_descriptions(args[0])