def rotateImage(a):

	b = []
	for i in range(len(a)):
		b.append([])

	for i in range(len(a)):
		for j in range(len(a[i])):
			b[j].insert(0,a[i][j])
    
	return b

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]



print(rotateImage(a))


(7, 4, 1)
(8, 5, 2)
(9, 6, 3)

for i in range(2):
	print(i)