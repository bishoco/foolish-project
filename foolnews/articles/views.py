from django.shortcuts import render

from .models import Article
from .utils import *
from datetime import datetime

def index(request):
    slug = "10-promise" #move this slug to db config table
    sub_article_count = 3

    article_list = get_articles_from_api()
    main_article = get_main_article (article_list, slug);
    sub_article_list = get_sub_articles(article_list, sub_article_count, main_article.uuid)

    context = {'main_article': main_article, 'sub_article_list': sub_article_list}
    return render(request, 'articles/index.html', context)

def detail(request):
    context = {}
    return render(request, 'articles/detail.html', context)



