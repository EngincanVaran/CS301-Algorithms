#functions to be used in MinPath Algorithms
import sys

#recursive TopBottom dynamic programming
FUNCTION minPathTopBottom(road,end,start,lane,memo):
    IF(memo[start][lane] != -1):
        RETURN memo[start][lane]
    ELSE:
        IF(end = start):
            IF(road[end][lane] = 1):
                RETURN 1
            ENDIF
            RETURN 0
        ENDIF
        IF(road[start][lane] = 1):
            RETURN sys.maxsize
        ENDIF
        IF(lane = 1):
            memo[start][1] <- min( minPathTopBottom(road,end,start+1,1,memo) , 1 + minPathTopBottom(road,end,start+1,0,memo) , 1 + minPathTopBottom(road,end,start+1,2,memo))
            RETURN memo[start][lane]
        ELSEIF(lane = 0):
            memo[start][0] <- min ( minPathTopBottom(road,end,start+1,0,memo) , ( 1 + minPathTopBottom(road,end,start+1,1,memo) ) )
            RETURN memo[start][0]
        ELSEIF(lane = 2):
            memo[start][2] <- min ( minPathTopBottom(road,end,start+1,2,memo) , ( 1 + minPathTopBottom(road,end,start+1,1,memo) ) )
            RETURN memo[start][2]
        ENDIF
    ENDIF


#iterative bottomTop dynamic programming
ENDFUNCTION

FUNCTION minPathBottomTop(road,end,memo2):
    x=1
    while(x<end):
        IF(x!=1):
            IF(road[x][0] != 1):
                memo2[x+1][0] <- min( memo2[x][0], memo2[x][1] + 1)
            ELSE:
                memo2[x+1][0] <- sys.maxsize
            ENDIF
            IF(road[x][1] != 1):
               memo2[x+1][1] <- min( memo2[x][0]+1, memo2[x][1], memo2[x][2]+1)
            ELSE:
                memo2[x+1][1] <- sys.maxsize
            ENDIF
            IF(road[x][2] != 1):
                memo2[x+1][2] <- min( memo2[x][1]+1, memo2[x][2])
            ELSE:
                memo2[x+1][2] <- sys.maxsize
            ENDIF
        ELSE:
            IF(road[x][0] != 1):
                memo2[x+1][0] <- 1
            ELSE:
                memo2[x+1][0] <- sys.maxsize
            ENDIF
            IF(road[x][1] != 1):
                memo2[x+1][1] <- 0
            ELSE:
                memo2[x+1][1] <- sys.maxsize
            ENDIF
            IF(road[x][2] != 1):
                memo2[x+1][2] <- 1
            ELSE:
                memo2[x+1][2] <- sys.maxsize
        ENDIF
            ENDIF
        x+=1
    ENDWHILE
    RETURN min( memo2[end] )
ENDFUNCTION

#recursive naive algorithm
FUNCTION minPath(road,end,start,lane):
    sum=0
    IF (end = start):
        RETURN sum
    ELSE:
        IF(lane = 1):
            IF(road[start+1][1] = 1):
                sum += ( min ( 1 + ( minPath(road,end,start+1,0) ), ( 1 + minPath(road,end,start+1,2) ) ) )
            ELSE:
                IF( road[start+1][0] = 1 ):
                    sum += ( min( minPath(road,end,start+1,1) , ( 1 + minPath(road,end,start+1,2) ) ) )
                ELSEIF( road[start+1][2] = 1):
                    sum += ( min( minPath(road,end,start+1,1) , ( 1 + minPath(road,end,start+1,0) ) ) )
                ELSE:
                    sum += ( min( minPath(road,end,start+1,1) , ( 1 + minPath(road,end,start+1,0) ) , ( 1 + minPath(road,end,start+1,2) ) ) )
            ENDIF
        ENDIF
        ELSEIF(lane = 0):
            IF(road[start+1][0] = 1):
                sum += ( 1 + minPath(road,end,start+1,1) )
            ELSE:
                IF(road[start+1][1] = 1):
                    sum += ( minPath(road,end,start+1,0) )
                ELSE:
                    sum += ( min ( minPath(road,end,start+1,0) , ( 1 + minPath(road,end,start+1,1) ) ) )
                ENDIF
            ENDIF
        ELSE:
            IF(road[start+1][2] = 1):
                sum += ( 1 + minPath(road,end,start+1,1) )
            ELSE:
                IF(road[start+1][1] = 1):
                    sum += ( minPath(road,end,start+1,2) )
                ELSE:
                    sum += ( min ( minPath(road,end,start+1,2) , ( 1 + minPath(road,end,start+1,1) ) ) )
                ENDIF
            ENDIF
        ENDIF
        RETURN sum
ENDFUNCTION
