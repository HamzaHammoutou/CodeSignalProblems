def phoneCall(min1, min2_10, min11, s):
    if min1 > s:
        return 0
    else:
        minutos1 = 1
        s = s - min1
        
        if (s//min2_10) > 9:
            minutos2 = 9
            s = s - minutos2*min2_10
            
            minutos3 = s//min11
        else:
            minutos2 = s//min2_10
            minutos3 = 0
        return minutos1 + minutos2 + minutos3