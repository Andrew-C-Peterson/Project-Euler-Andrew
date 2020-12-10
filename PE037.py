#Primes that are still primes when you remove numbers
#Example 3797 is a prime, so is 797, 97, and 7
#Going the other way - 379, 37, an 3 are also all primes

import time

start = time.time()

#Check if # is prime
def is_prime(n):
	"""function to check if the number
	is prime or not"""
	for i in range(2,int(abs(n)**0.5)+1):
		if n%i == 0:
			return False
	return True

#Returns prime numbers below n, for this we exclude single digit numbers
def sieve2(n):
	is_prime = [True]*n
	is_prime[0] = False
	is_prime[1] = False
	for i in range(3,int(n**0.5+1),2):
		index = i*2
		while index < n:
			is_prime[index] = False
			index = index+i
	prime = []
	for i in range(11,n,2):
		if is_prime[i] == True:
			prime.append(i)
	return prime
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

primes = sieve2(1000000)
single=[2,3,5,7]
check = single + primes
Trun_Primes=[]
checked=[]

for prime in primes:
    pr_str = str(prime)
    pr_list=list(pr_str)
    l = len(pr_list)
    flag = True
    flag_2=True

    pr_mid = pr_list[1:l-1].copy()
    for i in range(0,len(pr_mid)):
        if int(pr_mid[i]) in [0,2,4,5,6,8]:
            flag_2=False
            break
    if flag_2 == True:
    
        for i in range(0,l-1):
            del pr_list[0]
            pr_tr = int("".join(pr_list))
            if pr_tr not in check:
                flag = False
                break
        if flag == True:
            pr_list=list(pr_str)
            for i in range(0, l-1):
                del pr_list[-1]
                pr_tr = int("".join(pr_list))
                if pr_tr not in check:
                    flag = False
                    break
            if flag == True:
                Trun_Primes.append(prime)
        checked.append(prime)
        
print(sum(Trun_Primes))
print(time.time()-start)