# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-29 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device_management',
            name='power',
            field=models.FloatField(default='0', max_length=30),
        ),
    ]
