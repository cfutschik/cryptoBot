from os import close
from numpy.lib.function_base import append

# General Functions
from GET_RSI_DATA import get_RSI_data
from GET_CLOSE_DATA import get_close_data
from GET_ATR import get_ATR
from GET_MA import get_MA
from GET_TREND import get_trend
from PRINT_CHARTS import print_charts ###

def check_candleStick_pattern(all_opens, all_highs, all_lows, all_closes):
    candle = [-1,0,0]
    open_now = all_opens[-1]
    open_prev = all_opens[-2]
    high_now = all_highs[-1]
    high_prev = all_highs[-2]
    low_now = all_lows[-1]
    low_prev = all_lows[-2]
    close_now = all_closes[-1]
    close_prev = all_closes[-2] 
    # bull = 1
    # bear = 0

    #Engulfing & above-below candle
    if open_prev < close_now: #Bull
        candle[0] = 1
        if close_now > high_prev: #above Bull
            candle[1] = 2
        else:
            candle[1] = 1

    elif close_now < open_prev: #Bear
        candle[0] = 0
        if close_now < low_prev: #below bear
            candle[1] = 2
        else:
            candle[1] = 1
    
    #38.2 candle
    if close_now > open_now: # Bull 38.2
        candle[0] = 1
        if open_now > float((high_now-low_now)*61.8+low_now):
            candle[1] = 3
    
    elif close_now < open_now: # Bear 38.2
        candle[0] = 0
        if open_now < float((high_now-low_now)*38.2+low_now):
            candle[1] = 3

    return candle

def check_entry(all_opens, all_highs, all_lows, all_closes):

    check = [2,0]

    short_trend, long_trend = get_trend(all_closes)

    candle = check_candleStick_pattern(all_opens, all_highs, all_lows, all_closes)

    # Buy = 1
    # Sell = 0
    # Nothing = 2

    check[1] = candle

    if candle[1] != 0:
        if short_trend == 1 and candle[0] == 1: 
            check[0] = 1
        elif short_trend == 0 and candle[0] == 0:
            check[0] = 0

    return check

if __name__ == "__main__":

### pretend ticker ####
    o,h,l,c = get_close_data() ###
    #print(len(l))
###----------------####

# Trade details
    DATA_PERIOD = 400
    LONG_PERIOD = 200
    SHORT_PERIOD = 20
    RSI_PERIOD = 14
    RSI_OVERBOUGHT = 70
    RSI_OVERSOLD = 30
    TRADE_SYMBOL = 'ETHUSD'
    TRADE_QUANTITY = 0.05
# Empty Arrays
    
    all_opens = []
    all_closes = []
    all_highs = []
    all_lows = []
    SHORT_MA = []
    LONG_MA = []
# Initializers
    iteration = 0

### Pretend Ticker ####
    trend_s = []   ####
    trend_l = []    ###
    atr = []        ###
    x = 0           ###
    buy = []        ###
    sell = []       ###
    all_data = []   ###
    while x < 2884: ### 2884
        all_data_subset = []
###----------------####

        if len(all_closes) < DATA_PERIOD:
            all_closes.append(c[x])
            all_highs.append(h[x])
            all_lows.append(l[x])
            all_opens.append(o[x])
  
        if len(all_closes) == DATA_PERIOD:
            # Adding new ticker point
            all_closes.pop(0)
            all_highs.pop(0)
            all_lows.pop(0)
            all_opens.pop(0)
            all_closes.append(c[x])
            all_highs.append(h[x])
            all_lows.append(l[x])
            all_opens.append(o[x])

            #Finding trends
            entry = check_entry(all_opens, all_highs, all_lows, all_closes)



### Pretend Ticker ####

            if entry[0] == 1:
                buy.append(all_closes[-1])
            elif entry[0] == 0:
                sell.append(all_closes[-1])
            else:
                buy.append(2400)
                sell.append(2400)
            

            
            ATR = get_ATR(all_closes, all_highs, all_lows, 14)
            short_trend, long_trend = get_trend(all_closes)
            trend_s.append(short_trend)###
            trend_l.append(long_trend)###
            atr.append(ATR)
            #Append all data
            all_data_subset.append(x) #x position
            ohlc_data=[] 
            ohlc_data.append(all_closes[-1]) #closes
            ohlc_data.append(all_opens[-1])
            ohlc_data.append(all_lows[-1])
            ohlc_data.append(all_highs[-1])
            all_data_subset.append(ohlc_data)
            trend_data = []
            trend_data.append(short_trend)
            trend_data.append(long_trend)
            all_data_subset.append(trend_data)
            all_data_subset.append(ATR)
            #buy/sell/stay
            buy_sell_subset = [0,0]
            if entry[0] == 1:
                buy_sell_subset[1] = 1
            elif entry[0] == 0:
                buy_sell_subset[1] = -1
            else:
                buy_sell_subset[1] = 0
            all_data_subset.append(buy_sell_subset)
                    
            all_data.append(all_data_subset)

        
        x +=1 ###
###----------------####

#print(all_closes) ###
#print(len(all_highs)) ###
#print(len(all_lows)) ###


#[X-value [close,open,low,high], [Short trend, long trend], ATR, [buy(1)/sell(-1),stay(0)]]
#[399, [2435.22, 2438.87, 2434.63, 2439.2], [1, 0], 4.293584979499676, [2435.22, 0]]

#print(all_data[0])
#print(all_data[-1])
print_charts(all_data) ###