from GET_DATA import get_data
from binance.enums import ORDER_TYPE_MARKET, SIDE_BUY, SIDE_SELL
from binance.client import Client
import config

from GET_ATR import get_ATR
from CHECK_ENTRY import check_entry
from WRITE_DATA import write_data
from WRITE_PORTFOLIO import write_portfolios



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
                                                quantity = 0.04)
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
                                                quantity = 0.04)
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

def main_bot(raw_data, PORTFOLIO, DATA_PERIOD, all_data, TEST):

    change = [0,0,0]
    tradeWrite = 0
    #tradeWrite Key
    # 1 = buy
    # 2 = sell - loss
    # 3 = sell - bounce sell
    # 4 = sell - SM
    #print(all_data)
    
    crash_sell_position = 0
    if PORTFOLIO[0]['Position'] == True:
        crash_sell_position+=1
    
    if get_data(all_data, raw_data, DATA_PERIOD) or crash_sell_position == 2:
        #print(all_data['20_MA'])
        
        # !! need to loop this for multiple stocks
        if PORTFOLIO[0]['Position'] == False:
            #print('Flag 1 - after portfolio position')
            if check_entry(all_data):
                if execute_buy(PORTFOLIO[0], all_data, TEST):
                    tradeWrite = 1
                else:
                    tradeWrite = 0
                
                #print('Position: '+str(all_data['date'][-1])) ###
                #print('BUYING STOCK @ '+str(round(all_data['close'][-1],3)))
                #print('ATR: '+str(round(get_ATR(all_data, 14),3)))
                #print('Candle size: '+str(round(all_data['high'][-1]-all_data['low'][-1],3)))
                #print('Stop loss: '+str(round(PORTFOLIO[0]['sell_conditions']['stop_loss'],3))+' / Sell_marker: '+str(round(PORTFOLIO[0]['sell_conditions']['sell_marker'],3)))
                #risk = round((PORTFOLIO[0]['sell_conditions']['sell_marker'] - all_data['close'][-1])/(all_data['close'][-1]-PORTFOLIO[0]['sell_conditions']['stop_loss']),3)
                #print('Risk/Reward Ratio: '+str(risk)+'\n')

        elif PORTFOLIO[0]['Position'] == True:

            #Fixed Stop Loss
            if all_data['close'][-1] < PORTFOLIO[0]['sell_conditions']['stop_loss']:
                if TEST == True:
                    change[0] = (PORTFOLIO[0]['sell_conditions']['stop_loss']/all_data['close'][-1])-1.002
                    change[1] = 0
                    change[2] = 1
                
                tradeWrite = 2
                execute_sell(PORTFOLIO[0], TEST)
                
                

            #has the sell_marker been crossed already?
            ATR = get_ATR(all_data, 14)
            moving_diamond_hand = 0.5 #how deep the trail MA is made.
            if PORTFOLIO[0]['sell_conditions']['trail_stop']['above_marker']:
                
                # Price rebound to Fixed Sell Marker
                if all_data['close'][-1] <= PORTFOLIO[0]['sell_conditions']['sell_marker']:
                    if TEST == True:
                        change[0] = (PORTFOLIO[0]['sell_conditions']['sell_marker']/all_data['close'][-1])-1.002
                        change[1] = 1
                        change[2] = 1

                    tradeWrite = 3
                    execute_sell(PORTFOLIO[0], TEST)

                # Trail stop above fixed SM
                else:
                    if all_data['close'][-1] <= PORTFOLIO[0]['sell_conditions']['trail_stop']['moving_SM']:
                        if TEST == True:
                            change[0] = (PORTFOLIO[0]['sell_conditions']['trail_stop']['moving_SM']/all_data['close'][-1])-1.002
                            change[1] = 1
                            change[2] = 1                            

                        tradeWrite = 4
                        execute_sell(PORTFOLIO[0], TEST)
                    else:
                        #Update existing moving SM
                        if all_data['close'][-1] < all_data['close'][-2]:
                            pass
                        else:
                            PORTFOLIO[0]['sell_conditions']['trail_stop']['moving_SM'] = all_data['low'][-1]-moving_diamond_hand*ATR

            elif all_data['close'][-1] > PORTFOLIO[0]['sell_conditions']['sell_marker']:
                PORTFOLIO[0]['sell_conditions']['trail_stop']['moving_SM'] = all_data['low'][-1]-moving_diamond_hand*ATR
                PORTFOLIO[0]['sell_conditions']['trail_stop']['above_marker'] = True
                

    write_data(all_data, PORTFOLIO[0], tradeWrite)
    write_portfolios(PORTFOLIO)

    return change