import pandas as pd
import talib

from configuration import *

class STOCHASTIC():
    def __init__(self, client, timeframe='5m'):
        self.client = client
        self.timeframe = timeframe

    def signal(self):
        ohlcv_candles = pd.DataFrame(self.client.Trade.Trade_getBucketed(
            binSize=self.timeframe,
            symbol='XBTUSD',
            count=100,
            reverse=True
        ).result()[0])
    
        ohlcv_candles.set_index(['timestamp'], inplace=True)


        slowk, slowd = talib.STOCH(ohlcv_candles.high.values, ohlcv_candles.low.values, ohlcv_candles.close.values, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)

        result = 0
        slowk = slowk[-1]
        slowd = slowd[-1]
        
        # sell
        if slowk < slowd and slowk >= 80 and slowk <= 100 and slowd >= 80 and slowd <= 100:
            return -1
        # buy
        elif slowk > slowd and slowk >= 0 and slowk <= 20 and slowd >= 0 and slowd <= 20:
            return 1
        # do nothing
        else: return 0  