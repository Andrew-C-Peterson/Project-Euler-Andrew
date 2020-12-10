#Pandigital sums

#Take a number and multiply it by succesive integers starting with 1
#Concanate the sum of these products and determine if it is pandigital
#I want to determine the largest of these

import time as time

start = time.time()

#Storing all the pandigital numbers that I create
pans = []

#This is my set of digits 1-9, which I will check against
check = {'1','2','3','4','5','6','7','8','9'}

#I only need to go up to 4 digit numbers, 5 digit numbers would create
#a length of 10, which is too long
for i in range(1,10000):
    
    #The conconated product. Starts as nothing
    conc = ''
    
    #Integer starts as 1
    j = 1
    
    #While the length is less than 9, increase the integer
    #and conconate the product
    while len(conc) < 9:
        prod = i*j
        conc = conc+str(prod)
        j=j+1
        
    #check if it is pandigital
    if len(conc)==9 and set(conc) == check:
        pans.append(conc)
  
#Find my largest and print it      
print(max(pans)) 
print(time.time()-start)       