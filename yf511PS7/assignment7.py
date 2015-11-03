#@author Yichen Fan
import matplotlib as plt
import numpy as np
from PS7Q1 import *
from PS7Q2 import *
from PS7Q3 import *
from PS7Q4 import *

def main():
	q1=Question1()
	print "2nd and 4th Rows"
	q1.Q1a()
	print q1.a_array
	print "2nd Colum"
	q1.Q1b()
	print q1.b_array
	print "Coordinates [1,0] to [3,2]"
	q1.Q1c()
	print q1.c_array
	print "Between 3 and 11"
	q1.Q1d()
	print q1.d_array
	Q2()
	Q3()
	Q4()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print "KeyboardInterrupt"
	