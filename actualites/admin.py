#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from actualites.models import Article, Categorie


# Register your models here.

class PageAdmin(admin.ModelAdmin):

    # Configuration de la liste de page
    list_display   = ('date', 'categorie', 'titre', 'slug', 'apercu_contenu',)
    list_filter    = ('titre', 'date', )
    ordering       = ('date', 'categorie', )
    search_fields  = ('titre',)
    prepopulated_fields = {"slug": ("titre",)} # automatic slug

    # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
       ('Général', {
            'fields': ('titre', 'slug', 'categorie', 'date',)
        }),
        # Fieldset 2 : contenu de l'article
        ('Contenu de la page', {
           			'description': 'Contenu de l\'article',
           			'fields': ('contenu',)
				}
        ),
	# Fieldset 3 : images
	('Images de la page', {
				'description' : 'Pour les images, privilégier 800*600',
				'fields' :('image1','image2','image3',)
			     }
	)
    )

    # Colonnes personnalisées 
    def apercu_contenu(self, article):
        """ 
        Retourne les 40 premiers caractères du contenu de l'article. S'il
        y a plus de 40 caractères, il faut rajouter des points de suspension.
        """
        text = article.contenu[0:40]
        if len(article.contenu) > 40:
            return text+'...'
        else:
            return text

    apercu_contenu.short_description = 'Aperçu du contenu'

class CategorieAdmin(admin.ModelAdmin):

    # Configuration de la liste de page
    list_display   = ('nom', 'iconeEncodedImage',)
    list_filter    = ('nom',)
    ordering       = ('nom',)
    search_fields  = ('nom',)

    # Configuration du formulaire d'édition
    fieldsets = (
       			('Général', {
	    'description' : "L'attribut iconeEncodedImage correspond au code html src généré sur le site Icone8",
            'fields': ('nom', 'iconeEncodedImage', )
        	 		    }
			),
		)


admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Article, PageAdmin)
