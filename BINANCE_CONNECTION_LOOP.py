import time,os
from datetime import datetime
from binance_bot import binance_bot 

while True:
    try:
        binance_bot()
    except:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print('Trying to restart - ', current_time)
        time.sleep(5)
