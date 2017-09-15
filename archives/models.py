#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Document(models.Model):

    titre = models.CharField(max_length=100)

    document = models.FileField(upload_to="archives/")

    date = models.DateTimeField(verbose_name="Date de parution")
    
    categorie = models.ForeignKey('Categorie')

    def __unicode__(self):

        return self.titre


class Categorie(models.Model):

    nom = models.CharField(max_length=30)

    def __unicode__(self):

        return self.nom
