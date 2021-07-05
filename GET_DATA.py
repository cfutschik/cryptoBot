import pandas as pd
import numpy as np

def get_data():

    #df = pd.read_csv("Bitfinex_ETHUSD_minute.csv") #Length = 307957
    df = pd.read_csv("Bitfinex_ETHUSD_1h.csv") #LEn = 27235
    #df = pd.read_csv("Bitfinex_ETHUSD_d.csv")
    #print(len(df))
    df['date'] = pd.to_datetime(df['date']) #date corrector

    #df.drop(df.tail(307957).index, inplace=True) #minute
    #df.drop(df.tail(27235).index, inplace=True) #hr

    df.drop(df.tail(25235).index, inplace=True)
    #df.drop(df.tail(290957).index, inplace=True)
    
    df = df.iloc[::-1] #inverting data
    df.reset_index(drop=True, inplace=True)

    return df

