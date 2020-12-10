#Pandigitial number

#We want a x b = c to be pandigital (1-9 each used exactly once)

#We then want to sum all the products (c) for which this is true

import time as time

start = time.time()


#We don't want duplicates! The set will do this by only recording a value once
products=set()

pan = set('123456789')

#This checks single digit numbers with 4 digit numbers
for i in range(1,10):
    for j in range(1000,10000):
        nums = str(i)+str(j)+str(i*j)
        if len(nums)==9 and set(nums)==pan:
            products.add(i*j)
        elif len(nums)>9:
            break

#This checks two and three digit numbers
for i in range(10,100):
    for j in range(100,1000):
        nums = str(i)+str(j)+str(i*j)
        if len(nums)==9 and set(nums)==pan:
            products.add(i*j)
        elif len(nums)>9:
            break            
        
print(sum(products))

print("Total time was: ", time.time()-start)