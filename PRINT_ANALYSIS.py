from binance_bot import DATA_PERIOD
from re import template
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import numpy as np
import talib

from GET_ALL_DATA import get_all_data
#from GET_ATR import get_ATR

DATA_PERIOD = 100

dataSetInv = get_all_data()
#adjusting data set for priming period
dataSetInv.drop(dataSetInv.head(DATA_PERIOD).index, inplace=True)
all_data.pop(0)

#print(len(all_data))
#print(len(dataSetInv))
#print(dataSetInv)

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

#iteration variables
Trend_s = []
Trend_l = []
Buy_1 = []
Buy_2 = []
Buy_3 = []
Buy_x = []
Sell_x = []
Sell_good = []
Sell_marker = []
Stop_loss = []
Near_peak = [] # 4hours
Far_peak = [] # 8hours
ma_grad_20 = []
ma_grad_50 = []

# 0,                         1,                      2,                                            3,
#[[Short trend, long trend], [buy_1, buy_2, buy_3], [buy_close, sell_close, buy_marker, sell_stop], [past peak, nearest peak]

#print(all_data[0][3][0]['high'])

y = 0
for i in range(len(dataSetInv)):

        Trend_s.append(all_data[y][0][0])
        Trend_l.append(all_data[y][0][1])
        Buy_1.append(all_data[y][1][0])
        Buy_2.append(all_data[y][1][1])
        Buy_3.append(all_data[y][1][2])
        Buy_x.append(all_data[y][2][0]) 
        Sell_x.append(all_data[y][2][1])
        Sell_good.append(all_data[y][2][2])
        Sell_marker.append(all_data[y][2][3])
        Stop_loss.append(all_data[y][2][4])
        Near_peak.append(all_data[y][3][1]['high'])
        Far_peak.append(all_data[y][3][0]['high'])
        ma_grad_20.append(all_data[y][4][0])
        ma_grad_50.append(all_data[y][4][1])
        y+=1

#print(Near_peak)

#print(len(Near_peak))

dataSetInv['Buy_x'] = Buy_x
dataSetInv['Sell_x'] = Sell_x
dataSetInv['Sell_good'] = Sell_good
dataSetInv['Near_peak'] = Near_peak
dataSetInv['Far_peak'] = Far_peak
dataSetInv['ma_grad_20'] = ma_grad_20
dataSetInv['ma_grad_50'] = ma_grad_50

#print("Length data: "+str(len(o)))
#print("Length ATR: "+str(len(ATR)))
#print("Length MA: "+str(len(MA)))
#print("Length MA_LONG: "+str(len(MA_LONG)))
#print("Length all_data: "+str(len(all_data)))
#print("Length sell_marker: "+str(len(Sell_marker)))
#print(MA)

fig = make_subplots()

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
                y=dataSetInv['MA_LONG'],
                line = dict(color="cyan"),
                name = "MA_50")],

                rows = [1, 1, 1],
                cols = [1, 1, 1])

fig1 = make_subplots(rows=3)
fig1.add_traces([go.Scatter(
                x=dataSetInv['date'],
                y=dataSetInv['RSI'],
                line = dict(color="magenta"),
                name = "RSI"),

                go.Scatter(
                x=dataSetInv['date'],
                y=dataSetInv['ATR'],
                line = dict(color="red"),
                name = "ATR"),
                
                go.Scatter(
                x=dataSetInv['date'],
                y=dataSetInv['ma_grad_20'],
                line = dict(color="red"),
                name = "MA Grad 20"),

                go.Scatter(
                x=dataSetInv['date'],
                y=dataSetInv['ma_grad_50'],
                line = dict(color="blue"),
                name = "MA Grad 50")],
                
                #go.Scatter(
                #x=dataSetInv['date'],
                #y=dataSetInv['ATR'],
                #line = dict(color="red"),
                #name = "ATR")],
                
                rows = [1, 2, 3, 3],
                cols = [1, 1, 1, 1])

fig.update_layout(xaxis_rangeslider_visible=False, template='plotly_dark')
fig.show()

#fig1.update_layout(xaxis_rangeslider_visible=False, template='plotly_dark')
#fig1.show()

