#The longest sum of the digits for a^b for a,b < 100 
#I don't know how to do this, other than just brute force

import time

start = time.time()
max_sum = 0
for a in range(1,100):
    for b in range(1,100):
        c = a**b
        c_str = str(c)
        c_sum = 0
        for i in c_str:
            c_sum+=int(i)
        
        if c_sum>max_sum:
            max_sum = c_sum
            
print(max_sum)
print(time.time()-start)
        
