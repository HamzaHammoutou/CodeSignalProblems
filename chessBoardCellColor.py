def getColor (cell1):
    fila1 = cell1[0]
    column1 = cell1[1]
    color1 = 0
    if (int(column1)%2 != 0):
        if (ord(fila1) - ord("A") + 1)%2 != 0:
            color1 = 0
        else:
            color1 = 1
    else:
        if (ord(fila1) - ord("A") + 1)%2 != 0:
            color1 = 1
        else:
            color1 = 0
    return color1
    

def chessBoardCellColor(cell1, cell2):
    fila1 = cell1[0]
    column1 = cell1[1]

    
    fila2 = cell2[0]
    column2 = cell2[1]
    
    return getColor(cell1) == getColor(cell2)
    
    
            

'''
Columna impar:
    fila par: blanca
    fila impar: negra

columna par:
    fila par: negra
    fila impar: blanca
'''