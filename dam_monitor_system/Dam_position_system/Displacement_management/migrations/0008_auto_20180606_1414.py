# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-06 06:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Displacement_management', '0007_auto_20180606_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dpast',
            name='dam',
        ),
        migrations.RemoveField(
            model_name='dreal',
            name='dam',
        ),
    ]
