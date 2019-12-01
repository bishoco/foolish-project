import json, sys, random

from .models import Article

def get_articles_from_api():    
    json_data = open('articles/static/content_api.json')   
    content_api = json.load(json_data) # deserialises it
    raw_article_list = content_api.get("results")

    json_data.close()

    return raw_article_list;

# returns first article in the list with the slug
# otherwise the first article in the list is returned
# article converted to Article model
def get_main_article (article_list, slug):    
    for article in article_list:
        if (article_has_slug(article, slug)):
            return convert_raw_article_to_article(article)

    if len(article_list) > 0:   
        return convert_raw_article_to_article(article_list[0]);

#returns random elements from article_list excluding the uuid passed in
def get_sub_articles (article_list, count, main_uuid):
    #remove main article so that it is not repeated
    filtered_list = [x for x in article_list if x.get("uuid") != main_uuid]
    random_list = random.sample(filtered_list, count)
    converted_list = []
    for raw_article in random_list:
        converted_list.append(convert_raw_article_to_article(raw_article))
    return converted_list

#returns true if article.tags contains a slug equal to the slug param
def article_has_slug(article, slug):
    tags=article.get("tags")
    for tag in tags:
        if (tag.get("slug") == slug):
            return True

    return False

#converts the raw article data from the api to a more flattened object
#I did this to decouple the view from the api more cleanly
def convert_raw_article_to_article(raw_article):
    return Article(
        uuid = raw_article.get("uuid"),
        promo = raw_article.get("promo"),
        body = raw_article.get("body"),
        headline = raw_article.get("headline"),
        publish_at = raw_article.get("publish_at"),
        byline = raw_article.get("byline"),
        image_url = raw_article.get("images")[0].get("url")
    ) 