def alphabeticShift(inputString):
    newString = ""
    
    for c in inputString:
        newString = newString + (chr((( ord(c) - ord('a')) + 1)%26 + ord('a')))
    return newString

