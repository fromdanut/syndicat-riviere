# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-06 07:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('actualites', '0003_auto_20160604_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='icone',
            field=models.ImageField(default=datetime.datetime(2016, 6, 6, 7, 8, 37, 293595, tzinfo=utc), upload_to='page_images/'),
            preserve_default=False,
        ),
    ]
