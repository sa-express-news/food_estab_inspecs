from insps.models import GeocodedEstab
import csv
import os
import time


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
    ('EEEEEEEEEEEEEEEE', 'E'), 
    ('COMMERCIRRRRRRRRRRRRRRRRRRRAL', 'Commercial'),
    ('AVEEEE', 'AVE'), 
    ('AVEEEEEEEEEEEEEE', 'AVE'),
    ('AVEEEEEEEEEEEEE', 'AVE'), 
    ('ENCIRRRRRRRRRRRRRRRRRRRRNO', 'ENCINO'),
    ('AVEEEE', 'AVE'),
    ('CHAVEEEEEANEAUX', 'CHAVEANEAUX')
}

def addies_transforms(): 
    estabs = GeocodedEstab.objects.all()
    for estab in estabs:
        #print("Estab evaluating for transformation: " + estab.address)
        for transform in transforms:
            estab.address = estab.address.replace(*transform)
            estab.save()

