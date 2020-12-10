##I am trying to determine for how many integers (say n), the value of 
##n^i also has i digits.

import time

start = time.time()

#counting the number of such integers
count = 0

# n must be less than 10 based on logic.. 10^i will always have more
#than i digits so only need to check n from 1-9
for n in range(1,10):
    
    #iterate through different values of i, starting at 1 and count up by 1
    i=1
    
    while True:
        exp = n**i
        #Once n^i has less digits than i, it will never become equal to or greater
        #so we can stop the loop and move onto the next n
        if len(str(exp)) != i:
            break
        
        count +=1
        i +=1

print(count)
print(time.time()-start)