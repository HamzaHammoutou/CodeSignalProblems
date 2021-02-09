def isConnected(s1,s2):
	diferencias = 0
	for i in range(len(s1)):
		if s1[i] != s2[i]:
			diferencias += 1
	return diferencias == 1


def findNext(diccionario, cadenaActual,cadenasRestantes):
	sol = []
	for cadena in diccionario[cadenaActual]:
		if cadena in cadenasRestantes:
			nuevaRestantes = cadenasRestantes.copy()
			nuevaRestantes.remove(cadena)
			sol.append(findNext(diccionario,cadena, nuevaRestantes))

	if not cadenasRestantes:
		return True
	elif not sol and cadenasRestantes:
		return False
	else:
		return any(sol)
        
def stringsRearrangement(inputArray):
    conections = {}

    for i in range(len(inputArray)):
        conections[inputArray[i]] = []
        for j in range(len(inputArray)):
            if i!=j and isConnected(inputArray[i], inputArray[j]):
                conections[inputArray[i]].append(inputArray[j])
    sol = []
    for ca in inputArray:
    	aux = inputArray.copy()
    	aux.remove(ca)
    	sol.append(findNext(conections, ca, aux))

    if not sol:
    	return True
    else:
    	return any(sol)


print(stringsRearrangement(["aaaa", "aaab", "aabb", "abbb", "abab", "baab"]))