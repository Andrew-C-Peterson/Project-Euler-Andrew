#The largest pandigital prime
#Where a pandigital number has the numbers 1-n exactly once
#and n is the length of the number

import time as time
from itertools import permutations


start = time.time()

#Check if # is prime
def is_prime(n):
	"""function to check if the number
	is prime or not"""
	for i in range(2,int(abs(n)**0.5)+1):
		if n%i == 0:
			return False
	return True

#A nine digit number is the largest possible pandigital
a ='123456789'
#This flags when we have found the largest prime, and stops the loop
flag = 1

#Iterate from 9 digit pandigital all the way down to 1 digit 
for i in range(len(a)-1,-1,-1):
    #This creates a list of our pandigital numbers for each length
    #This is ordered large to small
    p = list(permutations(a[:i]))[::-1]
    #For each permutation
    for j in p:
        #If it's not even, lets turn the string into an integer
        #If it is even, we know it's not prime
        if int(j[i-1]) % 2 != 0:
            x = int("".join(j))
            
            #Check if it's prime. If it is we print it, flag it, and break
            if is_prime(x):
                flag = 0
                print(x)
                break
    #Broke out of one loop, but still need to break out of the initial loop
    if flag == 0:
        break
    
print(time.time()-start)