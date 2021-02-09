import sys


def dfs(graph, start, day, visited=None):
	if visited is None:
		visited = set()
	visited.add(start)
	if daysByCity[start] == -1 or daysByCity[start] > day:
		daysByCity[start] = day
	for next in graph[start] - visited:
		dfs(graph, next, day+1, visited)
	return visited
			
def citiesConquering(n, roads):
    global daysByCity
    daysByCity = [-1] * n
    global neighbords 
    neighbords = {}
    
    for c in range(n):
    	neighbords[c] = set()

    for c1, c2 in roads:
    	neighbords[c1].add(c2)
    	neighbords[c2].add(c1)

    for city in neighbords:
    	if (len(neighbords[city]) <= 1):
    		dfs(neighbords,city,1)

    		print("busqueda por: " + str(city))
    print(neighbords)



roads = [[1, 0], [1, 2], [8, 5], [9, 7], 
         [5, 6], [5, 4], [4, 6], [6, 7]]
n = 10 

citiesConquering(n,roads)

