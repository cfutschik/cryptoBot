from re import template
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import numpy as np
import talib

from GET_DATA import get_data
from GET_ATR import get_ATR

def print_analysis(all_data,DATA_PERIOD):

    dataSetInv = get_data()
    o = np.array(dataSetInv['open'])
    h = np.array(dataSetInv['high'])
    l = np.array(dataSetInv['low'])
    c = np.array(dataSetInv['close'])
    ATR = talib.ATR(h, l, c, timeperiod=14)
    MA = talib.MA(c, timeperiod=20, matype=0)
    MA_LONG = talib.MA(c, timeperiod=50, matype=0)
    RSI = talib.RSI(l, timeperiod=14)

    dataSetInv['MA'] = MA
    dataSetInv['MA_LONG'] = MA_LONG
    dataSetInv['RSI'] = RSI

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

    # [0]                        [1]                    [2]                        
    #[[Short trend, long trend], [buy_1, buy_2, buy_3], [buy_close, sell_close, buy_marker, sell_stop]]

    #print(DATA_PERIOD)

    y = 0 
    while y < DATA_PERIOD-1:
        Trend_s.append(np.nan)
        Trend_l.append(np.nan)
        Buy_1.append(np.nan)
        Buy_2.append(np.nan)
        Buy_3.append(np.nan)
        Buy_x.append(np.nan)
        Sell_x.append(np.nan)
        Sell_good.append(np.nan)
        Sell_marker.append(np.nan)
        Stop_loss.append(np.nan)
        y+=1

    y = 0 
    while y < len(all_data):
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
        y+=1

    
    dataSetInv['Buy_x'] = Buy_x
    dataSetInv['Sell_x'] = Sell_x
    dataSetInv['Sell_good'] = Sell_good

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
                    name = "MA_50"),

                    go.Scatter(
                    x=dataSetInv['date'],
                    y=dataSetInv['Buy_x'],
                    line = dict(color="green"),
                    name = "Buy points"),

                    go.Scatter(
                    x=dataSetInv['date'],
                    y=dataSetInv['Sell_x'],
                    line = dict(color="yellow"),
                    name = "Sell loss"),

                    go.Scatter(
                    x=dataSetInv['date'],
                    y=dataSetInv['Sell_good'],
                    line = dict(color="orange"),
                    name = "Sell gain")],
                    
                    rows = [1, 1, 1, 1, 1, 1],
                    cols = [1, 1, 1, 1, 1, 1])

    fig1 = go.Figure(data = go.Scatter(
                    x=dataSetInv['date'],
                    y=dataSetInv['RSI'],
                    line = dict(color="magenta"),
                    name = "RSI"))

    fig.update_layout(xaxis_rangeslider_visible=False, template='plotly_dark')
    fig.show()

    fig1.update_layout(xaxis_rangeslider_visible=False, template='plotly_dark')
    fig1.show()

