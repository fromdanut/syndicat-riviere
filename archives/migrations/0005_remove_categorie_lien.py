# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-15 06:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0004_auto_20160715_0651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categorie',
            name='lien',
        ),
    ]
