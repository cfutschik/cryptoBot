import talib, numpy

def get_ATR(all_closes,all_highs,all_lows,dataperiod):
    
    np_closes = numpy.array(all_closes)
    np_highs = numpy.array(all_highs)
    np_lows = numpy.array(all_lows)
    ATR = talib.ATR(np_highs, np_lows, np_closes, timeperiod=dataperiod)

    return ATR