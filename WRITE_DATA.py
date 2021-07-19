import csv
from GET_ATR import get_ATR

def write_data(all_data, PORTFOLIO, tradeWrite):
    
    with open('dataFiles/candle_stick_data.csv', 'a', newline='') as f:
        data_writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_MINIMAL)

        if len(all_data['date']) < 2:
            data_writer.writerow(['date', 'high', 'low', 'open', 'close', '20_MA', '50_MA'])

        data_writer.writerow([all_data['date'][-1],
                            all_data['high'][-1], 
                            all_data['low'][-1],
                            all_data['open'][-1], 
                            all_data['close'][-1],
                            all_data['20_MA'][-1],
                            all_data['50_MA'][-1]])

    if tradeWrite == 1:
        with open('dataFiles/buy_info.csv', 'a', newline='') as f:
            data_writer = csv.writer(f, delimiter=',',quoting=csv.QUOTE_MINIMAL)

            #['date', 'buy_price', 'ATR', 'candle_size', 'stop_loss', 'sell_marker','risk']
            data_writer.writerow([all_data['date'][-1],
                                all_data['close'][-1], 
                                get_ATR(all_data,14), 
                                all_data['high'][-1]-all_data['low'][-1],
                                PORTFOLIO['sell_conditions']['stop_loss'],
                                PORTFOLIO['sell_conditions']['sell_marker'],
                                round((PORTFOLIO['sell_conditions']['sell_marker'] - all_data['close'][-1])/(all_data['close'][-1]-PORTFOLIO['sell_conditions']['stop_loss']),3)])

    if tradeWrite != 0 and tradeWrite != 1:
        with open('dataFiles/sell_info.csv', 'a', newline='') as f:
            data_writer = csv.writer(f, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)

            if tradeWrite == 2:
                change = PORTFOLIO['sell_conditions']['stop_loss']/PORTFOLIO['buy_price']

            if tradeWrite == 3:
                change = PORTFOLIO['sell_conditions']['sell_marker']/PORTFOLIO['buy_price']

            if tradeWrite == 4:
                change = PORTFOLIO['sell_conditions']['trail_stop']['moving_SM']/PORTFOLIO['buy_price']

            # [date, sell_price, gain]
            data_writer.writerow([all_data['date'][-1],
                                all_data['close'][-1], 
                                change
                                ])


        

            



