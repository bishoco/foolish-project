from datetime import datetime
import random

from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.utils.html import strip_tags

from .models import Article, Comment, ContentConfig
from .utils import *

class MainView(TemplateView):
    template_name = "articles/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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

        context['main_article'] = main_article
        context['sub_article_list'] = sub_article_list
        return context

class ArticleDetailView(TemplateView):
    template_name = "articles/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        uuid = kwargs['uuid']
        article_list = get_articles_from_api()
        raw_article = get_article_by_uuid(article_list, uuid)
        
        #raise a 404 if the article is not found
        if not raw_article:
            raise Http404("Article not found")

        #list of instruments used to filter stock list
        instruments = raw_article.get("instruments")
        
        article = convert_raw_article_to_article(raw_article)

        stock_list = get_stocks_from_api()
        stock_list = filter_stock_list_by_instruments(stock_list, instruments)

        comment_list = Comment.objects.filter(article_uuid=uuid).order_by('-comment_date')

        read_more_list = get_sub_articles(article_list, 3, '')

        context['article'] = article
        context['stock_list'] = stock_list
        context['comment_list'] = comment_list
        context['read_more_list'] = read_more_list
        return context

def comment(request, uuid):
    comment = Comment(
        article_uuid = uuid,
        # Added strip tags to prevent people from injecting HTML
        comment_text = strip_tags(request.POST['comment_text'])
    )
    comment.save()
    return HttpResponseRedirect(reverse('articles:detail', args=(uuid,)))

def search(request):
    search_text = request.POST['search_text']
    
    article_list = get_articles_from_api()
    results = search_articles (article_list, search_text)
    context = {'results': results, 'search_text': search_text}

    return render(request, 'articles/search_results.html', context)



