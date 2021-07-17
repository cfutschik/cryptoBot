from CHECK_CANDLESTICK_PATTERN import check_candleStick_pattern

def check_candlestick_trend(all_data):
    #print('flag 3')
    check = 0
    for i in reversed(range(10)):
        candle = check_candleStick_pattern(all_data)
        if candle == 1: 
            check+=1
        elif candle == -1:
            check-=1
        else:
            check+=0

    # Need more than 2 more positives and negative patterns
    if check > 1:
        return 1
    else:
        return 0
