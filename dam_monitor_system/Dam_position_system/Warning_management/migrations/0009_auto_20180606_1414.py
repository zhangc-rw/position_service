# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-06 06:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Warning_management', '0008_auto_20180606_0913'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wpast',
            name='dam',
        ),
        migrations.RemoveField(
            model_name='wreal',
            name='dam',
        ),
    ]