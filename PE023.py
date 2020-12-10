#Abundant Numbers
abundant=[]
doesntsum=[]
import math
high=28123

#Finds the abundant numbers
for i in range(12,high):
    divisors=[]
    for j in range(1,int(math.sqrt((i)))+1):
        if i % j == 0:
            divisors.append(j)
            if j != 1 and j !=i/j:
                divisors.append(int(i/j))
        total=sum(divisors)
    if total > i:
            abundant.append(i)

doesntsum=[]

#Creates a list of all numbers
for i in range(1,high):
    doesntsum.append(i)

#Removes abundant numbers from the list
for i in range(0,len(abundant)):
    for j in range(i,len(abundant)):
        y = abundant[i]+ abundant[j]
        if y < high:
            doesntsum[y-1]=0
        
            
print(sum(doesntsum))
