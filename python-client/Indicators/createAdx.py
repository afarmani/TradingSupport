from pandas import DataFrame

from Indicators.createDi import set_pos_di, set_neg_di


def set_adx(df: DataFrame, window: int):
    if 'pos_di' not in df.columns:
        df = set_pos_di(df, window)

    if 'neg_di' not in df.columns:
        df = set_neg_di(df, window)

    di_diff = abs(df['pos_di'] - df['neg_di'])
    df_sum = df['pos_di'] + df['neg_di']
    dx = 100 * (di_diff / df_sum)
    df['adx'] = dx.rolling(window=window).mean()

    return df
