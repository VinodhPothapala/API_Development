import requests
import flask
from configuration.token import sk_token

"""
If the dates are given we are making call to max API and filter the data based on the given range.
If the dates are not given we are making call to YTD API and calculate daily returns.
"""


class IexClient:
    def __init__(self):
        self.token = sk_token

    # Getting stock data using ticker symbol, and type of the API as a parameters.
    # Make an API call to the IEX cloud
    def get_stock_data(self, symbol, mode):
        url = str("https://cloud.iexapis.com/stable/stock/" + symbol + "/chart/" + mode + "?token=" + self.token
                  + "&chartByDay=true")
        try:
            response = requests.get(url)
            return response.json()
        # IF the user provided invalid ticker symbol, it throws an exception.
        except Exception:
            message = f"Invalid Symbol. Please provide a valid stock data."
            payload = {"message": message}
            flask.abort(404, payload)
