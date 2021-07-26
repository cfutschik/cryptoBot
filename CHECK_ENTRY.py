from CHECK_PATTERN_ENTRY import check_pattern_entry
from BULL_BEAR_CANDLE import check_bull_bear_candle
from CHECK_MA_POSITION import check_ma_position
from CHECK_VOLUME import check_volume

def check_entry(all_data):

    #6 checks total
    back_span = 7 #number of previous candles looked at
    #check = 0
    if check_pattern_entry(all_data):
    
        if check_bull_bear_candle(all_data, back_span):

            if check_ma_position(all_data['close']):
                
                if check_volume(all_data['volume']):

                    return True
