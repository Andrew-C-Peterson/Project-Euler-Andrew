#maximum sum moving through triangle

import time

start = time.time()

#Open the file, and read it in as a string
file = open("pe067_triangle.txt")
number = file.read()

#split this into a list of lists
number = number.strip().split('\n')
for i in range(1,len(number)):
	number[i] = number[i].strip().split(' ')
	number[i] = [int(x) for x in number[i]]
number[0]=59

h = len(number)

#starting from the bottom, find the maximum value for each possible move and stores this
for i in range(h-1,1,-1):
    for j in range(0,len(number[i])-1):
        a = number[i][j]
        b = number[i][j+1]
        if a>=b:
            number[i-1][j]=number[i-1][j]+a
        else:
            number[i-1][j]=number[i-1][j]+b
 
#Add the 'top' of the triangle to the maximum of the two paths left, and print      
print(max(number[1])+number[0])
print(time.time()-start)
