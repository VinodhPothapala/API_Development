# DailyReturns insert required JSON data and its values into the dictionary


class DailyReturns:
    # For calculating returns, date, opening value, closing value and daily returns are required
    def __init__(self, date, opening, closing, daily_return):
        self.date = date
        self.opening = opening
        self.closing = closing
        self.daily_return = daily_return
