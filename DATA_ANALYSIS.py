#from re import template
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import shutil, os
import csv, talib, time

#entry_qaulity = entry_qaulity
#candle_pattern_data = check , candle score
#ma_trend_data = trend[0], trand[1], score
#ma_grad_data = grad[0], grad[1], score
#RSI_data = RSI[-1], score

# Deleting Copies
if os.path.exists("dataFiles/candle_stick_data_copy.csv"):
      os.remove("dataFiles/candle_stick_data_copy.csv")

if os.path.exists("dataFiles/buy_info_copy.csv"):
      os.remove("dataFiles/buy_info_copy.csv")

if os.path.exists("dataFiles/sell_info_data_copy.csv"):
      os.remove("dataFiles/sell_info_data_copy.csv")

if os.path.exists('dataFiles/ma_grad_data_copy.csv'):
      os.remove('dataFiles/ma_grad_data_copy.csv')

if os.path.exists('dataFiles/ma_trend_data_copy.csv'):
      os.remove('dataFiles/ma_trend_data_copy.csv')

if os.path.exists('dataFiles/ma_grad_data_copy.csv'):
      os.remove('dataFiles/ma_grad_data_copy.csv')

if os.path.exists('dataFiles/entry_data_copy.csv'):
      os.remove('dataFiles/entry_data_copy.csv')

if os.path.exists('dataFiles/RSI_data_copy.csv'):
      os.remove('dataFiles/RSI_data_copy.csv')

if os.path.exists('dataFiles/candle_pattern_data_copy.csv'):
      os.remove('dataFiles/candle_pattern_data_copy.csv')

if os.path.exists('dataFiles/bull_bear_candle_data_copy.csv'):
      os.remove('dataFiles/bull_bear_candle_data_copy.csv')

if os.path.exists('dataFiles/total_entry_data.csv'):
      os.remove('dataFiles/total_entry_data.csv')



#Copying data
shutil.copyfile("dataFiles/candle_stick_data.csv","dataFiles/candle_stick_data_copy.csv")
shutil.copyfile("dataFiles/buy_info.csv","dataFiles/buy_info_copy.csv")
shutil.copyfile("dataFiles/sell_info.csv","dataFiles/sell_info_copy.csv")
shutil.copyfile('dataFiles/bull_bear_candle_data.csv','dataFiles/bull_bear_candle_data_copy.csv')
shutil.copyfile('dataFiles/candle_pattern_data.csv','dataFiles/candle_pattern_data_copy.csv')
shutil.copyfile('dataFiles/RSI_data.csv','dataFiles/RSI_data_copy.csv')
shutil.copyfile('dataFiles/entry_data.csv','dataFiles/entry_data_copy.csv')
shutil.copyfile('dataFiles/ma_grad_data.csv','dataFiles/ma_grad_data_copy.csv')
shutil.copyfile('dataFiles/ma_trend_data.csv','dataFiles/ma_trend_data_copy.csv')

csd_df = pd.read_csv("dataFiles/candle_stick_data_copy.csv")
bi_df = pd.read_csv("dataFiles/buy_info_copy.csv", header=None)
si_df = pd.read_csv("dataFiles/sell_info_copy.csv", header=None)
bbcs_df = pd.read_csv('dataFiles/bull_bear_candle_data_copy.csv')
cpd_df = pd.read_csv('dataFiles/candle_pattern_data_copy.csv')
RSI_df = pd.read_csv('dataFiles/RSI_data_copy.csv')
entry_df = pd.read_csv('dataFiles/entry_data_copy.csv')
mag_df = pd.read_csv('dataFiles/ma_grad_data_copy.csv')
mat_dfd = pd.read_csv('dataFiles/ma_trend_data_copy.csv')

bbcs_header = ['bb_check','score']
entry_quality_header = ['entry_quality']
candle_pattern_header = ['check' , 'candle_score']
ma_trend_header = ['trend_0', 'trend_1', 'ma_trend_score']
ma_grad_header = ['grad_0', 'grad_1', 'ma_grad_score']
RSI_header = ['RSI' , 'score']
buy_header = ['date', 'buy_price', 'ATR', 'candle_size', 'stop_loss', 'sell_marker','risk']
sell_header = ['date', 'sell_price', 'gain']
data_header = ['date', 'high', 'low', 'open', 'close', '20_MA', '50_MA']

csd_df.to_csv("dataFiles/candle_stick_data_copy.csv", header=data_header)
bi_df.to_csv("dataFiles/buy_info_copy.csv", header=buy_header)
si_df.to_csv("dataFiles/sell_info_copy.csv", header=sell_header)
bbcs_df.to_csv('dataFiles/bull_bear_candle_data_copy.csv', header=bbcs_header)
cpd_df.to_csv('dataFiles/candle_pattern_data_copy.csv', header=candle_pattern_header)
RSI_df.to_csv('dataFiles/RSI_data_copy.csv', header=RSI_header)
entry_df.to_csv('dataFiles/entry_data_copy.csv', header=entry_quality_header)
mag_df.to_csv('dataFiles/ma_grad_data_copy.csv', header=ma_grad_header)
mat_dfd.to_csv('dataFiles/ma_trend_data_copy.csv', header=ma_trend_header)

bi_df = pd.read_csv("dataFiles/buy_info_copy.csv")
si_df = pd.read_csv("dataFiles/sell_info_copy.csv")
csd_df = pd.read_csv("dataFiles/candle_stick_data_copy.csv")
bbcs_df = pd.read_csv('dataFiles/bull_bear_candle_data_copy.csv')
cpd_df = pd.read_csv('dataFiles/candle_pattern_data_copy.csv')
RSI_df = pd.read_csv('dataFiles/RSI_data_copy.csv')
entry_df = pd.read_csv('dataFiles/entry_data_copy.csv')
mag_df = pd.read_csv('dataFiles/ma_grad_data_copy.csv')
mat_df = pd.read_csv('dataFiles/ma_trend_data_copy.csv')


#bbcs_df = ['bb_check','score']
#entry_df = ['entry_quality']
#cpd_df = ['check' , 'candle_score']
#mat_df = ['trend[0]', 'trand[1]', 'ma_trend_score']
#mag_df = ['grad[0]', 'grad[1]', 'ma_grad_score']
#RSI_df = ['RSI[-1]' , 'score']

csd_df['entry_qaulity'] = entry_df['entry_quality']
csd_df['candle_pattern_check'] = cpd_df['check']
csd_df['candle_pattern_score'] = cpd_df['candle_score']
csd_df['bb_check'] = bbcs_df['bb_check']
csd_df['bb_score'] = bbcs_df['score']
csd_df['trend_0'] = mat_df['trend_0']
csd_df['trend_1'] = mat_df['trend_1']
csd_df['trend_score'] = mat_df['ma_trend_score']
csd_df['grad_0'] = mag_df['grad_0']
csd_df['grad_1'] = mag_df['grad_1']
csd_df['grad_score'] = mag_df['ma_grad_score']
csd_df['RSI'] = RSI_df['RSI']
csd_df['RSI_score'] = RSI_df['score']

#print(csd_df)

csd_df.to_csv('dataFiles/total_entry_data.csv')

#tunr these off for testing 
#csd_df['date'] = (pd.to_datetime(csd_df['date'],unit='ms'))
#bi_df['date'] = (pd.to_datetime(bi_df['date'],unit='ms'))
#si_df['date'] = (pd.to_datetime(si_df['date'],unit='ms'))

#print(csd_df['date'])
#print(bi_df['date'])

RSI = talib.RSI(csd_df['close'], timeperiod=14)
csd_df['RSI'] = RSI

fig = make_subplots()
fig.add_traces([go.Candlestick(x=csd_df['date'], 
                open=csd_df['open'],
                high=csd_df['high'],
                low=csd_df['low'],
                close=csd_df['close']), 

                go.Scatter(
                x=bi_df['date'],
                y=bi_df['buy_price'],
                line = dict(color="hotpink"),
                name = "Buys",
                mode = 'markers'),

                #go.Scatter(
                #x=csd_df['date'],
                #y=csd_df['RSI'],
                #line = dict(color="hotpink"),
                #name = "RSI"),

                go.Scatter(
                x=si_df['date'],
                y=si_df['sell_price'],
                line = dict(color="yellow"),
                name = "Sell",
                mode = 'markers'),

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
                
                rows = [1,1,1,1,1],
                cols = [1,1,1,1,1])

fig.update_layout(xaxis_rangeslider_visible=False, template='plotly_dark')
fig.update_traces(marker=dict(size=12,
                              line=dict(width=1,
                                        color='DarkSlateGrey')),
                                        selector=dict(mode='markers'))
fig.show()

