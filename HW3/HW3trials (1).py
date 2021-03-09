import random
from functions import *
from timeit import default_timer as timer
from graphit import *

sys.setrecursionlimit(sys.maxsize)

def createRoad(n):
    temp = [ [ 0 for i in range(3) ] for j in range(n) ]
    for i in range (n-1):
        chance = random.randint(0,5)
        if(chance > 0):
            randomNumber = random.randint(0,2)
            temp[i+1][randomNumber] = 1
    return temp

def printRoad(m,n):
    for i in range(n):
        print(m[i])

    
length = int(input("Please enter the length for dynamic programming (>0): "))
length2 = int( input("Please enter the length for naive (>0): ") )
road = createRoad(length)
road2 = createRoad(length2)

#printRoad(road2,length2)

#recursive naive algorithm
start = timer()
shortPath = minPath(road2,length2-1,0,1)
end = timer()
result = end - start
print("MinPath is " + str(shortPath) + " and it takes " + str(result) + " seconds")

#iterative bottomtop dynamic programming
memo2 = [ [0 for i in range(3)] for j in range(length+1) ]
memo2[1] = [0,0,0]
start = timer()
shortPath = minPathBottomTop(road,length,memo2)
end = timer()
result = end - start
print("MinPathBottomTop is " + str(shortPath) + " and it takes " + str(result) + " seconds")

#recursive topbottom dynamic programming
memo = [ [-1 for i in range(3)] for j in range(length+1) ]
start = timer()
shortPath = minPathTopBottom(road,length-1,0,1,memo)
end = timer()
result = end-start

print("minPathTopBottom is " + str(shortPath) + " and it takes " + str(result) + " seconds")


end = input("END?")
