#functions to be used in MinPath Algorithms
import sys

#recursive TopBottom dynamic programming
def minPathTopBottom(road,end,start,lane,memo):
    if(memo[start][lane] != -1):
        return memo[start][lane]
    else:
        if(end == start):
            if(road[end][lane] == 1):
                return 1
            return 0
        if(road[start][lane] == 1):
            return sys.maxsize
        if(lane == 1):
            memo[start][1] = min( minPathTopBottom(road,end,start+1,1,memo) , 1 + minPathTopBottom(road,end,start+1,0,memo) , 1 + minPathTopBottom(road,end,start+1,2,memo))
            return memo[start][lane]
        elif(lane == 0):
            memo[start][0] = min ( minPathTopBottom(road,end,start+1,0,memo) , ( 1 + minPathTopBottom(road,end,start+1,1,memo) ) )
            return memo[start][0]
        elif(lane == 2):
            memo[start][2] = min ( minPathTopBottom(road,end,start+1,2,memo) , ( 1 + minPathTopBottom(road,end,start+1,1,memo) ) )
            return memo[start][2]
        

#iterative bottomTop dynamic programming
def minPathBottomTop(road,end,memo2):
    x=1
    while(x<end):
        if(x!=1):
            if(road[x][0] != 1):
                memo2[x+1][0] = min( memo2[x][0], memo2[x][1] + 1)
            else:
                memo2[x+1][0] = sys.maxsize
            if(road[x][1] != 1):
               memo2[x+1][1] = min( memo2[x][0]+1, memo2[x][1], memo2[x][2]+1)
            else:
                memo2[x+1][1] = sys.maxsize
            if(road[x][2] != 1):
                memo2[x+1][2] = min( memo2[x][1]+1, memo2[x][2])
            else:
                memo2[x+1][2] = sys.maxsize

        else:
            if(road[x][0] != 1):
                memo2[x+1][0] = 1
            else:
                memo2[x+1][0] = sys.maxsize
            if(road[x][1] != 1):
                memo2[x+1][1] = 0
            else:
                memo2[x+1][1] = sys.maxsize
            if(road[x][2] != 1):
                memo2[x+1][2] = 1
            else:
                memo2[x+1][2] = sys.maxsize
        x+=1
    return min( memo2[end] )


#recursive naive algorithm
def minPath(road,end,start,lane):
    sum=0
    if (end == start):
        return sum
    else:
        if(lane == 1):
            if(road[start+1][1] == 1):
                sum += ( min ( 1 + ( minPath(road,end,start+1,0) ), ( 1 + minPath(road,end,start+1,2) ) ) )
            else:
                if( road[start+1][0] == 1 ):
                    sum += ( min( minPath(road,end,start+1,1) , ( 1 + minPath(road,end,start+1,2) ) ) )
                elif( road[start+1][2] == 1):
                    sum += ( min( minPath(road,end,start+1,1) , ( 1 + minPath(road,end,start+1,0) ) ) )
                else:
                    sum += ( min( minPath(road,end,start+1,1) , ( 1 + minPath(road,end,start+1,0) ) , ( 1 + minPath(road,end,start+1,2) ) ) )
        elif(lane == 0):
            if(road[start+1][0] == 1):
                sum += ( 1 + minPath(road,end,start+1,1) )
            else:
                if(road[start+1][1] == 1):
                    sum += ( minPath(road,end,start+1,0) )
                else:
                    sum += ( min ( minPath(road,end,start+1,0) , ( 1 + minPath(road,end,start+1,1) ) ) )
        else:
            if(road[start+1][2] == 1):
                sum += ( 1 + minPath(road,end,start+1,1) )
            else:
                if(road[start+1][1] == 1):
                    sum += ( minPath(road,end,start+1,2) )
                else:
                    sum += ( min ( minPath(road,end,start+1,2) , ( 1 + minPath(road,end,start+1,1) ) ) )
        return sum