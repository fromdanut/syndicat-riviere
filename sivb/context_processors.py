#-*- coding: utf-8 -*-
"""
fetch information for block nav, articles in the aside and contact in the footer
"""

from actualites.models import Article
from sivb.settings import NUMBER_OF_MINIARTICLE, ACTUALITE_PAGINATION_BY
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def get_info_block_nav(request):

    """to display menu with flatpages
       DEBUG : name of menu should'nt be there !
       find a better place --> setting ?
       OR BETTER : should be fetch from DB directly"""


    menuTitles = [{'nom':'Les rivières', 'URLslug' : '/rivieres/'},
		  {'nom':'La vallée', 'URLslug' : '/vallee/'},
		  {'nom':'Le syndicat', 'URLslug' : '/syndicat/'},
	          {'nom':'Les actions', 'URLslug' : '/action/'},
		 ]

    return locals()

def get_info_articles(request):
    """
    Set articles here because we need it in every part of the site
    """

    # set the articles
    articles = Article.objects.order_by('-date')

    # DEBUG add a page number into articles (uglay way, find a better option !)

    count=ACTUALITE_PAGINATION_BY
    for article in articles :
        page_num = count/ACTUALITE_PAGINATION_BY # keep the entire part of the division
        article.page=page_num # part that we put into page variable.
        count += 1

    # set the miniArticles for the aside
    miniArticles = articles[:NUMBER_OF_MINIARTICLE]

    return {'miniArticles' : miniArticles,
	    'articles': articles,
           }
