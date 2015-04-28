from django.core.management.base import BaseCommand, CommandError
from insps.models import GeocodedEstab
import csv
import os
import time

class Command(BaseCommand):

    def handle(self, *args, **options):

        transforms = {
            ('FREDSBG', 'FREDERICKSBURG'),
            ('BRNFLS','BRAUNFELS'),
            ('PZ', 'PLAZA'),
            ('AV', 'AVE'),
            ('MC CULLOUGH', 'MCCULLOUGH'),
            ('HY', 'HWY'),
            ('GEN MCMULLEN', 'GENERAL MCMULLEN DR'),
            ('PY', 'PKWY'),
            ('MALTSBRG', 'MALTSBERGER'),
            ('SLPHR SPGS', 'SULFUR SPRINGS'),
            ('BV', 'BLVD'),
            ('PKY', 'PARKWAY'),
            ('GEN KRUEGER BV', 'GENERAL KRUEGER BLVD'),
            ('JDTN FY', 'JOURDANTON FWY'),
            ('CI', 'CIR'),
        } 
        estabs_to_geocode = GeocodedEstab.objects.all()
        for estab in estabs_to_geocode:
            print("Estab evaluating for transformation: " + estab.address)
            for transform in transforms:
                estab.address = estab.address.replace(*transform)
                estab.save()
        








        # with open(estabs, "r") as f:
        #     data = list(csv.reader(f))

        # with open(fixed_estabs, "a") as f:
        #     writer = csv.writer(f)
        #     for row in data:
        #         for transform in transforms:
        #             row[2] = row[2].replace(*transform)
        #         writer.writerow(row)



