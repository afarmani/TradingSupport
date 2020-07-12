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
        out_str = "%s " % self.symbol
        out_str = out_str + "[open=%s] " % self.open
        out_str = out_str + "[close=%s] " % self.close
        out_str = out_str + "[high=%s] " % self.high
        out_str = out_str + "[low=%s] " % self.low
        out_str = out_str + "[volume=%s] " % self.volume

        return out_str


        # "%d to %d //  %.8f  %.8f  %.8f  %.8f " % (
        # self.start, self.stop, self.open, self.close, self.high, self.low)

        # {
        #     "e": "kline",					# event type
        #     "E": 1499404907056,				# event time
        #     "s": "ETHBTC",					# symbol
        #     "k": {
        #         "t": 1499404860000, 		# start time of this bar
        #         "T": 1499404919999, 		# end time of this bar
        #         "s": "ETHBTC",				# symbol
        #         "i": "1m",					# interval
        #         "f": 77462,					# first trade id
        #         "L": 77465,					# last trade id
        #         "o": "0.10278577",			# open
        #         "c": "0.10278645",			# close
        #         "h": "0.10278712",			# high
        #         "l": "0.10278518",			# low
        #         "v": "17.47929838",			# volume
        #         "n": 4,						# number of trades
        #         "x": false,					# whether this bar is final
        #         "q": "1.79662878",			# quote volume
        #         "V": "2.34879839",			# volume of active buy
        #         "Q": "0.24142166",			# quote volume of active buy
        #         "B": "13279784.01349473"	# can be ignored
        #     }
        # }
