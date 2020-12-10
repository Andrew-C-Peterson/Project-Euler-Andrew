#Start with 1 in the middle, and create a counter-clockwise spiral of 
#numbers increasing by 1 each time. 

#At what side length is the proportion of digits on the diagnols less than 0.1

import time

#Check if # is prime. I improved the efficiency of this from previous
#versions by checking for 2, and then only checking odd numbers
def is_prime(n):
    if n%2 ==0:
        return False
    for i in range(3,int(abs(n)**0.5)+1,2):
        if n%i == 0:
            return False
    return True


start = time.time()

#I found a pattern for the diagnols. Start with 1, then for the first layer
#add 2 for each diagnol (3,5,7,9). For the next layer, add 4 (13,17,21,25), etc.

#corners is a list where I store each value that is on a diagnol
#prime is the number of primes
#not_prime is the number of not primes
corners = [1]
prime = 0
not_prime = 1
j = 2
while True:
    for i in range(0,4):
        x = corners[-1]+j
        corners.append(x)
        if is_prime(x):
            prime+=1
        else:
            not_prime +=1
    
    j+=2
    if prime/(not_prime+prime) < .1:
        break
    
    
length = j -1

print(length)
print(time.time()-start)
