
import time as time


start = time.time()


def sieve(n):
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, int(n**0.5+1), 2):
        index = i*2
        while index < n:
            is_prime[index] = False
            index = index+i
    prime = [2]
    for i in range(3, n, 2):
        if is_prime[i]:
            prime.append(i)
    return prime

primes = sieve(1000000)

max_len = 0

max_sum = 0

# max value of the j variable(second for loop)
end_j = int(len(primes)/2)

# two for loops
for i in range(0,len(primes)):
    for j in range(i+max_len+1, end_j):
        sol = sum(primes[i:j])
        if sol < 1000000:
            if sol in primes:
                max_len = j-i
                max_sum = sol
        else:
            end_j = j+1
            break
        
    high_start = 1000000/max_len
    
    if primes[i]>high_start:
        break

print(max_len)       
print(max_sum)
print(time.time()-start)