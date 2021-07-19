# General Functions
from GET_MA_GRAD import get_ma_grad
import numpy as np
from PRINT_ANALYSIS import print_analysis
from GET_ALL_DATA import get_all_data
from GET_ATR import get_ATR
from GET_TREND import get_trend
from CHECK_ENTRY import check_entry
from GET_SUP_RES import get_sup_res

### DATA ANALYSIS
from PRINT_CHARTS import print_charts #################################################################
#from datatime import datetime
#datetime.fromtimestamp()
###

def trail_stop_sell(PORTFOLIO, all_data):
    #True will sell
    
    sell_point = True
    return sell_point

def execute_buy(PORTFOLIO, all_data):

    ATR = get_ATR(all_data, 14)

    PORTFOLIO['Position'] = True
    PORTFOLIO['buy_price'] = all_data['close'][-1]
    PORTFOLIO['sell_conditions']['stop_loss'] = all_data['low'][-1]-ATR
    PORTFOLIO['sell_conditions']['sell_marker'] = all_data['close'][-1]+2*ATR
    
    #order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
    return

def execute_sell(PORTFOLIO):
    #clean prior sale data 
    PORTFOLIO[0]['Position'] = False
    PORTFOLIO[0]['sell_conditions']['trail_stop']['moving_SM'] = 0.0
    PORTFOLIO[0]['sell_conditions']['trail_stop']['above_marker'] = False

    return

if __name__ == "__main__":

### pretend ticker ####
    #o,h,l,c,close_time = get_close_data() ##################################################################
    all_ticker_data = get_all_data()
    date = all_ticker_data['date']
    o = np.array(all_ticker_data['open'])
    h = np.array(all_ticker_data['high'])
    l = np.array(all_ticker_data['low'])
    c = np.array(all_ticker_data['close'])
    dates = all_ticker_data['date']
    #print(len(l))###############################################################
###----------------####

# Trade details
    DATA_PERIOD = 350
    LONG_PERIOD = 200
    SHORT_PERIOD = 20
    RSI_PERIOD = 14
    RSI_OVERBOUGHT = 70
    RSI_OVERSOLD = 30
    PORTFOLIO = [{'Stock':'ETHUSD',
                'Trade_Quantity':0.05,
                'Position':False,
                'buy_price': 0.0, 
                'sell_conditions':{
                    'stop_loss': 0.0,
                    'sell_marker': 0.0,
                    'trail_stop': {
                        'above_marker': False,
                        'moving_SM' : 0.0,
                    }
                }
                },{}]
    #TRADE_SYMBOL = 'ETHUSD'
    #TRADE_QUANTITY = 0.05
    SELL_BUY_INFO = open("SELL_BUY_INFO.txt","w") #Creating error file

# Empty Arrays
    all_data = {
        'open': [],
        'close': [],
        'high': [],
        'low': [],
        'date': []
        }

### Pretend Ticker ###############################################################
    trend_s = []   ###################################################################
    trend_l = []    ##################################################################
    #atr = []        ##################################################################
    x = 0           ##################################################################
    buy_1 = []        ##################################################################
    buy_2 = []        ##################################################################
    buy_3 = []        ##################################################################
    bottom_value = 500
    buy_x = bottom_value
    sell_x = bottom_value
    sell_good = bottom_value
    sell_stop = bottom_value
    buy_marker = bottom_value
    all_analysis_data = []
    TOTAL_PROFIT = 0.0 ###############################################################
    WIN_LOSS_RATIO = 0.0 ###############################################################
    SALES = 0.0
    TRAIL_TRADE = 0
    STOP_TRADE = 0
    BOUNCE_TRADE = 0
    INITIAL_BALANCE = 1000
    data_length = len(o)
    xyz = 1
    while x < data_length: ### 4000 ###############################################################
        all_data_subset = []
###----------------####

        if len(all_data['close']) < DATA_PERIOD:

            all_data['open'].append(all_ticker_data['open'][x])
            all_data['close'].append(all_ticker_data['close'][x])
            all_data['high'].append(all_ticker_data['high'][x])
            all_data['low'].append(all_ticker_data['low'][x])
            all_data['date'].append(all_ticker_data['date'][x])

        if len(all_data['close']) == DATA_PERIOD:
            # Adding new ticker point

            all_data['open'].pop(0)
            all_data['close'].pop(0)
            all_data['high'].pop(0)
            all_data['low'].pop(0)
            all_data['date'].pop(0)
            
            all_data['open'].append(all_ticker_data['open'][x])
            all_data['close'].append(all_ticker_data['close'][x])
            all_data['high'].append(all_ticker_data['high'][x])
            all_data['low'].append(all_ticker_data['low'][x])
            all_data['date'].append(all_ticker_data['date'][x])
            
            # Start main loop
            peak_tracker = get_sup_res(all_data)
            ma_grad_data = get_ma_grad(all_data)
            

                
            # !! need to loop this for multiple stocks
            if PORTFOLIO[0]['Position'] == False:
                if check_entry(all_data) >= 2.5:
                    execute_buy(PORTFOLIO[0], all_data)
                    
                    SELL_BUY_INFO.write('Position: '+str(all_data['date'][-1])+'\n') ###
                    SELL_BUY_INFO.write('BUYING STOCK @ '+str(round(all_data['close'][-1],3))+'\n')
                    SELL_BUY_INFO.write('ATR: '+str(round(get_ATR(all_data, 14),3))+'\n')
                    SELL_BUY_INFO.write('Candle size: '+str(round(all_data['high'][-1]-all_data['low'][-1],3))+'\n')
                    SELL_BUY_INFO.write('Stop loss: '+str(round(PORTFOLIO[0]['sell_conditions']['stop_loss'],3))+' / Sell_marker: '+str(round(PORTFOLIO[0]['sell_conditions']['sell_marker'],3))+'\n')
                    risk = round((PORTFOLIO[0]['sell_conditions']['sell_marker'] - all_data['close'][-1])/(all_data['close'][-1]-PORTFOLIO[0]['sell_conditions']['stop_loss']),3)
                    SELL_BUY_INFO.write('Risk/Reward Ratio: '+str(risk)+'\n')
                    
                    buy_x = all_data['close'][-1]###
                    sell_x = bottom_value ###
                    sell_good = bottom_value ###
                    buy_marker = PORTFOLIO[0]['sell_conditions']['sell_marker'] ###
                    sell_stop = PORTFOLIO[0]['sell_conditions']['stop_loss'] ###

                else: 
                    sell_x = bottom_value ###
                    sell_good = bottom_value ###
                    buy_x = bottom_value ###

            elif PORTFOLIO[0]['Position'] == True:

                #Fixed Stop Loss
                if all_data['close'][-1] < PORTFOLIO[0]['sell_conditions']['stop_loss']:
                    PORTFOLIO[0]['Position'] = False

                    change = PORTFOLIO[0]['sell_conditions']['stop_loss']/PORTFOLIO[0]['buy_price']
                    SELL_BUY_INFO.write('SELLING STOCK @ '+str(round(all_data['close'][-1],3))+' - profit/loss: '+str(round((change-1)*100,3))+'\n\n')

                    SALES+=1
                    INITIAL_BALANCE*=change
                    TOTAL_PROFIT+=change
                    STOP_TRADE+=1
                    sell_x = all_data['close'][-1] ###
                    sell_good = bottom_value
                    buy_marker = bottom_value ###
                    sell_stop = bottom_value ###

                #has the sell_marker been crossed already?

                if PORTFOLIO[0]['sell_conditions']['trail_stop']['above_marker']:
                    ATR = get_ATR(all_data, 14)
                    # Price rebound to Fixed Sell Marker
                    if all_data['close'][-1] <= PORTFOLIO[0]['sell_conditions']['sell_marker']:
                        

                        change = PORTFOLIO[0]['sell_conditions']['sell_marker']/PORTFOLIO[0]['buy_price']
                        fee = (change-1)*100*0.005
                        total_change = change - fee
                        SELL_BUY_INFO.write('SELLING STOCK @ '+str(round(all_data['close'][-1],3))+' - profit/loss: '+str(round((change-1)*100,3))+'\n\n')
                        if change > 0: 
                                WIN_LOSS_RATIO+=1
                        SALES+=1
                        TOTAL_PROFIT+=change
                        INITIAL_BALANCE*=change
                        BOUNCE_TRADE+=1
                        sell_good = all_data['close'][-1] ###
                        sell_x = bottom_value
                        buy_marker = bottom_value ###
                        sell_stop = bottom_value ###

                        execute_sell(PORTFOLIO)

                    # Trail stop above fixed SM
                    elif PORTFOLIO[0]['sell_conditions']['trail_stop']['moving_SM']:
                        if all_data['close'][-1] <= PORTFOLIO[0]['sell_conditions']['trail_stop']['moving_SM']:
                        
                            change = PORTFOLIO[0]['sell_conditions']['trail_stop']['moving_SM']/PORTFOLIO[0]['buy_price']
                            fee = (change-1)*100*0.005
                            total_change = change - fee
                            move_SM = PORTFOLIO[0]['sell_conditions']['trail_stop']['moving_SM']
                            SELL_BUY_INFO.write('Moving SM: '+str(round(move_SM,3))+'\n')
                            SELL_BUY_INFO.write('SELLING STOCK @ '+str(round(all_data['close'][-1],3))+' - profit/loss: '+str(round((change-1)*100,3))+'\n\n')
                            if change > 0: 
                                    WIN_LOSS_RATIO+=1
                            SALES+=1
                            TOTAL_PROFIT+=change
                            INITIAL_BALANCE*=change
                            TRAIL_TRADE+=1
                            sell_good = all_data['close'][-1] ###
                            sell_x = bottom_value
                            buy_marker = bottom_value ###
                            sell_stop = bottom_value ###

                            execute_sell(PORTFOLIO)
                        else:
                            #Update existing moving SM
                            PORTFOLIO[0]['sell_conditions']['trail_stop']['moving_SM'] = all_data['low'][-1]-0.1*ATR
                    else:
                        #Create moving SM
                        PORTFOLIO[0]['sell_conditions']['trail_stop']['moving_SM'] = all_data['low'][-1]-0.1*ATR

                elif all_data['close'][-1] > PORTFOLIO[0]['sell_conditions']['sell_marker']:
                    PORTFOLIO[0]['sell_conditions']['trail_stop']['above_marker'] = True

                else:
                    buy_x = bottom_value###
                    sell_x = bottom_value###
                    

### Pretend Ticker ###################################################################            
            short_trend, long_trend = get_trend(all_data['close'])###
            trend_s.append(short_trend)###
            trend_l.append(long_trend)###
            trend_data = []###
            trend_data.append(short_trend)###
            trend_data.append(long_trend)###
            all_data_subset.append(trend_data)###
            #buy/sell/stay 2240###

            buy_1 = bottom_value###
            buy_2 = bottom_value###
            buy_3 = bottom_value###

            buy_subset = [buy_1,buy_2,buy_3]###
            all_data_subset.append(buy_subset)###
            buy_sell_points = [buy_x, sell_x, sell_good, buy_marker, sell_stop]###
            all_data_subset.append(buy_sell_points)###      
            all_data_subset.append(peak_tracker)###
            all_data_subset.append(ma_grad_data)###  
            all_analysis_data.append(all_data_subset)###

            #if x%100 == 0:
            #    print("Iteration: "+str(x))

        x +=1 ###


# 0,                         1,                      2,                                            3,
#[[Short trend, long trend], [buy_1, buy_2, buy_3], [buy_close, sell_close, buy_marker, sell_stop], [past peak, nearest peak]  ]
#print('Total profit: '+str(round(TOTAL_PROFIT, 2)))
print('Total profit: '+str(round(INITIAL_BALANCE, 2)))
print('Success Rate: '+str(round(WIN_LOSS_RATIO/SALES*100, 2)))
print('Total bids: '+str(SALES))
print('Stop Loss Trades: '+str(round(STOP_TRADE/SALES*100,1)))
print('Sell Marker Trades: '+str(round(BOUNCE_TRADE/SALES*100,1)))
print('Trailing Stop Trades: '+str(round(TRAIL_TRADE/SALES*100,1)))

#print(len(all_analysis_data))
print_analysis(all_analysis_data, DATA_PERIOD)