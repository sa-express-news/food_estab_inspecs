# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'GeocodedEstab.longitude'
        db.alter_column(u'insps_geocodedestab', 'longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=7))

    def backwards(self, orm):

        # Changing field 'GeocodedEstab.longitude'
        db.alter_column(u'insps_geocodedestab', 'longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=10))

    models = {
        u'insps.geocodedestab': {
            'Meta': {'object_name': 'GeocodedEstab'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'estab_id': ('django.db.models.fields.IntegerField', [], {'max_length': '12', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['insps']