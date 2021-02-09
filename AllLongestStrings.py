import sys

def allLongestStrings(inputArray):
	length = [ len(s)  for s in inputArray]
	longestString = max(length)
	return [s  for s in inputArray  if len(s) == longestString]



print(allLongestStrings(["aba", "aa", "ad", "vcd","aba"]))
