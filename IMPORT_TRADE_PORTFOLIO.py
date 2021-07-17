# importing the module
import json
def import_trade_portfolio():
    # reading the data from the file
    with open('dataFiles/ETHBUSD.txt') as f:
        data1 = json.loads(f.read())
        
    with open('dataFiles/HolderX.txt') as f:
        data2 = json.loads(f.read())

    PORTFOLIO = [data1, data2] 

    return PORTFOLIO


