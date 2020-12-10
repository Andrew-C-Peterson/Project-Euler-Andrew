import time as time

start = time.time()

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

z = 1000000

primes = sieve(z)
high_len = 0
high_len_sum = 0

for i in range(0,len(primes)):
    prime = primes[i]
    cur_sum=sum(primes[i:i+high_len+1])
    len_sum = high_len+1
    for j in range(i+high_len+1,len(primes)):
        cur_sum+=primes[j]
        len_sum+=1
        if cur_sum > z:
            break
        if cur_sum in primes:
            if len_sum > high_len:
                high_len = len_sum
                high_len_sum = cur_sum
    highest_start = z/high_len
    if prime > highest_start:
        break
print(high_len)       
print(high_len_sum)
print(time.time()-start)