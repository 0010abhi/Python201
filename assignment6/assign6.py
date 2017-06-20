import math
import numpy as np
import scipy as sp
import pandas as pd

from pylab import *
import matplotlib as mp

def convertToPolar(co_ord):
    x = co_ord.item((0,0))
    y = co_ord.item((0,1))

    r = math.sqrt(x**2 + y**2)
    degree = math.degrees(math.atan(y/x))
    
    rx = str(r) + "cos(" + str(degree) + ")"
    ry = str(r) + "sin(" + str(degree) + ")"
    return [rx,ry]

##Task1: Convert 10 X 2 Matrix cartesian co-ordinare matrix into polar co-ordinate matrix. 
cartesianArray = np.array([[1,1],[2,2],[-1,-1],[-2,-2],[-1,1],[-2,2],[1,-1],[2,-2],[-1,2],[2,-1]])
cartesianMatrix = np.mat(cartesianArray)
shape = cartesianMatrix.shape
count = 0
polarArray = []
while (count < shape[0]):
    polarCord = convertToPolar(cartesianMatrix[count])
    polarArray.append(polarCord)
    count += 1 

polarMatrix = np.mat(polarArray)
print "Task1: \ncartesian co-ordinare matrix\n",cartesianMatrix,"\ninto polar co-ordinate matrix\n",polarMatrix

##Task2: Create random vector of size 50 and replace the maximum value by 0 and minimum value by 100. 
vectorArray = np.random.random_sample((1,50)) * 10
maxIndex = np.argmax(vectorArray)
minIndex = np.argmin(vectorArray)
print "******\nTask2: original vector array with random values \n",vectorArray
vectorArray[0][maxIndex] = 100
print "max index",maxIndex
vectorArray[0][minIndex] = 0
print "min index",minIndex
print "\n putting max index = 100 & min index = 0", vectorArray

##Task3: Create matrix using scipy. 
Task3Matrix = sp.identity(10) * 2
shape = Task3Matrix.shape
count=0
while(count<shape[0]):
    try:
        if count+2<10:
            Task3Matrix[count][count+2] = 1.0
    except IndexError:
        pass
    try:
        if count-2>=0:
            Task3Matrix[count][count-2] = 1.0
    except IndexError:
        pass
    count +=1

print "****\nTask3: The Desired Matrix Is:\n",Task3Matrix

##Task4: Plot the given graph. 
n = 256
x = np.linspace(-np.pi,np.pi,n,endpoint=True)
y = np.sin(2*x)
plot(x,y+1,color='blue',alpha=1.00)
plot(x,y-1,color='blue',alpha=1.00)
print "****\nTask4: graph generation"
raw_input("press any key to see graph:")
show()
