# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-28 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkings', '0002_checkmodel_int_blank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkmodel',
            name='int_blank',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
