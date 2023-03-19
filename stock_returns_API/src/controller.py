import datetime
from flask import Flask, request
from flask_cors import CORS
from validator import Validator
from service import Service
from flasgger import Swagger, LazyJSONEncoder, swag_from
from src.configuration.swaggerConfig import SwaggerConfig

app = Flask(__name__)
app.json_encoder = LazyJSONEncoder
cors = CORS(app)

swagger = Swagger(app, template=SwaggerConfig.swagger_template, config=SwaggerConfig.swagger_config)

"""
Implementation of Get Return Method, it accepts three arguments

First argument is ticker symbol (ex: 'AAPL') is mandatory.
Second argument is from_date (YYYY-MM-DD) is optional.
Third argument is to_date (YYYY-MM-DD) is optional.
if second or third arguments are not provided it will consider ytd
"""


@swag_from("configuration/returns.yml")
@app.route('/return/<string:symbol>/', methods=['GET'])
def stock_return(symbol):
    # Obtain from_date and to_Date from the given arguments if no dates are given it will consider none value
    from_date = request.args.get('from_date')
    to_date = request.args.get('to_date')
    # Validate the given dates by checking the date format and date range
    if Validator().validate_date_range(from_date, to_date):
        from_date = datetime.datetime.strptime(from_date, "%Y-%m-%d")
        to_date = datetime.datetime.strptime(to_date, "%Y-%m-%d")

    # Making a service call to get the daily return using IEX cloud API
    filtered_stock_data = Service(symbol).get_daily_returns(from_date, to_date)
    return filtered_stock_data


"""
Implementation of Get Alpha Method, it accepts four arguments.

First argument is ticker symbol (ex: 'AAPL').
Second argument is benchmark (ex: 'MSFT').
Third argument is from_date (YYYY-MM-DD) is optional.
Fourth argument is to_date (YYYY-MM-DD) is optional.
Here, first two arguments are mandatory for comparison to calculate alpha
if third or fourth arguments are not provided it will consider ytd
"""


@swag_from("configuration/alpha.yml")
@app.route('/alpha/<string:symbol>/<string:benchmark>/', methods=['GET'])
def stock_alpha(symbol, benchmark):
    # Obtain the data of ticker and benchmarks stocks data inbetween given date ranges
    ticker_stock_data = stock_return(symbol)
    benchmark_stock_data = stock_return(benchmark)

    """
    Here is the logic for calculating alpha:
    Initially obtaining initial_price of the stock and final_price of the stock in provided date ranges.
    similarly obtain the same data for benchmark as well.
    calculate the returns for both ticker and benchmark by using the formula
    returns : (final_price - initial_price)/ initial_price
    Finally, the alpha is subtracting the tickers returns minus benchmark returns
    """
    ticker_initial_price = ticker_stock_data[0]["opening"]
    ticker_final_price = ticker_stock_data[-1]["closing"]

    benchmark_initial_price = benchmark_stock_data[0]["opening"]
    benchmark_final_price = benchmark_stock_data[-1]["closing"]
    try:
        ticker_pct_returns = 100 * (ticker_final_price - ticker_initial_price) / ticker_initial_price
        benchmark_pct_returns = 100 * (benchmark_final_price - benchmark_initial_price) / benchmark_initial_price
        alpha = round(ticker_pct_returns - benchmark_pct_returns, 4)

    # Exception handling for worst case scenario since we are performing division operation.
    # Worst case scenario: Dividing by zero
    except ZeroDivisionError:
        alpha = "one of the stocks initial price is zero and hence cannot calculate alpha."
    return {"alpha": alpha}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5009)
