#Find the first 4 consecutive numbers that have at least 4 distinct prime factors

import time as time

start = time.time()

#Check if # is prime
def prime(n):
    if n % 2 ==0:
        return False
    else:
        for i in range(2,int(abs(n)**0.5)+1):
            if n%i == 0:
                return False
        return True

flag = True
i = 3
primes = [2]

while flag:
    count = 0
    i1_fac = False
    i2_fac = False
    i3_fac = False
    if prime(i):
        primes.append(i)
        i+=1
    else:
        for j in primes:
            if i % j ==0:
                count +=1
        if count >=4:
            i1_fac = True
            if prime(i+1):
                primes.append(i+1)
                i+=1
            else:
                count = 0
                for j in primes:
                    if (i+1) % j ==0:
                        count +=1
                if count >=4:
                    i2_fac=True
                    if prime(i+2):
                        primes.append(i+2)
                        i+=2
                    else:
                        count = 0
                        for j in primes:
                            if (i+2) % j == 0:
                                count+=1
                        if count >=4:
                            i2_fac=True
                            if prime(i+3):
                                primes.append(i+3)
                                i+=3
                            else:
                                count = 0
                                for j in primes:
                                    if (i+3) % j==0:
                                        count+=1
                                if count >=4:
                                    print(i, i+1, i+2,i+3)
                                    print(time.time()-start)
                                    break
        


                
    
