from django.db import models

class GeocodedEstab(models.Model):
	name = models.CharField(max_length=255)
	estab_id = models.IntegerField(max_length=12, null=True, unique=True)
	address = models.CharField(max_length=255)
	latitude = models.DecimalField(max_digits=10, decimal_places=7)
	longitude = models.DecimalField(max_digits=10, decimal_places=7)

	def __unicode_(self):
		return self.name, self.address


class Inspection(models.Model):
	estab_id = models.ForeignKey(GeocodedEstab, to_field='estab_id')
	demerits = models.CharField(max_length=255, null=True)
	demerits_nums = models.IntegerField(max_length=5, null=True)
	inspection_key = models.CharField(max_length=255, null=True, unique=True)
	date = models.DateField(auto_now=False, auto_now_add=False, null=True)

class Description(models.Model):
	estab_id = models.ForeignKey(GeocodedEstab, to_field='estab_id')
	inspection_key = models.ForeignKey(Inspection, to_field='inspection_key')
	viol_text = models.TextField(null=True)




