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

#ARRAYS TO BE USED IN THE PERFORMANCE BENCHMARK
road_length = []
time_naive = []
time_TD = []
time_BU = []

#CHANGE THIS TO CHANGE THE SIZE OF THE ARRAY
arraysize = 14
#CHANGE THIS TO CHANGE THE NUMBER OF TRIALS
trialnumber = 10
#CHANGE THIS FOR LOOP TO TO CHANGE THE ROAD LENGTHS
for i in range(1,arraysize):
    road_length.append(500 * i)
    time_TD.append(0)
    time_BU.append(0)


end = "NO"

while(end == "NO"):
    for x in range(trialnumber):
        for i in range(0,arraysize-1):
            length = road_length[i]
            road = createRoad(length)

            #naive (UNCOMMENT THIS PART TO MEASURE THE NAIVE ALGORITHM)
            #start = timer()
            #shortPath = minPath(road,length-1,0,1)
            #end = timer()
            #result = end - start
            #print("Naive took:\t" + str(result) + " seconds, and the minPath is:\t" + str(shortPath))
            #time_naive[i] += result

            #Bottom Up
            memo2 = [ [0 for i in range(3)] for j in range(length+1) ]
            memo2[1] = [0,0,0]
            start = timer()
            shortPath = minPathBottomTop(road,length,memo2)
            end = timer()
            result = end - start
            print("BU took:\t" + str(result) + " seconds, and the minPath is:\t" + str(shortPath))
            time_BU[i] += result

            #Top Down
            memo = [ [-1 for i in range(3)] for j in range(length+1) ]
            start = timer()
            shortPath = minPathTopBottom(road,length-1,0,1,memo)
            end = timer()
            result = end-start
            print("TD took:\t" + str(result) + " seconds, and the minPath is:\t" + str(shortPath))
            time_TD[i] += result

    for j in range(0,arraysize-1):
        #time_naive[j] /= trialnumber
        time_BU[j] /= trialnumber
        time_TD[j] /= trialnumber

    #graphthis(road_length,time_naive,"Length of the Road","Running Time Naive")
    graphthis(road_length,time_BU,"Length of the Road","Running Time Bottom-Up")
    graphthis(road_length,time_TD,"Length of the Road","Running Time Top-Down")

    end = input("END?")