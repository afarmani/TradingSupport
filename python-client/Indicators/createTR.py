from pandas import DataFrame
import numpy as np


def set_tr(df: DataFrame):
    # if previous close was nan then current value should be nan
    df['prevCloseIsNan'] = np.isnan(df['Close'].shift())
    df["H-L"] = df["High"] - df["Low"]
    df["H-pC"] = np.where(df['prevCloseIsNan'], np.nan, abs(df['High'] - df['Close'].shift()))
    df["L-pC"] = np.where(df['prevCloseIsNan'], np.nan, abs(df['Low'] - df['Close'].shift()))
    df["TR"] = np.where(df['prevCloseIsNan'], np.nan, df[['H-L', 'H-pC', 'L-pC']].max(axis=1))

    df = df.drop(columns=['H-L', 'H-pC', 'L-pC', 'prevCloseIsNan'])
    return df


def set_atr(df: DataFrame, window: int):
    x = 0
    trValues = []
    atrValues = []
    atr = 0
    for index, row in df.iterrows():
        if x == 0:
            atrValues.append(0)
        if 1 <= x <= window:
            trValues.append(row['TR'])
            if x != window:
                atrValues.append(0)
        if x == window:
            atr = sum(trValues) / 14
            atrValues.append(atr)
        if x > window:
            atr = ((atr - (atr / 14)) + row['TR'])
            atrValues.append(atr)
        x = x + 1

    df['ATR'] = atrValues
    return df
