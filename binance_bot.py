# General Functions
import numpy as np
import websocket, json, config
from binance.client import Client
from binance.enums import *

from MAIN_BOT import main_bot
from GET_ALL_DATA import get_all_data
from IMPORT_TRADE_PORTFOLIO import import_trade_portfolio

def binance_bot():
    client = Client(config.API_KEY, config.API_SECRET)
    SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"
    DATA_PERIOD = 60
    connectionTest = open('dataFiles/connectionTest.txt','w')

    all_data = {
        'open': [],
        'close': [],
        'high': [],
        'low': [],
        'date': [],
        '20_MA': [],
        '50_MA': []
        }

    PORTFOLIO = import_trade_portfolio()

    ETH_BALANCE = round(float(client.get_account()['balances'][2]['free']),6)
    BUSD_BALANCE = round(float(client.get_account()['balances'][188]['free']),6)
    #PORTFOLIO[0] = ETHBUSD

    PORTFOLIO[0]['Balance_1'] = ETH_BALANCE
    PORTFOLIO[0]['Balance_2'] = BUSD_BALANCE

    #[{'Stock':'ETHBUSD',
    #            'Balance_1': ETH_BALANCE, 
    #            'Balance_2': BUSD_BALANCE, 
    #            'TRD_QTY': 0.1,
    #            'Position': False,
    #            'buy_price': 0.0, 
    #            'sell_conditions':{
    #                'stop_loss': 0.0,
    #                'sell_marker': 0.0,
    #                'trail_stop': {
    #                    'above_marker': False,
    #                    'moving_SM' : 0.0,
    #            }
    #            }

        #},{}]

    TEST = False

    if TEST:
        print('Starting Test')
        all_ticker_data = get_all_data()
        date = all_ticker_data['date']
        o = np.array(all_ticker_data['open'])
        h = np.array(all_ticker_data['high'])
        l = np.array(all_ticker_data['low'])
        c = np.array(all_ticker_data['close'])

        raw_data = []

        for x in range(len(all_ticker_data)):
            data = {'k': {
                        'o': all_ticker_data['open'][x],
                        'c': all_ticker_data['close'][x],
                        'h': all_ticker_data['high'][x],
                        'l': all_ticker_data['low'][x],
                        'T': all_ticker_data['date'][x]
                        }}
            raw_data.append(data)

        BALANCE_INIT = 0

        for i in range(len(raw_data)):
            change = main_bot(raw_data[i], PORTFOLIO, DATA_PERIOD, all_data, TEST)
            BALANCE_INIT+=(change-1)
            
            print(BALANCE_INIT)

    else:
        # use previous data to populate first DATA period entries
        if False: 
            for i in range(DATA_PERIOD):
                raw_data[i]['date'] = i*1000
                main_bot(raw_data[i], PORTFOLIO, DATA_PERIOD, all_data, False)

        def on_open(ws):
                print('Opened connection')

        def on_close(ws):
            print('closed connection')

        def on_message(ws, message):
            global closes, in_position
            raw_data = json.loads(message)
            print('Connected')
            connectionTest.write('Connected')

            try:
                main_bot(raw_data, PORTFOLIO, DATA_PERIOD, all_data, False)
            except:
                print('Main Issue')

            #if raw_data['k']['x']:

        ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
        ws.run_forever()             
