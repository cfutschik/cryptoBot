import csv

def check_bull_bear_candle(all_data, offset):
    
    bb_check = 0
    check_score = 0

    for i in range(offset):
        #Bullish Engulfing & above-below candle
        if all_data['close'][-2-i] > all_data['open'][-2-i]:
            bb_check-=1
        elif all_data['close'][-2-i] < all_data['open'][-2-i]:
            bb_check+=1

    if bb_check >= 0:
        check_score = 1
    elif bb_check < 0:
        check_score = 0

    with open('dataFiles/bull_bear_candle_data.csv', 'a', newline='') as f:
        data_writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow([bb_check, check_score])    
                
    return check_score
