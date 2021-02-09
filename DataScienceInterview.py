

# I = 1
# V = 5
# X = 10
# L = 50
# C = 100
# D = 500
# M = 1000
#


def fromDecToRoman(decimal):
	diccionario = {
		1: "I",
		5: "V",
		9: "IX",
		10: "X",
		50: "L",
		90: "XC",
		100: "C",
		500: "D",
		900: "CM",
		1000: "M"
	}
	
	resto = decimal
	numeroRomano = ""

	while (resto != 0):

		for enteroRomano in list(reversed(sorted(diccionario.keys()))):
			veces = 0
			if enteroRomano <= resto:
				veces = int(resto/enteroRomano)
				resto = resto%enteroRomano
				numeroRomano = numeroRomano + diccionario[enteroRomano]*veces
				break

	return numeroRomano


print(fromDecToRoman(298))







