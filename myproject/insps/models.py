from django.db import models

class GeocodedEstab(models.Model):
	name = models.CharField(max_length=255)
	address = models.CharField(max_length=255)
	latitude = models.DecimalField(max_digits=14, decimal_places=10)
	longitude = models.DecimalField(max_digits=14, decimal_places=10)

