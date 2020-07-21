from datetime import datetime

from utils.constants import DateTimeConstants
from utils.helpers.convert import get_datetime, get_time


class KlineTicker:

    def __init__(self, msg):
        ticker = msg['k']
        self.symbol = ticker['s']
        self.start = ticker['t']
        self.stop = ticker['T']
        self.open = ticker['o']
        self.close = ticker['c']
        self.high = ticker['h']
        self.low = ticker['l']
        self.volume = ticker['v']

    def __str__(self):
        out_str = "%s " % datetime.now()
        out_str = out_str + "%s " % get_time(self.start, DateTimeConstants.MS)
        out_str = out_str + "to %s " % get_time(self.stop, DateTimeConstants.MS)
        out_str = out_str + "%s " % self.symbol
        out_str = out_str + "[open=%s] " % self.open
        out_str = out_str + "[close=%s] " % self.close
        # out_str = out_str + "[high=%s] " % self.high
        # out_str = out_str + "[low=%s] " % self.low
        out_str = out_str + "[volume=%s] " % self.volume

        return out_str

    def get_start(self):
        return self.start