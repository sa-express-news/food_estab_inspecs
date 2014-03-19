# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'GeocodedEstab'
        db.create_table(u'insps_geocodedestab', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=14, decimal_places=10)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=14, decimal_places=10)),
        ))
        db.send_create_signal(u'insps', ['GeocodedEstab'])


    def backwards(self, orm):
        # Deleting model 'GeocodedEstab'
        db.delete_table(u'insps_geocodedestab')


    models = {
        u'insps.geocodedestab': {
            'Meta': {'object_name': 'GeocodedEstab'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '10'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '14', 'decimal_places': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['insps']