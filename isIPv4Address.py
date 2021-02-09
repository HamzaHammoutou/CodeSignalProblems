def isIPv4Address(inputString):
    numbers = inputString.split(".")
    lista = []
    for n in numbers:
        if (n.isnumeric()):
            if len(n) > 1 and n[0] == "0":
                lista.append(False)
            else:
                lista.append(int(n) >= 0 and int(n) <= 255)
        else:
            lista.append(False)
    return lista





a = "172.16.254.1"


print(isIPv4Address(a))