import sys

def arrayChange(inputArray):
    moves = 0
    for i in range(1,len(inputArray)):
        if (inputArray[i]<= inputArray[i-1]):
            diff = inputArray[i] - inputArray[i-1]
            moves += abs(diff) + 1
            inputArray[i] += abs(diff) + 1
    return moves


print(arrayChange([1,1,1]))

