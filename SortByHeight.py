import sys

def sortByHeight(a):
    people = [x for x in a if (x != -1)]
    people.sort()
    j = 0
    for i in range(len(a)):
        if (a[i] != -1):
            a[i] = people[j]
            j += 1
    return a