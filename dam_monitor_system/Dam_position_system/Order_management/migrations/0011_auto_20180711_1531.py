# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-11 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order_management', '0010_auto_20180703_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='dam_parameter',
            name='parameter_type',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='dam_parameter',
            name='parameter_data',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
