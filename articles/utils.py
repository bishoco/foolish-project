import json, sys, random
from datetime import datetime

from .models import Article

#### Article Utils ####

#Pulls article list from json file
def get_articles_from_api():    
    json_data = open('data/content_api.json', encoding='utf-8')   
    content_api = json.load(json_data) # deserialises it
    raw_article_list = content_api.get("results")

    json_data.close()

    return raw_article_list;

#returns the article that has the uuid passed in
def get_article_by_uuid(article_list, uuid):
    for article in article_list:
        if (article.get("uuid") == uuid):
            return article

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
#articles converted to Article models
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
#I did this to decouple the view from the api
def convert_raw_article_to_article(raw_article):
    return Article(
        uuid = raw_article.get("uuid"),
        promo = raw_article.get("promo"),
        #removing the extraneous {%sfr%} tag
        body = raw_article.get("body").replace("{%sfr%}",""),
        headline = raw_article.get("headline"),
        #converting string in iso date format to datetime
        #had to convert Z to +00:00 to use the fromisoformat function
        publish_at = datetime.fromisoformat(raw_article.get("publish_at").replace("Z", "+00:00")),
        byline = raw_article.get("byline"),
        image_url = raw_article.get("images")[0].get("url"),
        instruments = raw_article.get("instruments")
    )

#### Search Utils ####

#filters article list by the search text
#This is a rather crude search. Using some kind of search library
#or implementing a robust search method would make sense
#in the long term.
def search_articles (article_list, search_text):
    filtered_article_list = []
    for raw_article in article_list:
        if (search_text.upper() in raw_article.get("headline").upper() or search_text.upper() in raw_article.get("body").upper()):
            filtered_article_list.append(convert_raw_article_to_article(raw_article))
    return filtered_article_list;