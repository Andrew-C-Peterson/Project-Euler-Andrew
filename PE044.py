#Pentagonal numbers

import time as time

start = time.time()
i = 1

def is_pent(P):
    if (1+(24*P+1)**0.5) % 6 == 0:
        return True
    return False
    
flag = True
while flag:
    a = i*(3*i-1)/2
    for k in range(1, i):
        b = k*(3*k-1)/2
        
        x = a-b
        y = a+b
        
        if is_pent(x) and is_pent(y):
            print(x)
            flag = False
            break
    
    i+=1
    
print(time.time()-start)