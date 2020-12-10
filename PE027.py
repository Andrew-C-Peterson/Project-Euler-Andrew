#Quad formula which produces the largest number of consec. primes

import time


start = time.time()

#sieve of Eratosthenes
#https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
#Finds a list of primes numbers, below the input 'n'

def sieve(n):
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	for i in range(2,int(n**0.5+1)):
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = []
	for i in range(n):
		if is_prime[i] == True:
			prime.append(i)
	return prime


#Is this number a prime? Returns the bool True or False
def is_prime(n):
	"""function to check if the number
	is prime or not"""
	for i in range(2,int(abs(n)**0.5)+1):
		if n%i == 0:
			return False
	return True

#Makes our list of primes under 1000, as well as a copy
primes_1000 = sieve(1000)
primes=primes_1000[:]

#This is our longest list of consecutives primes
high = 0

#cycle through all the primes in the range for both a and b
for b in primes_1000:
    for a in primes_1000:
        i=0
        while True:
            quad = (i**2) + (a*i)+(b)
            #If quad is in primes, we move on. If not we check if it should be
            if quad not in primes:
                #If it is, we add it and move on
                if is_prime(quad):
                    primes.append(quad)
                #If it's not, we see if we have made the longest list
                #If so, we store the length, a, b, and a x b
                else:
                    if i - 1 > high:
                        high = i-1
                        axb=a*b
                        high_a = 1*a
                        high_b =1*b
                    break    
            i+=1
            
        i=0
        #We now must check for a being negative
        #b can't be negative, so we don't need to worry about that
        while True:
            quad = (i**2) - (a*i)+(b)
            if quad not in primes:
                if is_prime(quad) and quad > 0:
                    primes.append(quad)
                else:
                    if i - 1 > high:
                        high = i-1
                        axb=-a*b  
                        high_a = -1*a
                        high_b=1*b
                    break
            i+=1
                               
print(axb)
print(time.time()-start)