import pandas as pd


class Indicators:

    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def set_bb(self, window, deviation, datatype):
        # dataType should be open high low close volume etc.
        # window int, deviation int, datatype string
        basis = self.set_ma_key(datatype, window)
        # set MA
        self.set_ma(window, datatype)
        std = str(window) + 'STD' + str(datatype)
        upper = str(window) + 'UpperBand' + str(datatype)
        lower = str(window) + 'LowerBand' + str(datatype)

        self.df[std] = self.df[datatype].rolling(window=window).std()
        self.df[upper] = self.df[basis] + (self.df[std]*deviation)
        self.df[lower] = self.df[basis] - (self.df[std]*deviation)

        return self.df

    def set_ma_key(self, datatype, window):
        return str(window) + 'MA' + str(datatype)

    def set_ma(self, window, datatype):
        basis = self.set_ma_key(datatype, window)
        self.df[basis] = self.df[datatype].rolling(window=window).mean()

