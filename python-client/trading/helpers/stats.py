from pandas import Series


def set_mean(series: Series, window: int):
    return series.rolling(window=window).mean()

