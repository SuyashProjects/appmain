# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-26 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_appreq_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appreq',
            name='ID',
            field=models.CharField(default=uuid.UUID('e087a7d4-3399-4ef1-b898-cff9bb67068a'), max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
