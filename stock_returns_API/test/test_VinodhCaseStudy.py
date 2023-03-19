import collections
import unittest
import requests


class UnitTesting(unittest.TestCase):
    collections.Callable = collections.abc.Callable
    """Unit testing test cases"""
    returns_url = "http://192.168.0.41:5009/return/AAPL?from_date=2023-03-01&to_date=2023-03-02"
    alpha_url = "http://192.168.0.41:5009/alpha/AAPL/MSFT?from_date=2023-03-01&to_date=2023-03-15"

    # test case to check the status code of returns API
    def test1(self):
        resp = requests.get(self.returns_url)
        self.assertEqual(resp.status_code, 200)

    # test case to check the type of output of returns API
    def test2(self):
        resp = requests.get(self.returns_url)
        resp_type = type(resp.json())
        self.assertEqual(resp_type, list)

    # test case to check the length of output of returns API
    def test3(self):
        resp = requests.get(self.returns_url)
        resp_length = len(resp.json())
        self.assertEqual(resp_length, 2)

    # test case to check encoding format of returns API
    def test4(self):
        resp = requests.get(self.returns_url)
        resp_encode = resp.encoding
        self.assertEqual(resp_encode, 'utf-8')

    # test case to check the status code of returns API
    def test5(self):
        resp = requests.get(self.alpha_url)
        self.assertEqual(resp.status_code, 200)

    # test case to check the type of output of alpha API
    def test6(self):
        resp = requests.get(self.alpha_url)
        resp_type = type(resp.content)
        self.assertEqual(resp_type, bytes)

    # test case to check encoding format of alpha API
    def test7(self):
        resp = requests.get(self.alpha_url)
        resp_encode = resp.encoding
        self.assertEqual(resp_encode, 'utf-8')


if __name__ == '__main__':
    unittest.main()
