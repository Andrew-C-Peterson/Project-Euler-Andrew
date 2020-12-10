#Circular primes
#prime numbers that are primes for every ordering of digits

#Return primes below n
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

#Check if # is prime
def is_prime(n):
	"""function to check if the number
	is prime or not"""
	for i in range(2,int(abs(n)**0.5)+1):
		if n%i == 0:
			return False
	return True

x=sieve(1000000)
         
z = []      
for i in x: 
    number = i
    for j in range(0,len(str(i))):
        flag = True
        number = (number%10)*10**(len(str(i))-1)+number//10
        if is_prime(number)==False:
            flag = False
            break
    if flag == True:
        z.append(i)
    
print(len(z))