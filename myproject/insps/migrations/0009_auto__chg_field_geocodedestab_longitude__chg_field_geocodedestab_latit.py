# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'GeocodedEstab.longitude'
        db.alter_column(u'insps_geocodedestab', 'longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=7))

        # Changing field 'GeocodedEstab.latitude'
        db.alter_column(u'insps_geocodedestab', 'latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=7))

    def backwards(self, orm):

        # Changing field 'GeocodedEstab.longitude'
        db.alter_column(u'insps_geocodedestab', 'longitude', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=10, decimal_places=7))

        # Changing field 'GeocodedEstab.latitude'
        db.alter_column(u'insps_geocodedestab', 'latitude', self.gf('django.db.models.fields.DecimalField')(default=datetime.datetime(2014, 9, 8, 0, 0), max_digits=10, decimal_places=7))

    models = {
        u'insps.description': {
            'Meta': {'object_name': 'Description'},
            'estab_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['insps.GeocodedEstab']", 'to_field': "'estab_id'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inspection_key': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['insps.Inspection']", 'to_field': "'inspection_key'"}),
            'viol_text': ('django.db.models.fields.TextField', [], {'null': 'True'})
        },
        u'insps.geocodedestab': {
            'Meta': {'object_name': 'GeocodedEstab'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'estab_id': ('django.db.models.fields.IntegerField', [], {'max_length': '12', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '7', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '7', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'insps.inspection': {
            'Meta': {'object_name': 'Inspection'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'demerits': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'demerits_nums': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True'}),
            'estab_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['insps.GeocodedEstab']", 'to_field': "'estab_id'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inspection_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['insps']