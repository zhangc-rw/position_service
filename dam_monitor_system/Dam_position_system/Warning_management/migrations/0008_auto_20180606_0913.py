# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-06 01:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Warning_management', '0007_auto_20180606_0906'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wpast',
            old_name='dam_num',
            new_name='dam',
        ),
        migrations.RenameField(
            model_name='wpast',
            old_name='device_num',
            new_name='device',
        ),
        migrations.RenameField(
            model_name='wreal',
            old_name='dam_num',
            new_name='dam',
        ),
        migrations.RenameField(
            model_name='wreal',
            old_name='device_num',
            new_name='device',
        ),
    ]
