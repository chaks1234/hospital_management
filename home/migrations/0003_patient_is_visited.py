# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-16 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_doctor_patient'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='is_visited',
            field=models.BooleanField(default=False),
        ),
    ]
