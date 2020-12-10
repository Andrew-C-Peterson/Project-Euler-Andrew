#What numbers can be written as the sum of their digits^5

import time

start=time.time()

#This is the highest possible number we can go to
high = 5*(9**5)

#add_up is where I store the numbers that are the sum of there digits^5
#powers is each digit 0-9 to the fifth 
add_up=[]
powers=[]
for i in range(0,10):
    powers.append(i**5)
 
#iterate through from 10 (you can't sum single digits) to the highest
#checks if each number meets the condition
for i in range(10,high+1):
    x=str(i)
    y=0
    for j in range(0,len(x)):
        z = int(x[j])
        y=y+powers[z]
    if y == i:
        add_up.append(i)

#print the sum of add_up as well as the time       
print(sum(add_up))
print(time.time()-start)