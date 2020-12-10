#I want to find the longest list of consecutive primes which sums uo to 
#a prime below 1,000,000

#The answer is the length of this list

import time as time

start = time.time()

#I create a list of primes below 1,000,000
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

#This is the variable for 1,000,000 - I just had this so I could easily
#change the limits to test my script
z = 1000000

#Create my list of primes, the longest list length, and the sum of the longest
#list
primes = sieve(z)
high_len = 0
high_len_sum = 0

#For each prime number in primes
for i in range(0,len(primes)):
    #I set the sum equal to the sum of the list from prime to the length 
    #of the current longest list - we don't care about shorter lists
    prime = primes[i]
    cur_sum=sum(primes[i:i+high_len+1])
    len_sum = high_len+1
    
    #For each following prime, I add it to the sum, check if it is prime, and
    #add one to the length
    for j in range(i+high_len+1,len(primes)):
        cur_sum+=primes[j]
        len_sum+=1
        #If the sum is greater than the limit, we break
        if cur_sum > z:
            break
        #If the sum is a prime, we check if the length is the new longest
        #If so, we update the variables accordingly
        if cur_sum in primes:
            if len_sum > high_len:
                high_len = len_sum
                high_len_sum = cur_sum
    #There's no need to keep checking if we know it can't be the longest
    #This breaks when it is impossible for a new prime to be the start of 
    #a longest list
    highest_start = z/high_len
    if prime > highest_start:
        break
print(high_len)       
print(high_len_sum)
print(time.time()-start)