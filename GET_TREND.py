from GET_MA import get_MA

def get_trend(all_closes):

    SHORT_MA, LONG_MA = get_MA(all_closes)

    period = [0,1]
    #data_length = [short_period, long_period]
    data_length = [5,50]
    trend_data = [SHORT_MA, LONG_MA]
    trends = []

    for x in period:
        count = 0  
        trend_value = 0
        while count < data_length[x]:
            value = count - data_length[x]
            trend = all_closes[value]/trend_data[x][value]
            if trend > 1:
                trend_value+=(trend-1)
            elif trend <= 1:
                trend_value-=trend
            
            count+=1

        #print(trend_value)

        if trend_value > 0:
            # Up trend
            trends.append(1)
        elif trend_value < 0:
            # Down trend
            trends.append(0)
        else:
            # No trend
            trends.append(2)

    return trends[0], trends[1]