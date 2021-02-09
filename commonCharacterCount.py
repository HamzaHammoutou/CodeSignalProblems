import sys


def commonCharacterCount(s1, s2):
    total = 0
    for c in s1:
        if (c in s2):
            total += 1
            s1 = s1.replace(c, "",1)
            s2 = s2.replace(c, "",1)
    return total
        
