import sys


def matrixElementsSum(matrix):
    sum = 0
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
        	if (matrix[i][j] == 0):
        		break
        	sum += matrix[i][j]
    return sum
