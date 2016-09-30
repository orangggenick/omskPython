# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.TextField(max_length=150)),
                ('text', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
                ('date', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'Article',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('surname', models.TextField(max_length=30)),
                ('years', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
                ('text', models.TextField()),
            ],
            options={
                'db_table': 'Person',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('text', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'Place',
            },
        ),
    ]
