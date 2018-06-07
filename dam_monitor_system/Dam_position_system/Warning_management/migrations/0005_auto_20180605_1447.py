# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-05 06:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Warning_management', '0004_auto_20180604_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wpast',
            name='Logo',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='wpast',
            name='dam_num',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dam_Device_management.Dam'),
        ),
        migrations.AlterField(
            model_name='wpast',
            name='device_num',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dam_Device_management.Device'),
        ),
        migrations.AlterField(
            model_name='wpast',
            name='station',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='wpast',
            name='wreal_type',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='wreal',
            name='Logo',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='wreal',
            name='dam_num',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dam_Device_management.Dam'),
        ),
        migrations.AlterField(
            model_name='wreal',
            name='device_num',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Dam_Device_management.Device'),
        ),
        migrations.AlterField(
            model_name='wreal',
            name='station',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='wreal',
            name='wreal_type',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
