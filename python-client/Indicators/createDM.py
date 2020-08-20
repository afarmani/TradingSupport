from pandas import DataFrame
import numpy as np


def set_posDM(df: DataFrame):
    df['posDMCalc1'] = currHighPrevHighDiff(df)
    df['posDMCalc2'] = prevLowCurrLowDiff(df)
    df['posDM'] = np.where((df['posDMCalc1'] > df['posDMCalc2']),
                           np.where((df['posDMCalc1'] > 0), df['posDMCalc1'], 0)
                           , 0)
    df = df.drop(columns=['posDMCalc1', 'posDMCalc2'])
    return df


def set_negDM(df: DataFrame):
    df['negDMCalc1'] = prevLowCurrLowDiff(df)
    df['negDMCalc2'] = currHighPrevHighDiff(df)
    df['negDM'] = np.where((df['negDMCalc1'] > df['negDMCalc2']),
                           np.where((df['negDMCalc1'] > 0), df['negDMCalc1'], 0)
                           , 0)
    df = df.drop(columns=['negDMCalc1', 'negDMCalc2'])
    return df


def prevLowCurrLowDiff(df):
    return df['Low'].shift() - df['Low']


def currHighPrevHighDiff(df):
    return df["High"] - df['High'].shift()
