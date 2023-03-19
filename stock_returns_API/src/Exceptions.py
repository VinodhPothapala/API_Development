import flask


# Custom Exception Handling class

class LargeDateError(ValueError):
    pass


# class EnterCorrectDates(ValueError):
#     message = f"Provide valid dates in YYYY-MM-DD format to check the stock data"
#     payload = {"message": message}
#     flask.abort(500, payload)


class NoDataException(ValueError):
    pass
