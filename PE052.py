
#Find the smallest number 'x', where 2*x, 3*x, 4*x, 5*x, 6*x
#All have the same digits (but in a different order, obviously)

import time as time

start = time.time()

#Funciton that makes a list that contains the number of each digit
#ie, the 0 index contains the # of 0's, the 1 index contains the # of 1's, etc.

#It would have been easier to just make a set here, but I was worried 
#That would not account for numbers with multiples of digits
#E.g. The set of 2556 and 2665 are both {'2','5','6'} but 2556 and 2665 
#do not have the same digits.. I'm working through a more efficient way 
#of solving this problem, but for now I use this function
def dig_list(n):
    digits=[]
    for i in range(0,10):
        digits.append(0)
    for i in str(n):
        digits[int(i)]+=1
    return digits
    
#A single digit number can't possibly solve this, so starting at 2 digits    
x = 10

#z is my variable for how many multiples we need, we want up to 6*x
z = 6

while True:
    x_digits = dig_list(x)
    
    #This counts how many multiples we make it to
    count = 1
    
    #Iterates through each multiple up to z
    #If the digit lists are different, we break the loop
    #If they are the same, we add 1 to the counter
    for i in range(2,z+1):
        if x_digits != dig_list(i*x):
            break
        else:
            count+=1
    
    #If the counter has made it to 'z' we have reach a number which
    #satisfies the condition. So we break the while loop
    if count == z:
        break
    
    x +=1

#Prints out the numbers from x through z*x, as well as the time
for i in range(1,z+1):
    print(i*x)
    
print(time.time()-start)