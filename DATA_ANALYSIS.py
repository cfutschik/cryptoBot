#from re import template
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import shutil, os
import csv, talib, time

# Deleting Copies
if os.path.exists("dataFiles/candle_stick_data_copy.csv"):
      os.remove("dataFiles/candle_stick_data_copy.csv")

if os.path.exists("dataFiles/buy_info_copy.csv"):
      os.remove("dataFiles/buy_info_copy.csv")

if os.path.exists("dataFiles/sell_info_data_copy.csv"):
      os.remove("dataFiles/sell_info_data_copy.csv")

#Copying data
shutil.copyfile("dataFiles/candle_stick_data.csv","dataFiles/candle_stick_data_copy.csv")
#shutil.copyfile("dataFiles/buy_info.csv","dataFiles/buy_info_copy.csv")
#shutil.copyfile("dataFiles/sell_info.csv","dataFiles/sell_info_copy.csv")

csd_df = pd.read_csv("dataFiles/candle_stick_data_copy.csv")
#bi_df = pd.read_csv("dataFiles/buy_info_copy.csv", header=None)
#si_df = pd.read_csv("dataFiles/sell_info_copy.csv", header=None)

buy_header = ['date', 'buy_price', 'ATR', 'candle_size', 'stop_loss', 'sell_marker','risk']
sell_header = ['date', 'sell_price', 'gain']
#bi_df.to_csv("dataFiles/buy_info_copy.csv", header=buy_header)
#si_df.to_csv("dataFiles/sell_info_
#copy.csv", header=sell_header)

#bi_df = pd.read_csv("dataFiles/buy_info_copy.csv")
#si_df = pd.read_csv("dataFiles/sell_info_copy.csv")

csd_df['date'] = (pd.to_datetime(csd_df['date'],unit='ms'))

print(csd_df['date'])
#print(bi_df['date'])


#print(si_df['gain'])
#print(bi_df['buy_price'])

#print(csd_df['date'])

fig = make_subplots()
fig.add_traces([go.Candlestick(x=csd_df['date'], 
                open=csd_df['open'],
                high=csd_df['high'],
                low=csd_df['low'],
                close=csd_df['close']), 

                go.Scatter(
                x=csd_df['date'],
                y=csd_df['20_MA'],
                line = dict(color="red"),
                name = "20_MA"),

                go.Scatter(
                x=csd_df['date'],
                y=csd_df['50_MA'],
                line = dict(color="cyan"),
                name = "50_MA")],
                
                rows = [1,1,1],
                cols = [1,1,1])

fig.update_layout(xaxis_rangeslider_visible=False, template='plotly_dark')
fig.show()

#fig1 = make_subplots(rows=3)
#fig1.add_traces([go.Scatter(
                #x=dataSetInv['date'],
                #y=dataSetInv['RSI'],
                #line = dict(color="magenta"),
                #name = "RSI"),

                #go.Scatter(
                #x=dataSetInv['date'],
                #y=dataSetInv['ATR'],
                #line = dict(color="red"),
                #name = "ATR"),
                
                #go.Scatter(
                #x=dataSetInv['date'],
                #y=dataSetInv['ma_grad_20'],
                #line = dict(color="red"),
                #name = "MA Grad 20"),

                #go.Scatter(
                #x=dataSetInv['date'],
                #y=dataSetInv['ma_grad_50'],
                #line = dict(color="blue"),
                #name = "MA Grad 50")],
                
                #go.Scatter(
                #x=dataSetInv['date'],
                #y=dataSetInv['ATR'],
                #line = dict(color="red"),
                #name = "ATR")],
                
#                rows = [1, 2, 3, 3],
#                cols = [1, 1, 1, 1])



#fig1.update_layout(xaxis_rangeslider_visible=False, template='plotly_dark')
#fig1.show()

