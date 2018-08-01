# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-17 06:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0008_auto_20180425_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='associated_carrier',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='carrier_management.Carrier'),
        ),
        migrations.AlterField(
            model_name='devicestatus',
            name='device',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='device_management.Device'),
        ),
    ]
