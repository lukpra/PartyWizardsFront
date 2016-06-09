# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 20:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('delete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Ban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('perm', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('delete', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Decoration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('picture', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('recipe', models.CharField(max_length=1000)),
                ('picture', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('kind', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ListDecoration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decoration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizapp.Decoration')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizapp.Drink')),
            ],
        ),
        migrations.CreateModel(
            name='ListIngredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField()),
                ('kindMeasure', models.CharField(max_length=20)),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizapp.Drink')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizapp.Ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='ListTools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizapp.Drink')),
            ],
        ),
        migrations.CreateModel(
            name='myUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_moderator', models.BooleanField()),
                ('date_of_birthday', models.DateField()),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizapp.Drink')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('kind', models.CharField(max_length=250)),
                ('picture', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.AddField(
            model_name='listtools',
            name='tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizapp.Tool'),
        ),
        migrations.AddField(
            model_name='comment',
            name='drink',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizapp.Drink'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='barcode',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizapp.Ingredient'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answer_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wizapp.Comment'),
        ),
    ]
