from graphit import *
from functions import *
from timeit import default_timer as timer
import random

nlist = ['10^4','10^5','10^6','10^7']
alist = []

time_list = []

time = 0.0

for x in range(4,8):
    alist.clear()
    for i in range(1,10**x+1):
        alist.append(i)

    #recursive
    start = timer()
    binarySearchRecursive(alist,1)
    end = timer()
    time = end - start
    time_list.append(time)

print("Recursion List")
print(time_list)

graphthis(nlist,time_list,"# of Elements","Running Time Recursive (sec)")
