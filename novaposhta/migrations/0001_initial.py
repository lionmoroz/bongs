# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-26 09:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255, verbose_name='Title')),
                ('address', models.CharField(db_index=True, max_length=255, verbose_name='Address')),
            ],
            options={
                'verbose_name': 'Warehouse',
                'verbose_name_plural': 'Warehouses',
            },
        ),
    ]
