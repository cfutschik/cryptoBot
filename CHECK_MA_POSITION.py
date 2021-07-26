from GET_MA import get_MA

def check_ma_position(all_closes):

    SHORT_MA, LONG_MA = get_MA(all_closes)

    if SHORT_MA[-1] >= LONG_MA[-1]:
        return True
    #elif all_closes[-1] > SHORT_MA[-1]: 
        #return True
    else:
        return False