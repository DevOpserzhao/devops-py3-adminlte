# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-10-19 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publish',
            name='address',
            field=models.CharField(max_length=100, verbose_name='出版商地址'),
        ),
    ]
