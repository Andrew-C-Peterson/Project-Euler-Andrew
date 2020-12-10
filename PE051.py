#Project Euler problem 51
#I used quite a bit of help on this one, from RadiusOfCircle.blogspot.com

#I want to find the smallest prime, which when you replace digits with the same
#number contains 8 primes.

#For example - 56**3 yields: 56003, 56113, 56333, 56443, 56663, 56773, 56993
#That is a family of 7, by replacing digits 3+4

from collections import Counter
import time as time

start = time.time()

#Funciton to make a list of primes
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

def pdr(s):
    """take a number and return a list with families
    for example if the input number is 566003 then
    the result will be
    [[566003,566113,566223,566333,566443,566553,566663,566773,566883,566993],
    [500003,511003,522003,533003,544003,555003,566003,577003,588003,599003]]"""
    s = str(s)
    sol = []
    for duplicate in (Counter(s) - Counter(set(s))):
        a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        temp = [int(s.replace(duplicate, x)) for x in a]
        sol.append(temp)
    return sol

def check(l):
    """take a list and remove all the values which are
    not prime numbers, finally return a list with only
    prime numbers"""
    for i in l:
        checked.append(i)
        if i not in primes:
            l.remove(i)
    return l

primes = sieve(1000000)

primes = [x for x in primes if len(str(x)) - len(set(str(x))) >= 3]

# list to store all the checked numbers, so not to repeat
checked = []

# condition for while loop
flag = True

# while loop iterator
i = 0

# while loop
while flag:
    # check if we have not check the number before
    if primes[i] not in checked:
        # find the family of the given number
        replacements = pdr(primes[i])
        for j in replacements:
            if len(check(j)) == 8:
                print(j[0])
                flag = False
                break
    i += 1

# time at the end of program execution
end = time.time()

# total time taken for execution
print (end - start)
