from GET_MA_GRAD import get_ma_grad
from GET_TREND import get_trend
from CHECK_CANDLESTICK_TREND import check_candlestick_trend
from CHECK_MA_GRAD import check_ma_grad
from CHECK_MA_TREND import check_ma_trend
from CHECK_RSI import check_RSI


def check_entry(all_data):

    #print('flag 2')
    # 4 checks total
    check = 0

    #   1. Past 10 candle stick patterns
    check += check_candlestick_trend(all_data)
    #print('check_candlestick_trend')
        
    #   2. Trend
    check += check_ma_trend(all_data['close'])
    #print('check_ma_trend')

    #   3. Trend Gradient    
    check += check_ma_grad(all_data)
    #print('check_ma_grad')

    #   4. RSI 
    check += check_RSI(all_data['close'])
    #print('check_RSI')

    return check