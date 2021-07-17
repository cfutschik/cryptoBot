import json

def write_portfolios(PORTFOLIO):

    with open('dataFiles/ETHBUSD.txt', 'r+') as f:
        f.seek(0)
        f.truncate()
        f.write(json.dumps(PORTFOLIO[0]))
        
    with open('dataFiles/HolderX.txt','r+') as f:
        f.seek(0)
        f.truncate()
        f.write(json.dumps(PORTFOLIO[0]))