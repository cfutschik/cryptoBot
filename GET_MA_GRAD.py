from GET_MA import get_MA

def get_ma_grad(all_closes,all_highs,all_lows,dataperiod):

    ATR = get_ATR(all_closes,all_highs,all_lows,dataperiod)

    avg_ATR = sum(ATR[-50:])/len(ATR[-50:])

    ma_short, ma_long = get_MA(all_closes)
    ma_data = [ma_short, ma_long]
    x = [0, avg_ATR, 2*avg_ATR]
    grad_factor = []

    for i in range(len(ma_data)):
        y = ma_data[i][-4:-1]
        pol = np.polyfit(x, y, 1)
        angle = np.rad2deg(np.arctan(pol[0]))
        grad_factor.append(angle/90)

    return grad_factor