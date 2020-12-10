#Goldbach proposed that every odd composite number could be written as 
#a sum of a prime and twice a square
#Find the first number which proves this wrong


#Check if # is prime
def is_prime(n):
	"""function to check if the number
	is prime or not"""
	for i in range(2,int(abs(n)**0.5)+1):
		if n%i == 0:
			return False
	return True

import time as time

start = time.time()

#Start at num =3, start a list of primes, and also a flag to see when we
#need to break the while loop
num = 3
primes=[2]
flag=True

while flag:
    #If the number is prime, add it to the list of primes and move to next odd
    if is_prime(num):
        primes.append(num)
        num+=2
    #If the number is not prime, I set the flag to False
    #I then iterate through the primes, and see if there is an integer
    #which satisfies the conjecture
    #If it is satisied, the flag is set back to True and the for loop breaks
    else:
        flag = False
        for i in primes:
            if ((num-i)/2)**.5 % 1 == 0:
                num+=2
                flag=True
                break
    
print(num)
print(time.time()-start)