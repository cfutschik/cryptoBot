# General Functions
import numpy as np
from GET_CLOSE_DATA import get_close_data
from PRINT_ANALYSIS import print_analysis
from GET_DATA import get_data
from GET_ATR import get_ATR
from GET_TREND import get_trend
from CHECK_ENTRY import check_entry

### DATA ANALYSIS
from PRINT_CHARTS import print_charts #################################################################
#from datatime import datetime
#datetime.fromtimestamp()
###

def trail_stop_sell(PORTFOLIO):
    
    sell_point = True

    


    return sell_point



def execute_buy(PORTFOLIO, all_closes, all_highs, all_lows):

    ATR = get_ATR(all_closes, all_highs, all_lows, 14)

    PORTFOLIO['Position'] = True
    PORTFOLIO['buy_price'] = all_closes[-1]
    PORTFOLIO['sell_conditions']['stop_loss'] = all_lows[-1]-ATR
    PORTFOLIO['sell_conditions']['sell_marker'] = all_closes[-1]+2*ATR
    
    #order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
    return


if __name__ == "__main__":

### pretend ticker ####
    #o,h,l,c,close_time = get_close_data() ##################################################################
    all_candle_data = get_data()
    date = all_candle_data['date']
    o = np.array(all_candle_data['open'])
    h = np.array(all_candle_data['high'])
    l = np.array(all_candle_data['low'])
    c = np.array(all_candle_data['close'])
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
                    'trail_stop': False
                }
                },{}]
    #TRADE_SYMBOL = 'ETHUSD'
    #TRADE_QUANTITY = 0.05
    SELL_BUY_INFO = open("SELL_BUY_INFO.txt","w") #Creating error file

# Empty Arrays
    
    all_opens = []
    all_closes = []
    all_highs = []
    all_lows = []
    #SHORT_MA = []
    #LONG_MA = []
# Initializers
    #iteration = 0

### Pretend Ticker ###############################################################
    trend_s = []   ###################################################################
    trend_l = []    ##################################################################
    #atr = []        ##################################################################
    x = 0           ##################################################################
    buy_1 = []        ##################################################################
    buy_2 = []        ##################################################################
    buy_3 = []        ##################################################################
    bottom_value = 1700
    buy_x = bottom_value
    sell_x = bottom_value
    sell_good = bottom_value
    sell_stop = bottom_value
    buy_marker = bottom_value
    all_analysis_data = []
    TOTAL_PROFIT = 0.0 ###############################################################
    WIN_LOSS_RATIO = 0.0 ###############################################################
    SALES = 0.0
    data_length = len(o)
    while x < data_length: ### 4000 ###############################################################
        all_data_subset = []
###----------------####

        if len(all_closes) < DATA_PERIOD:
            all_closes.append(c[x])
            all_highs.append(h[x])
            all_lows.append(l[x])
            all_opens.append(o[x])
  
        if len(all_closes) == DATA_PERIOD:
            # Adding new ticker point
            all_closes.pop(0)
            all_highs.pop(0)
            all_lows.pop(0)
            all_opens.pop(0)
            all_closes.append(c[x])
            all_highs.append(h[x])
            all_lows.append(l[x])
            all_opens.append(o[x])

            #Finding trends
            entry = check_entry(all_opens, all_highs, all_lows, all_closes)
            #entry[buy/sell,close,type]

            # !! need to loop this for multiple stocks
            if PORTFOLIO[0]['Position'] == False:
                if entry[0] == 1:
                    execute_buy(PORTFOLIO[0], all_closes, all_highs, all_lows)
                    #side = 'BUY'
                    #order_type = 'ORDER_TYPE_MARKET'
                    #(symbol, sie, order_type=ORDER_TYPE_MARKET, quantity, all_closes, all_highs, all_lows

                    SELL_BUY_INFO.write('Position: '+str(x)+'\n') ###
                    SELL_BUY_INFO.write('BUYING STOCK @ '+str(round(all_closes[-1],3))+'\n')
                    SELL_BUY_INFO.write('Candle pattern: '+str(entry[2])+'\n')
                    SELL_BUY_INFO.write('ATR: '+str(round(get_ATR(all_closes, all_highs, all_lows, 14),3))+'\n')
                    SELL_BUY_INFO.write('Candle size: '+str(round(all_highs[-1]-all_lows[-1],3))+'\n')
                    SELL_BUY_INFO.write('Stop loss: '+str(round(PORTFOLIO[0]['sell_conditions']['stop_loss'],3))+' - Sell_marker: '+str(round(PORTFOLIO[0]['sell_conditions']['sell_marker'],3))+'\n')
                    risk = round((PORTFOLIO[0]['sell_conditions']['sell_marker'] - all_closes[-1])/(all_closes[-1]-PORTFOLIO[0]['sell_conditions']['stop_loss']),3)
                    SELL_BUY_INFO.write('Risk/Reward Ratio: '+str(risk)+'\n')
                    
                    buy_x = all_closes[-1]###
                    sell_x = bottom_value ###
                    sell_good = bottom_value
                    buy_marker = PORTFOLIO[0]['sell_conditions']['sell_marker'] ###
                    sell_stop = PORTFOLIO[0]['sell_conditions']['stop_loss'] ###

                else: ####
                    sell_x = bottom_value ###
                    sell_good = bottom_value

            elif PORTFOLIO[0]['Position'] == True:

                #Sell conditions

                if all_closes[-1] < PORTFOLIO[0]['sell_conditions']['stop_loss']:
                    PORTFOLIO[0]['Position'] = False

                    change = PORTFOLIO[0]['sell_conditions']['stop_loss'] - PORTFOLIO[0]['buy_price']
                    #print('stop_loss: '+str(PORTFOLIO[0]['stop_loss']))
                    #print('stop_sell: '+str(PORTFOLIO[0]['sell_marker']))
                    #print('buy_price: '+str(PORTFOLIO[0]['buy_price']))
                    SELL_BUY_INFO.write('SELLING STOCK @ '+str(round(all_closes[-1],3))+' - profit/loss: '+str(round(change,3))+'\n\n')
                    #print('SELLING STOCK @ '+str(round(all_closes[-1],3))+' - profit/loss: '+str(round(change,3)))

                    SALES+=1
                    TOTAL_PROFIT+=change

                    sell_x = all_closes[-1] #############################################################
                    sell_good = bottom_value
                    buy_marker = bottom_value ###################################################################
                    sell_stop = bottom_value ####################################################################

                elif all_closes[-1] > PORTFOLIO[0]['sell_conditions']['sell_marker']:
                    #trail_stop_sell()
                    PORTFOLIO[0]['Position'] = False

                    change = PORTFOLIO[0]['sell_conditions']['sell_marker'] - PORTFOLIO[0]['buy_price']
                    #print('stop_loss: '+str(PORTFOLIO[0]['stop_loss']))
                    #print('stop_sell: '+str(PORTFOLIO[0]['sell_marker']))
                    #print('buy_price: '+str(PORTFOLIO[0]['buy_price']))
                    SELL_BUY_INFO.write('SELLING STOCK @ '+str(round(all_closes[-1],3))+' - profit/loss: '+str(round(change,3))+'\n\n')
                    #print('SELLING STOCK @ '+str(round(all_closes[-1],3))+' - profit/loss: '+str(round(change,3))+'\n\n')

                    if change > 0: 
                            WIN_LOSS_RATIO+=1
                    SALES+=1
                    TOTAL_PROFIT+=change

                    sell_good = all_closes[-1] #############################################################
                    sell_x = bottom_value
                    buy_marker = bottom_value ###################################################################
                    sell_stop = bottom_value ####################################################################

                else:
                    #print('HOLDING @ '+str(all_closes[-1]))

                    buy_x = bottom_value###############################################################
                    sell_x = bottom_value##############################################################
                    

### Pretend Ticker ###################################################################            
            short_trend, long_trend = get_trend(all_closes)###############################################################
            trend_s.append(short_trend)##################################################################
            trend_l.append(long_trend)##################################################################
            trend_data = []###############################################################
            trend_data.append(short_trend)###############################################################
            trend_data.append(long_trend)###############################################################
            all_data_subset.append(trend_data)###############################################################
            #buy/sell/stay 2240###############################################################

            if entry[0] == 1:###############################################################
                if entry[2] == 1:###############################################################
                    buy_1 = all_closes[-1]###############################################################
                    buy_2 = bottom_value###############################################################
                    buy_3 = bottom_value###############################################################
                elif entry[2] == 2:###############################################################
                    buy_2 = all_closes[-1]###############################################################
                    buy_1 = bottom_value###############################################################
                    buy_3 = bottom_value###############################################################
                elif entry[2] == 3:###############################################################
                    buy_3 = all_closes[-1]###############################################################
                    buy_1 = bottom_value###############################################################
                    buy_2 = bottom_value###############################################################
            else:###############################################################
                buy_1 = bottom_value###############################################################
                buy_2 = bottom_value###############################################################
                buy_3 = bottom_value###############################################################

            buy_subset = [buy_1,buy_2,buy_3]###############################################################
            all_data_subset.append(buy_subset)###############################################################
            buy_sell_points = [buy_x, sell_x, sell_good, buy_marker, sell_stop]
            all_data_subset.append(buy_sell_points)        
            all_analysis_data.append(all_data_subset)###############################################################

        
        x +=1 ##################################################################
###----------------###################################################################

# 0,                         1,                      2,                        
#[[Short trend, long trend], [buy_1, buy_2, buy_3], [buy_close, sell_close, buy_marker, sell_stop]]

print('Total profit: '+str(round(TOTAL_PROFIT, 2)))
print('Success Rate: '+str(round(WIN_LOSS_RATIO/SALES*100, 2)))

#print(len(all_analysis_data))
print_analysis(all_analysis_data, DATA_PERIOD)