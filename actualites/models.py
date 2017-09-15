#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):

    titre = models.CharField(max_length=100)

    slug = models.SlugField(max_length=100, unique=True)

    contenu = models.TextField(null=True)

    date = models.DateTimeField(verbose_name="Date de parution")
    
    categorie = models.ForeignKey('Categorie')

    image1 = models.ImageField(upload_to="actualites/images/", null=True, blank = True)

    image2 = models.ImageField(upload_to="actualites/images/", null=True, blank = True)

    image3 = models.ImageField(upload_to="actualites/images/", null=True, blank = True)
    

    def __unicode__(self):

        """ 
        Cette méthode permettra de reconnaître les dif-
	férents objets dans l'administration
        """

        return self.titre

class Categorie(models.Model):

    nom = models.CharField(max_length=30)

    # encoded images from icone8
    iconeEncodedImage = models.TextField()


    def __unicode__(self):

        return self.nom

