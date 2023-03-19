import collections
import unittest
from src.IexClient import IexClient

collections.Callable = collections.abc.Callable


# Tests Method present in the IexClient class
class IexClientTesting(unittest.TestCase):
    # Test Case to check for return type of the get_stock_data method
    def test_get_stock_data(self):
        symbol = 'MSFT'
        mode = 'max'
        actual_response = IexClient().get_stock_data(symbol, mode)
        self.assertEqual(type(actual_response), list)
