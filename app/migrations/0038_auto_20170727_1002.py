# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 04:32
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_auto_20170727_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appreq',
            name='ID',
            field=models.CharField(default=uuid.UUID('9633392e-7284-11e7-866d-448500c2e63c'), max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
