import sys

def isLucky(n):
    cadena = str(n)
    sum1 = 0
    sum2 = 0
    for i in range(int(len(cadena)/2)):
        sum1 += int(cadena[i])
        
    for i in range(int(len(cadena)/2),len(cadena)):
        sum2 += int(cadena[i])
    return sum1 == sum2

