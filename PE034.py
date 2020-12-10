#Find numbers for which the sum of the factorials of the digits equals
#the number
#Then sum all these numbers

import time
from math import factorial

start = time.time()

f=[]
for i in range(0,10):
    f.append(factorial(i)) 

def sum_fac(x):
    y = str(x)
    s=0
    for i in y:
        s = s + f[int(i)]
    return s

fun_nums = []
for i in range(10,1854721):
    if sum_fac(i)==i:
        fun_nums.append(i)


print(sum(fun_nums))
print('Time to run: ',time.time()-start)

