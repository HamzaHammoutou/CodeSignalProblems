import sys

def palindromeRearranging(inputString):
    letras = {}
    for c in inputString:
        if c not in letras:
            letras[c] = 1
        else:
            letras[c] += 1
            
    if len(inputString)%2 == 0:
        return all([ letras[c]%2 == 0 for c in letras])
    else:
        return sum([ letras[c]%2 != 0 for c in letras]) == 1