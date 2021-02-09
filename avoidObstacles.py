def avoidObstacles(inputArray):
    for t in range(1,max(inputArray) +2):
        valid = all([ n%t != 0 for n in inputArray])
        if valid == True:
            return t