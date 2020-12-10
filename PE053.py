#I want to find the number of combinations of nCr from n = 1 to 100 
#where the result is greater than 1,000,000

import time as time
import operator as op
from functools import reduce


#I found this function online for an efficient way of finding combinations
#Apparently, in Python 3.8 there is a math func for this, but I'm running 3.7
def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return int(numer / denom)

start = time.time()

#Counting the number of selections which yield over 1,000,000 combinations
count = 0

#For n from 1 to 100
for n in range(1,101):
    
    #Here I store the maximum r value and the minumum r value which
    #have over 1,000,000 combinations for each n value.
    #Both start at 0
    max_r = 0
    min_r = 0
    
    #Loops backward through r, stores when we go over 1 million, and breaks
    for r in range(n-1, 0, -1):
        if ncr(n,r) > 1000000:
            max_r = r
            break
        
    #If we never went over 1 million, no need to perform this next step
    if max_r != 0:    
        
        #Loops forward through r, stores when we go over 1 million, and breaks
        for r in range(1, max_r):
            if ncr(n,r) > 1000000:
                min_r = r
                break
            
        #Every value for r between the max and min of r will be over 1,000,000
        #So we add all of these to the counting variable
        count += max_r - min_r + 1
        
print(count)
print(time.time()-start)


#A brute force method is shown below to compare times
#For these parameters, the above method is ~ 10x faster


start = time.time()

count = 0

for n in range(1,101):
    for r in range(1,n):
        if ncr(n,r)>1000000:
            count +=1
 
print(count)
print(time.time()-start)           