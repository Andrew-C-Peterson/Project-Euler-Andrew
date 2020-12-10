#make right triangles out of integers

#then find the perimeter. What value of perimeter has the most triangles?

import time as time
import numpy as np

start = time.time()

#We only want values of p below 1000
#P list is where I count the number of instances for each p value
#k list is where I track the sides and perimeter for each triangle (not needed)
high  = 1000
p_list=[]
k_list =[]

#Start with 0's for all values of p
for i in range(0,high+1):
    p_list.append(0)

#Iterate through the sides of the triangle and find the hypotenuse
for i in range(1,int(high/2)+1):
    for j in range(i,int(high/2)+1):
        k = (i**2+j**2)**.5
        #Check if the perimeter is greater than 1000, if so we break out of the loop
        if i + j+ k > high:
            break
        #For viable p values, we now need to make sure k is an integer
        #If it is, we add 1 to p_list for that value of p
        elif k%1 == 0:
            p = i+j+int(k)
            k_list.append([i,j,int(k),p])
            p_list[p]+=1
 
#Convert to numpy array so we can find the index of the max           
a = np.array(p_list)

print('Max number of p is at: ', np.argmax(a))
print(time.time()-start)