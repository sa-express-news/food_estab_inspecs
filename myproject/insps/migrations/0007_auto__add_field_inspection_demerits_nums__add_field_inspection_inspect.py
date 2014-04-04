# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Inspection.demerits_nums'
        db.add_column(u'insps_inspection', 'demerits_nums',
                      self.gf('django.db.models.fields.IntegerField')(max_length=5, null=True),
                      keep_default=False)

        # Adding field 'Inspection.inspection_key'
        db.add_column(u'insps_inspection', 'inspection_key',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)

        # Adding field 'Inspection.date'
        db.add_column(u'insps_inspection', 'date',
                      self.gf('django.db.models.fields.DateField')(null=True),
                      keep_default=False)


        # Changing field 'Inspection.demerits'
        db.alter_column(u'insps_inspection', 'demerits', self.gf('django.db.models.fields.CharField')(max_length=255, null=True))

    def backwards(self, orm):
        # Deleting field 'Inspection.demerits_nums'
        db.delete_column(u'insps_inspection', 'demerits_nums')

        # Deleting field 'Inspection.inspection_key'
        db.delete_column(u'insps_inspection', 'inspection_key')

        # Deleting field 'Inspection.date'
        db.delete_column(u'insps_inspection', 'date')


        # Changing field 'Inspection.demerits'
        db.alter_column(u'insps_inspection', 'demerits', self.gf('django.db.models.fields.CharField')(default=0, max_length=255))

    models = {
        u'insps.geocodedestab': {
            'Meta': {'object_name': 'GeocodedEstab'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'estab_id': ('django.db.models.fields.IntegerField', [], {'max_length': '12', 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '7'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'insps.inspection': {
            'Meta': {'object_name': 'Inspection'},
            'date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'demerits': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'demerits_nums': ('django.db.models.fields.IntegerField', [], {'max_length': '5', 'null': 'True'}),
            'estab_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['insps.GeocodedEstab']", 'to_field': "'estab_id'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inspection_key': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        }
    }

    complete_apps = ['insps']