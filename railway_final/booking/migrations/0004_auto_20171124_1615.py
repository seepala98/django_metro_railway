# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-11-24 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20171124_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='phone',
            field=models.IntegerField(default=9999999999),
        ),
    ]
