import csv
import time
import os
from googlegeocoder import GoogleGeocoder

dir = os.path.dirname(__file__) 


geocoder = GoogleGeocoder()

estabs = os.path.join(dir, "processed/7501_end.csv")
geocoded_estabs = os.path.join(dir, "processed/geocoded_estabs.csv") 



with open(estabs, "r") as f:
	data = list(csv.reader(f))

with open(geocoded_estabs, "a") as f:
	writer = csv.writer(f)
	for row in data:
		

		addy = row[2]
		try:
			search = geocoder.get(addy)
			row.append(search[0].geometry.location.lat)
			row.append(search[0].geometry.location.lng)
			print row
			writer.writerow(row)
			time.sleep(.5)
		except:
			print "Couldn't geocode ", row