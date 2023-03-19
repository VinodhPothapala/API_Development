import collections
import unittest
from datetime import datetime
from src.service import Service

collections.Callable = collections.abc.Callable


# Tests Method present in the Service class
class ServiceTesting(unittest.TestCase):

    # test case to verify the number of records obtained for the given ticker symbol and date ranges
    def test_get_daily_returns(self):
        from_date = '2023-03-01'
        from_date = datetime.strptime(from_date, '%Y-%m-%d')
        to_date = '2023-03-02'
        to_date = datetime.strptime(to_date, '%Y-%m-%d')
        symbol = 'AAPL'
        actual_stock_returns = Service(symbol).get_daily_returns(from_date, to_date)
        self.assertEqual(len(actual_stock_returns), 2)
