import json
from django.shortcuts import render

from django import template

register = template.Library()

# Create your views here.
@register.inclusion_tag('stocks/stocks.html')
def show_stocks(instruments):
    stock_list = get_stocks_from_api()
    return { 'stock_list' : filter_stock_list_by_instruments(stock_list, instruments) }

def get_stocks_from_api():    
    json_data = open('data/quotes_api.json', encoding='utf-8')   
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