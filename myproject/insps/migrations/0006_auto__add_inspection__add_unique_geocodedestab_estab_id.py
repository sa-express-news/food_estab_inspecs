# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Inspection'
        db.create_table(u'insps_inspection', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('estab_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['insps.GeocodedEstab'], to_field='estab_id')),
            ('demerits', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'insps', ['Inspection'])

        # Adding unique constraint on 'GeocodedEstab', fields ['estab_id']
        db.create_unique(u'insps_geocodedestab', ['estab_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'GeocodedEstab', fields ['estab_id']
        db.delete_unique(u'insps_geocodedestab', ['estab_id'])

        # Deleting model 'Inspection'
        db.delete_table(u'insps_inspection')


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
            'demerits': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'estab_id': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['insps.GeocodedEstab']", 'to_field': "'estab_id'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['insps']