import collections
import unittest
from src.validator import Validator

collections.Callable = collections.abc.Callable


# Tests Method present in the Validator class
class ValidatorTesting(unittest.TestCase):

    def test_validate_date_range(self):
        from_date = '2022-03-01'
        to_date = '2023-03-02'
        self.assertEqual(Validator().validate_date_range(from_date, to_date), True)
