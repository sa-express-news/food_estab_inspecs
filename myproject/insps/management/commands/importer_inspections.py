from django.core.management.base import BaseCommand, CommandError
from insps.lib.import_inspections import load_csv_inspections

class Command(BaseCommand):
    def handle(self, *args, **options):
        load_csv_inspections(args[0])