from GET_CLOSE_DATA import get_close_data
from GET_RSI_DATA import get_RSI_data
import talib
import matplotlib.pyplot as plt

#def print_charts(trend_l, trend_s, ATR, buy, sell):
def print_charts(all_data):    
    #[0]       [1]                    [2]                        [3]  [4]
    #[X-value, [close,open,low,high], [Short trend, long trend], ATR, [buy(1)/sell(-1)/stay(0)]]

    x = all_data[0]
    close = all_data[1][0]
    open = all_data[1][1]
    low = all_data[1][2]
    high = all_data[1][3]
    trend_s = all_data[2][0]
    trend_l = all_data[2][1]
    ATR = all_data[3]
    buy_sell = all_data[4]
    print(close)

    z = 0
    while z < len(trend_s):
        #print(trend_s[z])
        if trend_s[z] == 1:
            trend_s[z] = 2480
        elif trend_s[z] == 0:
            trend_s[z] = 2400
        z+=1

    fig, ax1 = plt.subplots()
    ax1.plot(x, close)
    MA = talib.MA(close, timeperiod=20, matype=0)
    #MA_LONG = talib.MA(clos, timeperiod=200, matype=0)
    ax1.plot(x, MA, color='r')
    #ax1.plot(x[:length], MA_LONG[-length:] , color='g')
    ax1.plot(x,trend_s)
    #ax1.plot(x, buy[-length:] , color='g', marker='o')
    #ax1.plot(x[(length-len(trend_l)):length],trend_l[-length:])
    #ax2.bar(x[:length],trend_s[-length:])

    plt.show()