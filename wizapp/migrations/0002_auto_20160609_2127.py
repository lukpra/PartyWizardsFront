# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 21:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wizapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ban',
            name='perm',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_moderator',
            field=models.BooleanField(default=False),
        ),
    ]
