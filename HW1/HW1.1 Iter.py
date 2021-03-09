from graphit import *
from functions import *
from timeit import default_timer as timer
import random
import statistics

nlist = ['10^4','10^5','10^6','10^7']
alist = []

avg_list = []

total_time_list = []

time = 0.0

avg_time = 0.0

std = 0.0

key = 50

for x in range(4,8):
    for i in range(1,10**x):
        a = random.randint(1,10**8)
        alist.append(a)
    alist.sort()

    for k in range(0,key):
        item = random.randint(1,10**8)

        start = timer()
        binarySearchIterative(alist,item)
        end = timer()
        time = end - start
        total_time_list.append(time)
    
    avg_time = sum(total_time_list) / key

    avg_list.append(avg_time)
    
    std = statistics.stdev(total_time_list)
    
    print("*************************************************************")
    print("Average Iteration Time: " + str(avg_time) + " SD: " + str(std))

    alist.clear()
    
graphthis(nlist,avg_list,"# of Elements","Running Time Iterative (sec)")
