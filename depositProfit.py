import math
def depositProfit(deposit, rate, threshold):
	return math.ceil(math.log(threshold/deposit, 1+rate/100))



print(depositProfit(100,20,170))