from pandas import DataFrame
import numpy as np

from Indicators.createIndicator import curr_high_prev_high_diff, prev_low_curr_low_diff
from Indicators.createTR import set_atr


def set_pos_dm(df: DataFrame):
    df['pos_dm_1'] = curr_high_prev_high_diff(df)
    df['pos_dm_2'] = prev_low_curr_low_diff(df)
    df['pos_dm'] = np.where((df['pos_dm_1'] > df['pos_dm_2']),
                            np.where((df['pos_dm_1'] > 0), df['pos_dm_1'], 0)
                            , 0)
    df = df.drop(columns=['pos_dm_1', 'pos_dm_2'])
    return df


def set_neg_dm(df: DataFrame):
    df['neg_dm_1'] = prev_low_curr_low_diff(df)
    df['neg_dm_2'] = curr_high_prev_high_diff(df)
    df['neg_dm'] = np.where((df['neg_dm_1'] > df['neg_dm_2']),
                            np.where((df['neg_dm_1'] > 0), df['neg_dm_1'], 0)
                            , 0)
    df = df.drop(columns=['neg_dm_1', 'neg_dm_2'])
    return df


def set_avg_pos_dm(df: DataFrame, window: int):
    if 'pos_dm' not in df.columns:
        df = set_pos_dm(df)

    if 'avg_pos_dm' in df.columns:
        print('avg_pos_dm column already exists in passed dataframe.')
        return df

    x = 0
    pos_dm_values = []
    avg_pos_dm_values = []
    atr = 0
    for index, row in df.iterrows():
        if x == 0:
            avg_pos_dm_values.append(0)
        if 1 <= x <= window:
            pos_dm_values.append(row['pos_dm'])
            if x != window:
                avg_pos_dm_values.append(0)
        if x == window:
            atr = sum(pos_dm_values) / 14
            avg_pos_dm_values.append(atr)
        if x > window:
            atr = ((atr - (atr / 14)) + row['pos_dm'])
            avg_pos_dm_values.append(atr)
        x = x + 1

    df['avg_pos_dm'] = avg_pos_dm_values
    df = df.drop(columns=['pos_dm'])
    return df


def set_avg_neg_dm(df: DataFrame, window: int):
    if 'neg_dm' not in df.columns:
        df = set_neg_dm(df)

    if 'avg_neg_dm' in df.columns:
        print('avg_neg_dm column already exists in passed dataframe.')
        return df

    x = 0
    neg_dm_values = []
    avg_neg_dm_values = []
    atr = 0
    for index, row in df.iterrows():
        if x == 0:
            avg_neg_dm_values.append(0)
        if 1 <= x <= window:
            neg_dm_values.append(row['neg_dm'])
            if x != window:
                avg_neg_dm_values.append(0)
        if x == window:
            atr = sum(neg_dm_values) / 14
            avg_neg_dm_values.append(atr)
        if x > window:
            atr = ((atr - (atr / 14)) + row['neg_dm'])
            avg_neg_dm_values.append(atr)
        x = x + 1

    df['avg_neg_dm'] = avg_neg_dm_values
    df = df.drop(columns=['neg_dm'])
    return df


def set_pos_di(df: DataFrame, window: int):
    if 'ATR' not in df.columns:
        df = set_atr(df, window)

    if 'avg_pos_dm' not in df.columns:
        df = set_avg_pos_dm(df, window)

    if 'pos_di' in df.columns:
        print('pos_di column already exists in passed dataframe.')
        return df

    df['pos_di'] = (df['avg_pos_dm'] / df['ATR']) * 100
    df = df.drop(columns=['avg_pos_dm'])
    return df


def set_neg_di(df: DataFrame, window):
    if 'ATR' not in df.columns:
        df = set_atr(df, window)

    if 'avg_neg_dm' not in df.columns:
        df = set_avg_neg_dm(df, window)

    if 'neg_di' in df.columns:
        print('neg_di column already exists in passed dataframe.')
        return df

    df['neg_di'] = (df['avg_neg_dm'] / df['ATR']) * 100
    df = df.drop(columns=['avg_neg_dm'])
    return df
