import matplotlib.pyplot as plt
import numpy as np
from numpy import *

#@author Yichen Fan


def Q4():
	print "Question Four"
#Creat a grid
	nx,ny = (500,500)
	print "x,y is ",nx,ny
	x = linspace(-2,1,nx)
	y = linspace(-1.5,1.5,ny)
	xv,yv = np.meshgrid(x,y)
	c = xv + 1j*yv

	#Do the Itertaion
	N_max = 50
	some_threshold = 50
	z = c
	for v in range(N_max):
		z = z**2 + c
	#Form a 2-D boolean Mask
	Mask = abs(z)<some_threshold
	#Result to an image
	plt.imshow(Mask,extent = [-2,1,-1.5,1.5])
	plt.gray()
	plt.savefig("Mandelbrot.png")
