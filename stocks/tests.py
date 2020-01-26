from django.test import TestCase

from .templatetags.showstocks import *

# Create your tests here.

class StockApiTests(TestCase):
    def test_get_stocks_from_api(self):
        stock_list = get_stocks_from_api()