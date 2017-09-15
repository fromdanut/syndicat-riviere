#-*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import template
register = template.Library()

def smart_truncate(texte, nbr):

    """
    truncate title if len > to nbr
    check if the last word is not split (and delete if it is)
    append '...' at the end
    """

    try:
        nbr = int(nbr) # check if nbr is an int
    except ValueError :
        return texte

    if len(texte) <= nbr : # nothing to truncate here
        return texte

    texte = texte[:nbr+1] # len(texte) > nbr --> we take on more character to check if it's a space


    # if the last charactere is not a space, e.g if we need to truncate the last word
    if texte[-1:] != ' ' :
        words = texte.split(' ')[:-1] # truncate the last word
	texte = ' '.join(words)
    else :
        texte = texte[:-1]

    return texte + '...'

register.filter('smart_truncate', smart_truncate)

import unicodedata
def strip_accents(texte):
    """
    strip the accents of the texte, usefull to display the title in capitale
    as there is no capital with accent in my police.
    """
    texte = unicode(texte)
    return u''.join(letter for letter in unicodedata.normalize('NFD', texte)
                  if unicodedata.category(letter) != 'Mn')

register.filter('strip_accents', strip_accents)

