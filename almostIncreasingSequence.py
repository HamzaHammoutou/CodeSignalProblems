import sys


def almostIncreasingSequenceAux(sequence, lastElement):
	for i in range (len(sequence)):
		if sequence[i] <= lastElement:
			return False
		lastElement = sequence[i]
	return True


def almostIncreasingSequence(sequence):
	lastElement = sequence[0]
	for i in range(1,len(sequence)):
		if sequence[i] <= lastElement:

			#Remove the actual element
			if (i + 1 < len(sequence)):
				opcion1 = almostIncreasingSequenceAux(sequence[i+1:], lastElement)
			else:
				opcion1 = True

			#Remove the last element
			if (i-2 >= 0):
				opcion2 = almostIncreasingSequenceAux(sequence[i:], sequence[i-2])
			else:
				opcion2 = almostIncreasingSequenceAux(sequence[i:],sequence[i]-1)
			return opcion1 or opcion2

		else:
			lastElement = sequence[i]

	return True


print(almostIncreasingSequence([1, 2, 3, 4, 99, 5, 6]))


