def arrayMaxConsecutiveSum(inputArray, k):   
    maximo = -1
    actual = 0
    for i in range(len(inputArray)):
        if i > k-1:
            actual = actual + inputArray[i] - inputArray[i-k]
        else:
            actual = actual + inputArray[i]
        
        if actual > maximo:
            maximo = actual

    
    return maximo