# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-10 11:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dam_Device_management', '0009_auto_20180810_1137'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Station',
            new_name='Station_data',
        ),
    ]
