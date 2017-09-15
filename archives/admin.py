#-*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from archives.models import Document, Categorie

# Register your models here.

class DocumentAdmin(admin.ModelAdmin):

    # Configuration de la liste de document
    list_display   = ('date', 'categorie', 'titre',)
    list_filter    = ('titre', 'date', )
    ordering       = ('date', 'categorie', )
    search_fields  = ('titre',)

    # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
       ('Général', {
	    'description' : 'Description du document',
            'fields': ('titre', 'categorie', 'date')
        }),
        # Fieldset 2 : lien vers le fichier
        ('Contenu de la page', {
           			'description': 'Sélection du document',
           			'fields': ('document',)
				}
        ),
    )



admin.site.register(Document, DocumentAdmin)
admin.site.register(Categorie)
