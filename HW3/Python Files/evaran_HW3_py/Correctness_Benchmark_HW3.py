import random

#returns a road with only Zeroes (0)
def Benchmark_0(n):
    temp = [ [ 0 for i in range(3) ] for j in range(n) ]
    return temp

#return a road with length 1
def Benchmark_1():
	temp = [ [ 0 for i in range(3) ] for j in range(1) ]
	return temp

#return a road with blocked column
def Benchmark_2(n,lane):
	temp = [ [ 0 for i in range(3) ] for j in range(n) ]
	for i in range(n-1):
		temp[i+1][lane] = 1
	return temp

#returns a diagonal blocked road
def Benchmark_3(n):
	temp = [ [ 0 for i in range(3) ] for j in range(n) ]
	j=0
	for i in range(n-1):
		temp[i+1][j] = 1
		j += 1
		j = j % 3
	return temp

#return a triangle like obstacles
def Benchmark_4(n):
	temp = [ [ 0 for i in range(3) ] for j in range(n) ]
	i = 0
	j = 0
	k = 0
	while(i<n-1):
		temp[i+1][j] = 1
		i+=1
		if( k%4 == 0):
			j+=1
		elif( k%4 == 1):
			j+=1
		elif( k%4 == 2):
			j-=1
		else:
			j-=1
		k+=1
	return temp
