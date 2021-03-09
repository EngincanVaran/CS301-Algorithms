# this code is for graphing
# write this (from graphit import graphthis) for your main code to implement it
# takes parameters x and y values, x-axis and y-axis names and creates a graph

import matplotlib.pyplot as plt

def graphthis(xValues,yValues,xName,yName):
	plt.plot(xValues, yValues, linewidth = "2.0")
	plt.xlabel(xName)
	plt.ylabel(yName)
	plt.show()

def graphthisNoNames(xValues,yValues):
	plt.plot(xValues, yValues, label = "linear")
	plt.show()