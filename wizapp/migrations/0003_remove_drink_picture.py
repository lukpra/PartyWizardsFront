# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-03 14:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wizapp', '0002_auto_20160609_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='picture',
        ),
    ]