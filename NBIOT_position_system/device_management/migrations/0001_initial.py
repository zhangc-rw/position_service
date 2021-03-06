# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-29 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_num', models.CharField(default='xxxxxxx', max_length=80, unique=True)),
                ('device_type', models.CharField(default='', max_length=50)),
                ('storage_time', models.TimeField(default='12:00', max_length=40)),
                ('card_num', models.CharField(default='0000000', max_length=80)),
                ('associated_carrier_num', models.CharField(default='0000000', max_length=80)),
                ('remark', models.TextField(default='无', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='device_management',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_num', models.CharField(default='xxxxxxx', max_length=80)),
                ('online', models.BooleanField(default='off-line', max_length=40)),
                ('last_time', models.TimeField(default='12:00', max_length=30)),
                ('working_status', models.CharField(default='', max_length=60)),
                ('power', models.SmallIntegerField(default='0', max_length=30)),
                ('business_model', models.CharField(default='', max_length=80)),
                ('G_Senser_state', models.CharField(default='off', max_length=80)),
                ('device_state', models.CharField(default='正常', max_length=80)),
            ],
        ),
    ]
