# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-25 02:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('real_time_monitoring', '0009_auto_20180425_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='device_management.Device'),
        ),
    ]