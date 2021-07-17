from GET_TREND import get_trend

def check_ma_trend(close_data):

    trend = get_trend(close_data)
    
    if trend[0] == 1 and trend[1] == 1:
        return 1
    elif trend[0] == 1 or trend[1] == 1:
        return 0.5
    else:
        return 0