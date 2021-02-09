def extractEachKth(inputArray, k):
    newList = []
    for i in range(len(inputArray)):
        if not (i+1)%k == 0:
            newList.append(inputArray[i])
    return newList