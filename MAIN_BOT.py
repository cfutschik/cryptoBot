from GET_DATA import get_data
from WRITE_DATA import write_data
from WRITE_PORTFOLIO import write_portfolios
from CHECK_TRADE import check_trade

def main_bot(raw_data, PORTFOLIO, DATA_PERIOD, all_data, TEST):

    
    #tradeWrite Key
    # 1 = buy
    # 2 = sell - loss
    # 3 = sell - bounce sell
    # 4 = sell - SM
    #print(all_data)

    tradeWrite = 0
    change = [0,0,0]

    if len(all_data['close']) >= DATA_PERIOD:
        print('Flag 1')
        all_data = get_data(all_data, raw_data, DATA_PERIOD)
        change, tradeWrite = check_trade(PORTFOLIO, all_data, TEST)

    elif len(all_data['close']) < DATA_PERIOD and PORTFOLIO[0]['Position'] == True:
        print('Flag 2')
        all_data = get_data(all_data, raw_data, DATA_PERIOD)
        change, tradeWrite = check_trade(PORTFOLIO, all_data, TEST)
        
    else:
        print('Flag 3')
        all_data = get_data(all_data, raw_data, DATA_PERIOD)
    
    write_data(all_data, PORTFOLIO[0], tradeWrite)
    write_portfolios(PORTFOLIO)

    print(str(len(all_data['close']))+' - '+str(all_data['close'][-1]))

    return change