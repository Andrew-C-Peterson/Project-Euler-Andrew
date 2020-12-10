#10,001th prime number

n =10001
i=5
count=2

import math

while True:
    flag = 0
    for j in range(2,int(math.sqrt(i))+1):
        if i % j == 0:
            flag=1
            break
    if flag ==0:
        count=count+1
        print(i)
    if count == n:
        break

    
    i = i+2
    