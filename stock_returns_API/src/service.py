import datetime

import flask

from IexClient import IexClient

from dailyReturns import DailyReturns

from Exceptions import NoDataException

YTD = 'ytd'
MAX = 'max'


# Service class basically gets stock data from IexCLIENT and filter the data based on the date ranges
class Service:
    def __init__(self, symbol):
        self.symbol = symbol

    """
    Method accepts from_date and to_date as parameters 
    This Method let IexCLIENT know which call it should make in case of invalid or non dates
    If one stock data is available and another stock data is not available for given two different symbols,
    this will raise an Exception
    """

    def get_daily_returns(self, from_date, to_date):

        mode = YTD if from_date is None or to_date is None else MAX

        stock_data = IexClient().get_stock_data(self.symbol, mode)
        daily_returns = []
        # Iterate through the obtained stock data for data filtering process
        for record in stock_data:
            # TODO: create a Service Exception Wrapper
            date = datetime.datetime.strptime(record["date"], "%Y-%m-%d")
            if mode == YTD or (mode == MAX and from_date <= date <= to_date):
                opening = record["open"]
                closing = record["close"]
                """
                Logic for calculating get returns
                To obtain the daily returns of the each day, subtract closing value with open value of the each stock
                Finally, rounding off the value 
                """
                daily_return = round((closing - opening), 4)
                daily_returns.append(DailyReturns(date=date, opening=opening, closing=closing,
                                                  daily_return=daily_return).__dict__)

        # throws No data found Exception when the stock data is null for given ticker and ranges
        try:
            if daily_returns is None or len(daily_returns) == 0:
                raise NoDataException

        except NoDataException:
            message = f"Stock data for {self.symbol} is unavailable in the specified date range"
            payload = {"message": message}
            flask.abort(422, payload)

        return daily_returns
