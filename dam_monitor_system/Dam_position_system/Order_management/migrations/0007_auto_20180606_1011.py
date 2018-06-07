# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-06 02:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Order_management', '0006_auto_20180606_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='dam',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Dam_Device_management.Dam'),
        ),
        migrations.AlterField(
            model_name='parameter',
            name='dam',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Dam_Device_management.Dam'),
        ),
    ]
