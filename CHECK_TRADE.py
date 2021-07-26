from CHECK_ENTRY import check_entry
from TRADE import execute_buy
from TRADE import execute_sell
from GET_ATR import get_ATR


def check_trade(PORTFOLIO, all_data, TEST):

    tradeWrite = 0
    change = [0,0,0]
    
    if PORTFOLIO[0]['Position'] == False:
        #print('Flag 1 - after portfolio position')
        if check_entry(all_data):
            if execute_buy(PORTFOLIO[0], all_data, TEST):
                tradeWrite = 1
            else:
                tradeWrite = 0

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

    return change, tradeWrite