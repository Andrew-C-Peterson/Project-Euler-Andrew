#Triangle, pentagonal, and hexagonal numbers

#T285 = P165 = H143 = 40755

#Find the next triangle number that is also a pentagonal and hexagonal number

import time as time

start = time.time()

#Function for determing if # is pentagonal
def is_pent(P):
    if (1+(24*P+1)**0.5) % 6 == 0:
        return True
    return False

#We are going to iterate through hexagonal numbers, since they have the largest
#Step size in between them. So we are starting after H143
i = 144


while True:
    #Find the ith hexagonal number
    hex_num = i*(2*i-1)
    
    #Check if it is also a pentagonal number
    #To note, all hexagonal numbers are triangle numbers so we don't need to check
    if is_pent(hex_num):
        #If it is, print the answer and break the look
        print(hex_num)
        break
    
    
    
    i+=1
    
print(time.time()-start)