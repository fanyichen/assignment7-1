import numpy as np
#@author Yichen Fan

def Q3():
    #Create 10*3 array of random numbers in range[0,1]
    x = np.random.random((10,3))
    print x

    m = range(10)

    n = np.abs(x-.5).argmin(axis = 1)#column index closest to .5 each row
    
    print 'The closest numbers to .5',x[m,n]
    print 'The column for each of the numbers closest to .5'
    print np.abs(x-.5).argsort(axis=1)[:,0]#with abs and argsort

    print 'Extract numbers by fancy indexing into an array'
    print x[m,n]#fancy indexing