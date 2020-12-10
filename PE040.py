#Create a fraction which is 0. 1 2 3 4 5 6 7 8 9 10 11 12 ....
#I want to take the 1st digit(1) time the 10th, 100, 1000, 10000, 100000, 1000000
#and multiply them all together

#Initialize the time
import time as time
start = time.time()

#Begin my fraction. Only including numbers after the decimal
#This will be a string, to make it easier to add numbers after
frac = ''
i=1

#Maximum number of digits needed in fraction
digits = 1000000

#Loop through until the needed length is reached
#Add 'i' to the end of the fraction string and then increment i
while len(frac)<digits+1:
    frac += str(i)
    i+=1

#This is just for making the indices I want to find the product of into a list
j=[1]
for i in range(1,7):
    j.append(j[i-1]*10)
  
#Initialize product as 1
product = 1

#Takes the product of each decimal digit that I want
for i in range(0,len(j)):
    product = product * int(frac[j[i]-1])
    
print(product)
print(time.time()-start)