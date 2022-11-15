"""
Created on Wed Mar 30 10:56:29 2022

@author: SHEERAZ MEMON
"""
n=5
for i in range(n): # for i in [0, 1, 2, 3, ... n-1]
    for j in range(i): # for j in [1, 2, 3, ... i-1]
        print ('* ', end="") # Print a star
    print('')

for i in range(n,0,-1): # for i in [n, n-1, n-2, ... 0]
    for j in range(i):  # for j in [1, 2, 3, ... i-1]
        print('* ', end="") # Print a start
    print('')