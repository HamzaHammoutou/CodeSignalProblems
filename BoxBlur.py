def boxBlur(image):
    newImage = []
    
    for i in range(1,len(image)-1):
        newImage.append([])
        for j in range(1, len(image[0]) -1):
            total = 0
            for ii in range(i-1,i+2):
                for jj in range(j -1, j+2):
                    total += image[ii][jj]
                    
            newImage[i-1].append(total//9)
    return newImage



a = [[1,1,1], [1,7,1], [1,1,1]]

print(boxBlur(a))