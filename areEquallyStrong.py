def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    strongest = max([yourLeft, yourRight])
    weakest = min([yourLeft, yourRight])
    
    return strongest == max([friendsLeft,friendsRight]) and weakest == min([friendsLeft,friendsRight])



   