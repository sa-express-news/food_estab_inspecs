# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('viol_text', models.TextField(null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeocodedEstab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('estab_id', models.IntegerField(max_length=12, unique=True, null=True)),
                ('address', models.CharField(max_length=255)),
                ('latitude', models.DecimalField(null=True, max_digits=10, decimal_places=7, blank=True)),
                ('longitude', models.DecimalField(null=True, max_digits=10, decimal_places=7, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Inspection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('demerits', models.CharField(max_length=255, null=True)),
                ('demerits_nums', models.IntegerField(max_length=5, null=True)),
                ('inspection_key', models.CharField(max_length=255, unique=True, null=True)),
                ('date', models.DateField(null=True)),
                ('estab_id', models.ForeignKey(to='insps.GeocodedEstab', to_field=b'estab_id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='description',
            name='estab_id',
            field=models.ForeignKey(to='insps.GeocodedEstab', to_field=b'estab_id'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='description',
            name='inspection_key',
            field=models.ForeignKey(to='insps.Inspection', to_field=b'inspection_key'),
            preserve_default=True,
        ),
    ]
