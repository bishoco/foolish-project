from django.test import TestCase

from .templatetags.showstocks import *

# Create your tests here.

class StockApiTests(TestCase):
    def test_get_stocks_from_api(self):
        stock_list = get_stocks_from_api()
        self.assertGreater(len(stock_list), 0)

    def test_filter_stock_list_by_instruments(self):
        instruments = [{"symbol":"NGG"}, {"symbol":"GS"}, {"symbol":"JOBS"}]        
        stock_list = get_stocks_from_api()
        filtered_list = filter_stock_list_by_instruments(stock_list, instruments)
        self.assertEqual(len(filtered_list), 3)

        ##empty_instruments list returns all stocks
        empty_instruments = []
        filtered_list = filter_stock_list_by_instruments(stock_list, empty_instruments)
        self.assertEqual(len(filtered_list), 25)