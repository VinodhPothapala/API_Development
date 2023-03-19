from datetime import datetime
from Exceptions import LargeDateError
import flask


# Validator is used for validating the given dates
class Validator:
    """
    These methods perform following validation of given dates
    If both from_date and to_date are none, it will consider YTD.
    Check for the given date format
    Check for the "too large" case, if the given dates are in the future, it will provide an exception
    check for the initial date and end date ranges and validate them
    """

    def validate_date_range(self, from_date, to_date):

        if from_date is None and to_date is None:
            return False
        elif from_date is None or to_date is None:
            return False

        self.validate(from_date)
        self.validate(to_date)

        if from_date <= to_date:
            return True
        else:
            message = f"From date {from_date} should be less than To date {to_date}."
            payload = {"message": message}
            flask.abort(409, payload)

    @staticmethod
    def validate(date):
        today = datetime.today()
        # convert the given date to the date object
        try:
            date = datetime.strptime(date, '%Y-%m-%d')
            if date > today:
                raise LargeDateError
        # raising valueError and custom Exceptions( LargeDateError) wherever necessary
        except LargeDateError:
            message = f"{date} is too large. Please use correct date till today's date"
            payload = {"message": message}
            flask.abort(409, payload)

        except ValueError:
            message = f"invalid {date} format. Please use 'YYYY-MM-DD' format"
            payload = {"message": message}
            flask.abort(409, payload)
