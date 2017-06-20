# -*- coding: utf-8 -*-
import math
import numpy as np
import pandas as pd
import scipy as sp
from pylab import *
import matplotlib.pyplot as plt

# colsToLoad = ['D', 'O', 'H', 'L', 'C', 'V', 'AC', 'CH']
# data = pd.read_csv('D:\\Python201\\Python201\\assignment7\\ARVIND.NS.csv', index_col='Date', parse_dates=True)
# print data
# data['Change'] = data.Open - data.Close
# print data.head()
data = pd.read_csv('D:\\Python201\\Python201\\assignment7\\ARVIND.NS.csv',index_col='Date', parse_dates=True)
# print data
data['Change'] = data.Open - data.Close
print data.head()
close_px = data['Adj Close']
mavg = pd.rolling_mean(close_px, 40)
print mavg[-10:]
close_px.plot(label='ARVIND')
mavg.plot(label='mavg')
# plt.legend()
show()

# DF = pd.DataFrame(data)
# DF.drop(DF.index[0:11], inplace=True)
# print data[1].CH

##Task1: Calculate change Iterate and assign the change.
# itr = DF.iterrows()
# count = 0
# for data in itr:
#     if count<1:
#         count +=1
#         continue
    
#     data[1].CH = float(data[1].C) - float(data[1].O)
#     DF.set_value(count, 'CH', data[1].CH)
#     xAxis.append(data[1].AC)
#     yAxis.append(data[1].D)
#     count +=1   
# print "Task1: DataFrame Created is: \n",DF
# print "*******************************\n"


##Task2: Calculate the “moving average” using Adj Close column. Hint Using rolling_mean
# x = pd.rolling_mean(DF['AC'],10, min_periods=None, freq=None, center=False, how=None)
# print x

##Task3: Create matrix using scipy. 

# mp.plot(xAxis,yAxis)
# pyplot(xAxis,yAxis)
# plot(x,y-1,color='blue',alpha=1.00)
# print "****\nTask4: graph generation"
# raw_input("press any key to see graph:")
# show()

# DF.plot()
# show()