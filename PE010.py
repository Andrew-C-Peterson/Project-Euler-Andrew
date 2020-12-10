#Sum primes below 2 million

#Initially, sum = 2+3 = 5
sumprimes=5
i=5

import math

while True:
    flag = 0
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            flag=1
            break
    if flag ==0:
        sumprimes=sumprimes+i
    if i > 2000000:
        break

    
    i = i+2

print(sumprimes)