from binance.client import Client
import pandas as pd

from utils.constants import DateTimeConstants
from utils.helpers.convert import get_datetime


class RetrieveHistory:

    def __init__(self, symbol, interval, client):
        self.symbol = symbol
        self.interval = interval
        self.client = client
        self.data = None

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
        self.data = self.client.get_historical_klines(self.symbol, self.interval, start_str, end_str)
        return self.data

    def set_panda_dataFrame(self, data):
        self.df = pd.DataFrame(data)
        self.setColumnsIndexAndDataTypes()

        return self.df

    def setColumnsIndexAndDataTypes(self):
        self.df.columns = ['Open Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Close Time', 'Quote Asset Volume',
                           'Number Of Trades', 'Taker buy base asset volume', 'Taker buy quote asset volume', 'ignore']
        rowDateIndex = self.df['Open Time'].apply(lambda x: get_datetime(x, DateTimeConstants.MS))
        self.df.index = rowDateIndex
        self.df = self.df.drop(columns=['Open Time', 'Close Time', 'Quote Asset Volume', 'Taker buy base asset volume',
                                        'Taker buy quote asset volume', 'ignore'])
        self.df['Open'] = self.df['Open'].astype(float)
        self.df['High'] = self.df['High'].astype(float)
        self.df['Low'] = self.df['Low'].astype(float)
        self.df['Close'] = self.df['Close'].astype(float)
        self.df['Volume'] = self.df['Volume'].astype(float)
        self.df['Number Of Trades'] = self.df['Number Of Trades'].astype(int)
