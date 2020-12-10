#Finds largest prime factor
import math

prime = 600851475143
factors = []
primefactors = []


for i in range(2,int(math.sqrt(prime))):
    y=""
    if prime % i == 0:
        factors.append(i)
        for j in range(2,i):
            if i % j ==0:
                y="Not prime"
                break
            if j == i-1:
                primefactors.append(i)
        
    

