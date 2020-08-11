# Open time,Open,High,Low,Close,Volume,Number Of Trades,Avg Volume
from pandas import Series


def set_historical_klines_variables(index, row: Series):
    close = row['Close']
    high = row['High']
    low = row['Low']
    open = row['Open']
    volume = row['Volume']

    return index, close, high, low, open, volume
