# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-17 06:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device_management', '0009_auto_20180717_1423'),
        ('real_time_monitoring', '0010_auto_20180425_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Past_Target',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('message_time', models.DateTimeField()),
                ('working_status', models.CharField(max_length=20)),
                ('base_num', models.CharField(max_length=80)),
                ('cell_num', models.CharField(max_length=80)),
                ('location_time', models.DateTimeField()),
                ('coordinates', models.CharField(max_length=60)),
                ('velocity', models.FloatField(default=0)),
                ('moving_direction', models.FloatField(default=0)),
                ('height', models.FloatField(default=0)),
                ('device', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='device_management.Device')),
            ],
        ),
        migrations.AlterField(
            model_name='target',
            name='coordinates',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='target',
            name='device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='device_management.Device'),
        ),
    ]
