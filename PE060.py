#i want to find a set of five numbers, where when any of the two numbers
#are combined (in either order) they make a prime number

#This one was really easy for the difficulty.. I wonder if it's because
#my method isn't that efficient?

import time

start = time.time()

#create list
def sieve(n):
    
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	for i in range(3,int(n**0.5+1),2):
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = [2]
	for i in range(3,n,2):
		if is_prime[i] == True:
			prime.append(i)
	return prime

#Check if # is prime
def is_prime(n):
    if n%2 ==0:
        return False
    for i in range(3,int(abs(n)**0.5)+1,2):
        if n%i == 0:
            return False
    return True

#Check if the two numbers create a prime when combined in either order
def check(a,b):
    if is_prime(int(str(a)+str(b))) and is_prime(int(str(b)+str(a))):
        return True
    else:
        return False
    
#I just had to guess and check here to find the upper limit. 
#Not sure of a better way to do it.
primes = sieve(10000)

flag = False


#Basically I just brute force this, and iterate through each number
#and check.
for i in range(0, len(primes)):
    a = primes[i]
    for j in range(i+1,len(primes)):
        b = primes[j]
        if check(a,b):
            
            for k in range(j+1, len(primes)):
                c = primes[k]
                
                if check(a,c) and check (b,c):
                    for l in range(k+1, len(primes)):
                        d = primes[l]
                        
                        if check(a,d) and check(b,d) and check(c,d):
                            for m in range(l+1,len(primes)):
                                e = primes[m]
                                
                                if check(a,e) and check(b,e) and check(c,e) and check(d,e):
                                    print(a,b,c,d,e)
                                    flag = True
                                    break
                        if flag:
                            break
                if flag:
                    break
        if flag:
            break
    if flag:
        break
    
print(a+b+c+d+e)
print(time.time()-start)