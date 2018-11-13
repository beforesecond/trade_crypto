import talib
import pandas as pd
from Indicators.macd import MACD
from Indicators.stochastic import STOCHASTIC

class Strategy():
    def __init__(self, client, timeframe='5m'):
        self.client = client
        self.timeframe = timeframe          

    def signal(self):
        macdValue = MACD(self.client, self.timeframe).signal()
        stoValue = STOCHASTIC(self.client, self.timeframe).signal()
        
        return stoValue 
          