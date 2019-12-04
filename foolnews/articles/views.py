from datetime import datetime
import random

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.utils.html import strip_tags

from .models import Article, Comment, ContentConfig
from .utils import *

def index(request):
    #pull the main article slug from the ContentConfig table
    #It didn't feel right to hard code "10-promise" so I created a 
    #config table that could be updated in the admin
    slug_config = get_object_or_404(ContentConfig, key="main-article-slug")
    slug = slug_config.value

    #raise a 404 if the article is not found
    if not slug:
        raise Http404("Main article slug not set in admin")

    #number of articles listed at the bottom of the main page
    sub_article_count = 3 

    article_list = get_articles_from_api()
    main_article = get_main_article (article_list, slug);
    
    sub_article_list = get_sub_articles(article_list, sub_article_count, main_article.uuid)

    context = {'main_article': main_article, 'sub_article_list': sub_article_list}
    return render(request, 'articles/index.html', context)

def detail(request, uuid):
    article_list = get_articles_from_api()
    raw_article = get_article_by_uuid(article_list, uuid)
    
    #raise a 404 if the article is not found
    if not raw_article:
        raise Http404("Article not found")

    instruments = raw_article.get("instruments")
    
    article = convert_raw_article_to_article(raw_article)

    stock_list = get_stocks_from_api()
    stock_list = filter_stock_list_by_instruments(stock_list, instruments)

    comment_list = Comment.objects.filter(article_uuid=uuid).order_by('-comment_date')

    read_more_list = get_sub_articles(article_list, 3, '')

    context = {'article': article, "stock_list": stock_list, "comment_list": comment_list, "read_more_list": read_more_list}
    return render(request, 'articles/detail.html', context)

def comment(request, uuid):
    comment = Comment(
        article_uuid = uuid,
        # Added strip tags to prevent people injecting HTML
        comment_text = strip_tags(request.POST['comment_text'])
    )
    comment.save()
    return HttpResponseRedirect(reverse('articles:detail', args=(uuid,)))




