import csv
def check_engulf_entry(all_data):
    
    open_now = all_data['open'][-1]
    open_prev = all_data['open'][-2]
    high_prev = all_data['high'][-2]
    close_now = all_data['close'][-1]
    close_prev = all_data['close'][-2] 
    
    # engulf w/ +38.3 = 1
    # engulf          = 0.75
    # close above     = 0.5
    # engulf w/ -38.3 = 0.5

    entry_quality = 0

    #Bullish Engulfing & above-below candle
    if open_prev > close_prev and close_now > open_now:
        # Checking close above
        if close_now > open_prev:
            entry_quality = 0.5

            if close_now > high_prev:
                entry_quality = 1
                 
    with open('dataFiles/entry_data.csv', 'a', newline='') as f:
        data_writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow([entry_quality])

    return entry_quality

