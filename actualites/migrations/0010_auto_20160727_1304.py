# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 13:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualites', '0009_auto_20160727_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]
