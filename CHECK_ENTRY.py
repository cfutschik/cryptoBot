from GET_TREND import get_trend
from CHECK_CANDLESTICK_PATTERN import check_candleStick_pattern

def check_entry(all_opens, all_highs, all_lows, all_closes):

    check = [0,0,0]
    #       
    trend = get_trend(all_closes)

    candle = check_candleStick_pattern(all_opens, all_highs, all_lows, all_closes)
    #candle = [trend,type,0]

    # Buy = 1
    # Sell = 0
    # Nothing = 2

    ## Double Trend Safety
    #trend[short trend, long trend]

    if trend[1] == 1 and trend[0] == 1: #both trends must be uptrending
        if candle[0] == 1:
            check[0] = 1
            check[1] = all_closes[-1]
            check[2] = candle[1]


#          check = [0,0,0] -> [buy(1)/sell(-1)/nothing(0), close (if buy), type of candle stick(1,2,3)]

    return check