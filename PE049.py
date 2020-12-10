#Find a series of three 4-digit primes which are equally spaced and
#permutations of each other


#Probably not the most efficient solution, but I like it

import time as time

start = time.time()

#We are given one such set of 3 numbers, and told there is only one more
#I set the loop to break when we find 2 sets. These variables help me track that
count = 0
flag = True

#This is the function I've been using to get a list of primes below 'n'
#I modified it to only include 4 digit numbers for this problem
def sieve(n):
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	for i in range(3,int(n**0.5+1),2):
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = []
	for i in range(1001,n,2):
		if is_prime[i] == True:
			prime.append(i)
	return prime

primes = sieve(9999)

#We iterate through each prime
for i in range(0,len(primes)):
    #Check it with each prime after it in the list and calculate the difference
    for j in range(i+1,len(primes)):
        a = set(str(primes[i]))
        b = set(str(primes[j]))
        
        dif = primes[j]-primes[i]
        
        #Potential 3rd number of the list
        c_int = primes[j]+dif
        
        #Only need to do the next steps if the first two are a set
        if a == b:
            #Now, we check if the third potential number in the sequence is prime
            #If it is, we then check that they are all permutations
            if c_int in primes:
                
                c = set(str(c_int))
                
                #If so, we print
                if b == c:
                    print(primes[i],primes[j],c_int)
                    print(str(primes[i])+str(primes[j])+str(c_int))
                    count = count + 1
                    if count == 2:
                        flag = False
                        break
        #If z is greater than 4 digits, no need to keep iterating through the loop
        if c_int > 9999:
            break
    #If we have two sets of numbers, this ends the program
    if flag == False:
        break
    
print(time.time()-start)
    
