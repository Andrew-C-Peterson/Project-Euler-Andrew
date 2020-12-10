#Highly divisble triangular number
import math
triangle=[1]
div=[1]
divisors=500
i=2

while True:
    count=0
    triangle.append(triangle[i-2]+i)
    for j in range(1,int(math.sqrt(triangle[i-1]))+1):
        if triangle[i-1] % j ==0:
            count=count+1
    
    count=count*2        
    div.append(count)
    if count > divisors:
        break
    i=i+1
                
print(triangle[i-1])


