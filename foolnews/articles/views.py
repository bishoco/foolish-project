from django.shortcuts import render

from .models import Article
from .utils import get_articles_from_api, get_main_article

def index(request):
    slug = "10-promise" #move this slug to db config table
    article_list = get_articles_from_api()
    main_article = get_main_article (article_list, slug);
    sub_article_list = [main_article, main_article, main_article]
    context = {'main_article': main_article, 'sub_article_list': sub_article_list}
    return render(request, 'articles/index.html', context)

def detail(request):
    context = {}
    return render(request, 'articles/detail.html', context)



