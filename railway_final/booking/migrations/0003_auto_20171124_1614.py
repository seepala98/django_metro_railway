# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-11-24 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_ticket_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='phone',
            field=models.IntegerField(default=None),
        ),
    ]
