import talib,numpy


def check_RSI(low_data):
    RSI = talib.RSI(numpy.array(low_data), timeperiod=14)
    
    if RSI[-1] < 60:
        return 1
    else:
        return 0
