# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 13:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualites', '0012_auto_20160727_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='titre',
            field=models.CharField(max_length=100),
        ),
    ]
