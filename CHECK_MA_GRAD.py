from GET_MA_GRAD import get_ma_grad

def check_ma_grad(all_data):

    grad =  get_ma_grad(all_data)
    
    if grad[0] > 0 and grad[1] > 0:
        return 1
    elif grad[0] > 0 or grad[1] > 0:
        return 0.5
    else:
        return 0