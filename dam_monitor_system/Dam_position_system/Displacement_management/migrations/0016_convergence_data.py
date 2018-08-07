# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-11 15:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dam_Device_management', '0007_auto_20180608_1632'),
        ('Displacement_management', '0015_auto_20180705_1341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convergence_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stationID', models.IntegerField(null=True)),
                ('dreal_update_time', models.DateTimeField(auto_now=True, null=True)),
                ('temperature', models.FloatField(null=True)),
                ('voltage', models.FloatField(null=True)),
                ('d', models.FloatField(null=True)),
                ('device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dam_Device_management.Device')),
            ],
        ),
    ]