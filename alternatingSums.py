import sys

def alternatingSums(a):
    sum1 = sum2 = 0
    for i in range(len(a)):
        if i%2 == 0:
            sum1 += a[i]
        else:
            sum2 += a[i]
    
    return [sum1, sum2]