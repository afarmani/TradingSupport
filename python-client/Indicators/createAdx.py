from pandas import DataFrame
import numpy as np


from Indicators.createAtr import cal_tr
from Indicators.createEma import ExpMovingAverage
from model.binanceModelSetter import set_historical_klines_variables


def directional_movement(d, o, h, l, c, po, ph, pl, pc):
    moveUp = h - ph
    moveDown = pl - l

    # moveup (mu) = curr high (ch) - previous high (ph)
    # if mu > 0 && mu > md : pos dx move (pdm) = mu else pdm = 0
    # pos dx idx = 100 x ( 14EMA(PDM) / ATR )

    if 0 < moveUp > moveDown:
        pdm = moveUp
    else:
        pdm = 0

    # movedown (md) = prev low (pl) - curr low (cl)
    # if md > 0 && md > mu : neg dx move (ndm) = md else ndm = 0
    # neg dx idx = 100 x ( 14EMA(NDM) / ATR )

    if 0 < moveDown > moveUp:
        ndm = moveDown
    else:
        ndm = 0

    return d, pdm, ndm


def calc_DIs(df: DataFrame, window: int):
    # strength of the trend pdi or ndi
    # adx = 100 x (14EMA(abs(pdi - ndi) / (pdi + ndi)))
    tr_dates = []
    true_ranges = []
    pdms = []
    ndms = []

    pclose = 0
    for index, row in df.iterrows():
        if pclose == 0:  # skip first index
            pindex, pclose, phigh, plow, popen, pvolume = set_historical_klines_variables(index, row)
        else:
            index, close, high, low, open, volume = set_historical_klines_variables(index, row)

            tr_date, true_range = cal_tr(index, close, high, low, open, pclose)
            tr_dates.append(tr_date)
            true_ranges.append(true_range)

            dmDate, pdm, ndm = directional_movement(index, open, high, low, close, popen, phigh, plow, pclose)
            pdms.append(pdm)
            ndms.append(ndm)
            # set previous values
            pindex, pclose, phigh, plow, popen, pvolume = index, close, high, low, open, volume

    expPdm = ExpMovingAverage(pdms, window)
    expNdm = ExpMovingAverage(ndms, window)
    atr = ExpMovingAverage(true_ranges, window)

    x = 0
    pDIs = []
    nDIs = []

    while x < len(atr):
        pdi = 100 * (expPdm[x] / atr[x])
        pDIs.append(pdi)
        ndi = 100 * (expNdm[x] / atr[x])
        nDIs.append(ndi)
        x += 1

    return pDIs, nDIs


def calc_adx(df: DataFrame, window: int):
    pDIs, nDIs = calc_DIs(df, window)

    x = 0
    DXs = []

    while x < len(pDIs):  # everything except first value
        DX = 100 * (abs(pDIs[x] - nDIs[x]) / (pDIs[x] + nDIs[x]))
        DXs.append(DX)
        x += 1

    adx = ExpMovingAverage(DXs, window)

    adx = np.r_[0, adx]
    pDIs = np.r_[0, pDIs]
    nDIs = np.r_[0, nDIs]

    return adx, pDIs, nDIs


class CreateAdx:
    def __init__(self, df, window):
        self.adx, self.pDIs, self.nDIs = calc_adx(df, window)
