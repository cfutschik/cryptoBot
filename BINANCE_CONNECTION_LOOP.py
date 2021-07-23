import time,os
from datetime import datetime
from binance_bot import binance_bot 

if os.path.exists('dataFiles/ma_grad_data.csv'):
      os.remove('dataFiles/ma_grad_data.csv')

if os.path.exists('dataFiles/ma_trend_data.csv'):
      os.remove('dataFiles/ma_trend_data.csv')

if os.path.exists('dataFiles/ma_grad_data.csv'):
      os.remove('dataFiles/ma_grad_data.csv')

if os.path.exists('dataFiles/entry_data.csv'):
      os.remove('dataFiles/entry_data.csv')

if os.path.exists('dataFiles/RSI_data.csv'):
      os.remove('dataFiles/RSI_data.csv')

if os.path.exists('dataFiles/candle_pattern_data.csv'):
      os.remove('dataFiles/candle_pattern_data.csv')

if os.path.exists('dataFiles/bull_bear_candle_data.csv'):
      os.remove('dataFiles/bull_bear_candle_data.csv')

if os.path.exists('dataFiles/candle_stick_data.csv'):
      os.remove('dataFiles/candle_stick_data.csv')

if os.path.exists('dataFiles/buy_info.csv'):
      os.remove('dataFiles/buy_info.csv')                              

if os.path.exists("dataFiles/sell_info_data_copy.csv"):
      os.remove("dataFiles/sell_info_data_copy.csv")

while True:
    try:
        binance_bot()
    except:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print('Trying to restart - ', current_time)
        time.sleep(5)
