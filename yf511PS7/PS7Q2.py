import numpy as np

#@author Yichen Fan
def Q2():
	a = np.arange(0,25).reshape(5,5)#array from 0 to 24 with five rows five columns
	b = np.array([1., 5, 10, 15, 20])
	b = b.reshape(5,1)#reshape to five column
	ab = np.divide(a,b)#a divide b
	print
	print "The result dividing each column in a with the array b"
	print ab
