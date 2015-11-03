import numpy as np
#@author Yichen Fan

class Question1(object):
	def __init__(self):

		array = np.arange(1,16)#range(start,end),1 to 15, global
		array.resize(3,5)#reshape to five rows three columns
		self.array = array.T
		# a_array = array(a_array)
		# a_array = a_array.reshape((3,5))#reshape to five rows three columns
		# a_array = transpose(a_array)#permute the dimensions of array
		print "A array"
		print array

	# def Q1(): #create array
	# 	global a_array
	# 	a_array = range(1,16) #range(start,end),1 to 15
	# 	a_array = array(a_array)
	# 	a_array = a_array.reshape((3,5))#reshape to five rows three columns 
	# 	a_array = transpose(a_array)#permute the dimensions of array
	# 	print "A array"
	# 	print a_array
	def Q1a(self):#second and fourth rows
		self.a_array = self.array[[1,3],:]
		print
		print "2nd and 4th Rows"
		print self.a_array
		return self.a_array

		
	def Q1b(self):#second column of array
		self.b_array = self.array[:,1]
		print
		print "2nd Colum"
		print self.b_array
		return self.b_array

	def Q1c(self):#rectangular section
		self.c_array = self.array[1:3,0:2]
		print 
		print "Coordinates [1,0] to [3,2]"
		print self.c_array
		return self.c_array

	def Q1d(self):#new array between 3 and 11
		self.d_array = np.logical_and(self.a_array<=11,self.a_array>=3)
		print
		print "Between 3 and 11"
		print self.d_array
		return self.d_array

#printing all answers
# 	print "Question1"

# 	Q1a()
# 	Q1b()
# 	Q1c()
# 	Q1d()

# if __name__ == '__main__':
# 	Q1()






 




















