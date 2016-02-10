from django.core.management.base import BaseCommand, CommandError
from insps.lib.import_estabs import load_csv_estabs

class Command(BaseCommand):
    def handle(self, *args, **options):
        load_csv_estabs(args[0])
