# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-11-24 10:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='phone',
            field=models.IntegerField(default=None, max_length=10),
        ),
    ]
