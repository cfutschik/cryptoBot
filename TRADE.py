from binance.client import Client
import config
from binance.enums import ORDER_TYPE_MARKET, SIDE_BUY, SIDE_SELL
from binance.client import Client
import config
from GET_ATR import get_ATR


def execute_buy(PORTFOLIO, all_data, TEST):

    client = Client(config.API_KEY, config.API_SECRET)    
    print('Sending order - Buy')
    try:
        if TEST == True:
            ATR = get_ATR(all_data, 14)
            PORTFOLIO['Position'] = True
            PORTFOLIO['buy_price'] = all_data['close'][-1]
            PORTFOLIO['sell_conditions']['stop_loss'] = all_data['low'][-1]-ATR
            PORTFOLIO['sell_conditions']['sell_marker'] = all_data['close'][-1]+2*ATR

        if TEST == False:
            order = client.create_order(symbol = PORTFOLIO['Stock'], 
                                                side = SIDE_BUY, 
                                                type = ORDER_TYPE_MARKET, 
                                                # Convert BUSD to ETH then request a buy
                                                quantity = round(PORTFOLIO['TRD_QTY'],4))
                                                #quantity = float(round((PORTFOLIO['Balance_2']/all_data['close'][-1])*.9,5))) 
            print(order)
        ATR = get_ATR(all_data, 14)
        PORTFOLIO['Position'] = True
        PORTFOLIO['buy_price'] = all_data['close'][-1]
        PORTFOLIO['sell_conditions']['stop_loss'] = all_data['low'][-1]-ATR
        PORTFOLIO['sell_conditions']['sell_marker'] = all_data['close'][-1]+2*ATR
        #tradewrite = 1    

    except Exception as e:
        print("An exception has occured - {}".format(e))
        #PORTFOLIO['Position'] = False
        #tradewrite = 0
        return False


    return True

def execute_sell(PORTFOLIO, TEST):
    client = Client(config.API_KEY, config.API_SECRET)
    print('Sending order - Sell')
    try:     
        if TEST == True:
            PORTFOLIO['Position'] = False
            #PORTFOLIO['sell_conditions']['trail_stop']['moving_SM'] = 0.0
            PORTFOLIO['sell_conditions']['trail_stop']['above_marker'] = False

        if TEST == False:  
            order = client.create_order(symbol = PORTFOLIO['Stock'], 
                                                side = SIDE_SELL, 
                                                type = ORDER_TYPE_MARKET, 
                                                quantity = round(PORTFOLIO['TRD_QTY'],4))
                                                #quantity = float(round(PORTFOLIO['Balance_1']*.9,5))) #ETH
            print(order)
        PORTFOLIO['Position'] = False
        #PORTFOLIO['sell_conditions']['trail_stop']['moving_SM'] = 0.0
        PORTFOLIO['sell_conditions']['trail_stop']['above_marker'] = False
        

    except Exception as e:
        print("An exception has occured - {}".format(e))
        #PORTFOLIO['Position'] = True
        return False

    return True