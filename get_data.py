# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 17:52:54 2019

@author: Dmitry
"""

import pandas as pd
import statistics as stat
import numpy as np
import matplotlib.pyplot as plt

from collections import deque
from bisect import insort, bisect_left
from itertools import islice

def running_median_insort(seq, window_size):
    """Contributed by Peter Otten"""
    seq = iter(seq)
    d = deque()
    s = []
    result = []
    for item in islice(seq, window_size):
        d.append(item)
        insort(s, item)
        result.append(s[len(d)//2])
    m = window_size // 2
    for item in seq:
        old = d.popleft()
        d.append(item)
        del s[bisect_left(s, old)]
        insort(s, item)
        result.append(s[m])
    return result


data = pd.read_csv('AAPL.csv', delimiter=',', header=0)

data.Date =  pd.to_datetime(data.Date)

delta = 5.

num_of_pos = 3


movemed_max = np.array(running_median_insort(np.array(data.High), 10))
movemed_min = np.array(running_median_insort(np.array(data.Low), 10))

shift = np.ones(len(data.High))*delta

movemed_mid = 1/2(movemed_max + movemed_min)

plt.figure()
plt.plot(range(len(data.High)), movemed_max + shift, c='red')
plt.plot(range(len(data.High)), data.Close, c='green')
plt.plot(range(len(data.High)), movemed_min - shift, c='blue')

openShort = []
openLong = []

closeShort = 0
closeLong = 0

for i in range(len(data.High)):
    print(data.Close[i])
    if np.array(data.Close)[i] >= movemed_max[i] + shift[i]:
        openShort.append(1)
    else:
        openShort.append(0)
        
    if np.array(data.Close)[i] <= movemed_min[i] - shift[i]:
        openLong.append(1)
    else: 
        openLong.append(0)
    

for i in range(len(openLong)):
    if openLong[i] == 1 and openShort[i] == 1:
        print('Impossible')
        break
    

print("----------------------------------------")
print(openShort)
print(openLong)

print('----------------------------------------')
print('Sum of short = ', sum(openShort))
print('Sum of long = ', sum(openLong))
