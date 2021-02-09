import sys

def addBorder(picture):
    row = ["*"* (len(picture[0])+2)]
    
    for i, r in enumerate(picture):
        picture[i] = "*" + r + "*"
        
    picture.insert(0,row)
    picture.insert(len(picture),row)
    
    return picture

print(addBorder(["abc", "ded"]))