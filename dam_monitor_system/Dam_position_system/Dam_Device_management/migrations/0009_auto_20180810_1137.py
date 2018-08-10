# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-10 11:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dam_Device_management', '0008_station'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='station',
            name='card_num',
        ),
        migrations.AddField(
            model_name='station',
            name='d1',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='d2',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='d3',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='d4',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='dreal_update_time',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='stationID',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='temperature',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='station',
            name='voltage',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='station',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dam_Device_management.Device'),
        ),
        migrations.AlterField(
            model_name='station',
            name='station_num',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
