from django.db import models

class GeocodedEstab(models.Model):
	name = models.CharField(max_length=255)
	estab_id = models.IntegerField(max_length=12, null=True)
	address = models.CharField(max_length=255)
	latitude = models.DecimalField(max_digits=10, decimal_places=7)
	longitude = models.DecimalField(max_digits=10, decimal_places=7)


# class Inspection(models.Model):
# 	estab_id = models.ForeignKey(GeocodedEstab, to_field='estab_id')
# 	demerits = models.CharField(max_length=255)




