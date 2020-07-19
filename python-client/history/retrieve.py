from binance.client import Client


class RetrieveHistory:

    def __init__(self, symbol, interval, client):
        self.symbol = symbol
        self.interval = interval
        self.client = client

    def update_time_frame(self, interval):
        self.interval = interval

    def update_symbol(self, symbol):
        self.symbol = symbol

    def get_historical_klines(self, start_str, end_str=None):
        """ default provides 500 points of data, maximum 1000.
        :param start_str: Start date string in UTC format or timestamp in milliseconds
        :type start_str: str|int
        :param end_str: optional - end date string in UTC format or timestamp in milliseconds (default will fetch everything up to now)
        :type end_str: str|int
        """
        # example start_str = "1 day ago UTC"
        # a member of class prefixed with _ is a protected member of the class
        # the writers did not intend for this member to be exposed.
        return self.client.get_historical_klines(self.symbol, self.interval, start_str, end_str)
