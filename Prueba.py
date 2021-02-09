import sys


def almostIncreasingSequence(sequence):
	lastElement = sequence[0]
	flag = False
	for i in range(1,len(sequence)):
		if sequence[i] < lastElement:
			if flag :
				return False
			flag = True





