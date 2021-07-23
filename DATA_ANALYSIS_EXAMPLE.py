import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import talib

from GET_ALL_DATA import get_all_data


dataSetInv = get_all_data()

o = np.array(dataSetInv['open'])
h = np.array(dataSetInv['high'])
l = np.array(dataSetInv['low'])
c = np.array(dataSetInv['close'])
ATR = talib.ATR(h, l, c, timeperiod=14)
MA = talib.MA(c, timeperiod=20, matype=0)
MA_LONG = talib.MA(c, timeperiod=50, matype=0)
MA_LONG_LONG = talib.MA(c, timeperiod=100, matype=0)
RSI = talib.RSI(c, timeperiod=14)

dataSetInv['MA'] = MA
dataSetInv['MA_LONG'] = MA_LONG
dataSetInv['MA_LONG_LONG'] = MA_LONG_LONG
dataSetInv['RSI'] = RSI
dataSetInv['ATR'] = ATR



fig = make_subplots(col=2)

fig.add_traces([go.Candlestick(x=dataSetInv['date'], 
                open=dataSetInv['open'],
                high=dataSetInv['high'],
                low=dataSetInv['low'],
                close=dataSetInv['close']), 
                
                go.Scatter(
                x=dataSetInv['date'],
                y=dataSetInv['MA'],
                line = dict(color="red"),
                name = "MA_20"),
                
                go.Scatter(
                x=dataSetInv['date'],
                y=dataSetInv['RSI'],
                line = dict(color="cyan"),
                name = "RSI"),

                go.Scatter(
                x=dataSetInv['date'],
                y=dataSetInv['MA_LONG'],
                line = dict(color="cyan"),
                name = "MA_50")],

                rows = [1, 1, 1, 1],
                cols = [1, 1, 2, 1])

fig.update_layout(xaxis_rangeslider_visible=False, template='plotly_dark')
fig.show()


