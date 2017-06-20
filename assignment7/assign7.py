import numpy as np
import pandas as pd
import scipy as sp
from pylab import *
import matplotlib.pyplot as plt

data = pd.read_csv('D:\\Python201\\Python201\\assignment7\\ARVIND.NS.csv',index_col='Date', parse_dates=True)
data['Change'] = data.Open - data.Close
print "Task 1:\n",data.head()

close_px = data['Adj Close']
mavg = pd.rolling_mean(close_px, 40)
print "\n***\nTask 2:\n",mavg[-10:]

close_px.plot(label='ARVIND')
mavg.plot(label='mavg')
raw_input("\n***\nTask 3: press any key to see plot\n")
show()