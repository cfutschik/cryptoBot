def check_candleStick_pattern(all_opens, all_highs, all_lows, all_closes):
    candle = [0,0,0]
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
    if open_prev > close_prev and close_now > open_now: #Bull
        if close_now > open_prev:
            candle[0] = 1

            if close_now > high_prev: #above Bull
                candle[1] = 'Close above'
            else:
                candle[1] = 'Engulfing'

    #elif close_now < open_prev: #Bear
    #    candle[0] = 0
    #    if close_now < low_prev: #below bear
    #        candle[1] = 2
    #    else:
    #        candle[1] = 1
    
    #38.2 candle Bullish
    if close_now > open_now: # Bull 38.2
        limit = float((high_now-low_now)*0.618+low_now)
        if float(open_now) > limit:
            candle[0] = 1
            candle[1] = '38.2 Candle'

    if close_now < open_now:
        limit = float((high_now-low_now)*0.618+low_now)
        if float(close_now) > limit:
            candle[0] = 1
            candle[1] = '38.2 Candle'
 
    #elif close_now < open_now: # Bear 38.2
    #    candle[0] = 0
    #    if open_now < float((high_now-low_now)*38.2+low_now):
    #        candle[1] = 3

    return candle