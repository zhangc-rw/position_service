# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-08-09 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dam_Device_management', '0007_auto_20180608_1632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station_num', models.IntegerField(null=True)),
                ('card_num', models.CharField(max_length=60, null=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dam_Device_management.Device')),
            ],
        ),
    ]