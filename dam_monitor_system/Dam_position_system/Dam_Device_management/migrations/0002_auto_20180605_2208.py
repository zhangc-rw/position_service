# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-05 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dam_Device_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='x',
            field=models.FloatField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='y',
            field=models.FloatField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='z',
            field=models.FloatField(max_length=60, null=True),
        ),
    ]