# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-09 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scans', '0008_auto_20170109_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='port',
            name='status',
            field=models.CharField(max_length=8),
        ),
    ]