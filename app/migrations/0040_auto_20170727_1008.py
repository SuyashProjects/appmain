# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 04:38
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_auto_20170727_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appreq',
            name='ID',
            field=models.CharField(default=uuid.UUID('444bd558-c610-429a-b343-a42ba9e4f1ce'), max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
