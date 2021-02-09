import sys

def reverseInParentheses(inputString):
    parentesis = []
    cadena = inputString
    for i,c in enumerate(inputString):
        if c == "(":
            parentesis.append(i)
        elif c == ")":
        	j = parentesis.pop()
        	fragmento = cadena[j:i+1]
        	cadena = cadena.replace(fragmento, fragmento[::-1])
    cadena = cadena.replace("(", "")
    cadena = cadena.replace(")", "")
    return cadena

print(reverseInParentheses("(bar)"))
