import json, sys, random
from datetime import datetime

from .models import Article

## Article Utils ##
def get_articles_from_api():    
    json_data = open('articles/static/content_api.json', encoding='utf-8')   
    content_api = json.load(json_data) # deserialises it
    raw_article_list = content_api.get("results")

    json_data.close()

    return raw_article_list;

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

## Stock Utils ##
def get_stocks_from_api():    
    json_data = open('articles/static/quotes_api.json', encoding='utf-8')   
    raw_stock_list = json.load(json_data) # deserialises it
    json_data.close()

    return raw_stock_list;

#filters a list of stocks based on the list of instruments passed in
#this compares instrument.symbol to stock.Symbol
#there is probably a more elegant way to do this in python, but this is good enough for now
def filter_stock_list_by_instruments(stock_list, instruments):
    filtered_stock_list = []
    for instrument in instruments:
        for stock in stock_list:
            if (instrument.get("symbol") == stock.get("Symbol")):
                filtered_stock_list.append(stock)
                break
    
    return filtered_stock_list;
