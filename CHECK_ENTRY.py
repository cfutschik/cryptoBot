from GET_MA_GRAD import get_ma_grad
from GET_TREND import get_trend
from CHECK_CANDLESTICK_TREND import check_candlestick_trend
from CHECK_MA_GRAD import check_ma_grad
from CHECK_MA_TREND import check_ma_trend
from CHECK_RSI import check_RSI
from CHECK_ENGULF_ENTRY import check_engulf_entry
from BULL_BEAR_CANDLE import check_bull_bear_candle
from CHECK_MA_POSITION import check_ma_position
from CHECK_VOLUME import check_volume


def check_entry(all_data):

    #6 checks total
    back_span = 7 #number of previous candles looked at
    #check = 0
    if check_engulf_entry(all_data):
    
        if check_bull_bear_candle(all_data, back_span):

            if check_ma_position(all_data['close']):
                
                if check_volume(all_data['volume']):

                    return True

    #check_2 = check_bull_bear_candle(all_data, back_span)


    #if check:

        #   1. Past 10 candle stick patterns
        #check += check_candlestick_trend(all_data, back_span)
        #print('check_candlestick_trend')
            
        #   2. Trend
        #check += check_ma_trend(all_data['close'])
        #print('check_ma_trend')

        #   3. Trend Gradient    
        #check += check_ma_grad(all_data)
        #print('check_ma_grad')

        #   4. RSI 
        #check += check_RSI(all_data['close']) #1
        #print('check_RSI')
        
    #return check