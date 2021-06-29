import numpy
from GET_CLOSE_DATA import get_close_data
from GET_RSI_DATA import get_RSI_data
import talib
import matplotlib.pyplot as plt

import plotly.graph_objects as go
import pandas as pd
from datetime import datetime


#def print_charts(trend_l, trend_s, ATR, buy, sell):
def print_charts(all_data):    
    x = []
    Close = []
    Open = []
    Low = []
    High = []
    Trend_s = []
    Trend_l = []
    ATR = []
    Buy_1 = []
    Buy_2 = []
    Buy_3 = []
    Buy_x = []
    Sell_x = []
    Sell_marker = []
    Stop_loss = []

    #[0]       [1]                    [2]                        [3]  [4]
    #[X-value, [close,open,low,high], [Short trend, long trend], ATR, [buy_1, buy_2, buy_3]]

    y = 0 
    while y < len(all_data):
        x.append(all_data[y][0])
        Close.append(all_data[y][1][0])
        Open.append(all_data[y][1][1])
        Low.append(all_data[y][1][2])
        High.append(all_data[y][1][3])
        Trend_s.append(all_data[y][2][0])
        Trend_l.append(all_data[y][2][1])
        ATR.append(all_data[y][3])
        Buy_1.append(all_data[y][4][0])
        Buy_2.append(all_data[y][4][1])
        Buy_3.append(all_data[y][4][2])
        Buy_x.append(all_data[y][5][0]) 
        Sell_x.append(all_data[y][5][1])
        Sell_marker.append(all_data[y][5][2])
        Stop_loss.append(all_data[y][5][3])
        y+=1
    close_ = numpy.array(Close)
    #print(buy_1)

    RSI = get_RSI_data()
    #print(RSI)
    #print(close_time)

    z = 0
    while z < len(Trend_s):
        #print(trend_s[z])
        if Trend_s[z] == 1:
            Trend_s[z] = 2500
        elif Trend_s[z] == 0:
            Trend_s[z] = 2400
        z+=1

    a = 0
    b = 500
    print(len(x))
    print(len(Sell_x))

    #fig, (ax1, ax2) = plt.subplots(1, 2)
    fig, ax1 = plt.subplots()
    ax1.plot(x[a:b], Close[a:b])
    MA = talib.MA(close_, timeperiod=20, matype=0)
    MA_LONG = talib.MA(close_, timeperiod=50, matype=0)
    ax1.plot(x[a:b], MA[a:b], color='r')
    ax1.plot(x[a:b], MA_LONG[a:b], color='m')
    #ax1.plot(x[a:b],trend_s[a:b])
    #ax1.plot(x[a:b], buy_1[a:b], 'o', color='g',)
    #ax1.plot(x[a:b], buy_2[a:b], 'o', color='r',)
    #ax1.plot(x[a:b], buy_3[a:b], 'o', color='m',)
    ax1.plot(x[a:b], Buy_x[a:b], 'o', color='g',)
    ax1.plot(x[a:b], Sell_x[a:b], 'o', color='m',)
    #ax1.plot(x[(length-len(trend_l)):length],trend_l[-length:])
    #ax2.plot(x[a:b],ATR[a:b])
    
    fig.show()

    #plt.show()



    