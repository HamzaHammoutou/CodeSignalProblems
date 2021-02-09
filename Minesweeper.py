import copy

def minesweeper(matrix):
    #Creating the new matrix
    newMatrix = copy.deepcopy(matrix)
    for i in range(len(newMatrix)):
        for j in range(len(newMatrix[0])):
            newMatrix[i][j] = 0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            
            for ii in range(-1,2):
                for jj in range(-1,2):
                    if 0 <= ii + i < len(matrix) and 0 <= jj + j < len(matrix[0]) and not (ii == 0 and jj == 0):
                        if (matrix[ii + i][jj + j]):
                            newMatrix[i][j] += 1
                        
    return newMatrix


matrix =  [[True, False, False],
          [False, True, False],
          [False, False, False]]

matrix1 = [[True,False,False,True], 
 [False,False,True,False], 
 [True,True,False,True]]


a = range(-1000, 1)

for i in a:
	print(i)
print(a)
