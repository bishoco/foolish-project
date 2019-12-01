import json, sys

def get_articles_from_api():    
    json_data = open('articles/static/content_api.json')   
    content_api = json.load(json_data) # deserialises it
    raw_article_list = content_api.get("results")

    json_data.close()

    return raw_article_list;

def get_main_article (article_list, slug):
    return next(a for a in article_list if article_has_slug(a, slug))
    #handle case where there is no main article

def article_has_slug(article, slug):
    tags=article.get("tags")
    for tag in tags:
        if (tag.get("slug") == slug):
            return True

    return False