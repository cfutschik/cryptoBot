import os
import numpy as np
import pandas as pd

def check_all_data(DATA_PERIOD):

    all_data = {
    'open': [],
    'close': [],
    'high': [],
    'low': [],
    'date': [],
    'volume': [],
    '20_MA': [],
    '50_MA': []
    }

    if os.path.exists('dataFiles/candle_stick_data.csv'):

        try:

            csd_df = pd.read_csv("dataFiles/candle_stick_data.csv",
                                    names = ['date', 'high', 'low', 'open', 'close', 'volume', '20_MA', '50_MA'])


            for i in range(DATA_PERIOD):

                if np.float64(csd_df['close'][i]) == np.NaN:
                    pass
                else:
                    all_data['open'].append(np.float64(csd_df['open'][i]))
                    all_data['close'].append(np.float64(csd_df['close'][i]))
                    all_data['high'].append(np.float64(csd_df['high'][i]))
                    all_data['low'].append(np.float64(csd_df['low'][i]))
                    all_data['date'].append(csd_df['date'][i])
                    all_data['volume'].append(np.float64(csd_df['volume'][i]))
                    all_data['20_MA'].append(np.float64(csd_df['20_MA'][i]))
                    all_data['50_MA'].append(np.float64(csd_df['50_MA'][i]))

            print("Data imported from previous data set.")

            return all_data
        except:
            print("Data could not be imported from previous data set.")

    else:
        return all_data