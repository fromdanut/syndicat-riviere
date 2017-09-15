# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-06 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualites', '0004_article_icone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='icone',
            field=models.ImageField(upload_to='images/logos/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
