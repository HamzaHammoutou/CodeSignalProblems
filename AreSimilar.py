import sys

def areSimilar(a, b):
    
    dic1 = {}
    dic2 = {}
    
    if len(a) != len(b):
        return False
    
    for i in range(len(a)):
        if (a[i] not in dic1):
            dic1[a[i]] = 1
        else:
            dic1[a[i]] += 1
        
        if (b[i] not in dic2):
            dic2[b[i]] = 1
        else:
            dic2[b[i]] += 1    
    
    for e in dic1:
        if (e not in dic2 or dic1[e] != dic2[e]):
            return False  
              
    numberOfDispar = 0
    for i in range(len(a)):
        if (a[i] != b[i]):
            numberOfDispar += 1
            
            if numberOfDispar > 2:
                return False
    return True
        


a = [1,3,4,2,5,5]
b = [1,2,3,4,5]

print(areSimilar(a,b))
