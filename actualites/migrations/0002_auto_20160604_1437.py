# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-04 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='page_images/'),
        ),
        migrations.AddField(
            model_name='article',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='page_images/'),
        ),
        migrations.AddField(
            model_name='article',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='page_images/'),
        ),
    ]
