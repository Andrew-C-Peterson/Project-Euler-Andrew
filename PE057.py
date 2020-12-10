#The sqrt(2) can be represented as an infinite continued fraction
#1 + [1/2] = 3/2, 1 + [(1/2+1/2)] = 7/5, 1+ 1/[2+(1/1+1/2)] = 17/12
#For how many of these iterations, up to 1000, how many have a larger 
#numerator than denominator?

#I found a way to solve this by seperating out the fraction and the 1 out in front
#the x list represents the fraction (numerator and denominator)
#the y list represents the fraction + 1 (again, num and den)

#I found an equation that works for the fraction part of the equation
#the new denominator is 2*previous numerator + previous denominator
#the new numerator is the previous denominator
#I then update the y list [1 + x]
#I then compare the length of the numerator and denominator for y
import time

start = time.time()

#x is the fraction. Each list within the list contains the numerator and denominator
#ie, [1,2] = 1/2
#y is 1 + x, so the first value would be [3,2] = 3/2
#count is the number of times in y where the numerator is larger than the 
#denominator
x = [[1,2]]
y=[]
count = 0


for i in range(0,1000):
    
    #1 + x, as a fraction
    y.append([sum(x[i]),x[i][1]])
    
    #if the length of the numerator is larger than the length of the denominator
    #we add 1 to count
    if len(str(y[i][0])) > len(str(y[i][1])):
        count+=1
    
    #Here is my equation for updating the next values of x
    b = 2*x[i][1]+x[i][0]
    a = x[i][1]
    x.append([a,b])
    
print(count)
print(time.time()-start)
print()


#I just found a new pattern, that I think will be faster (and less code)
#Not gonna bother with any explanation for this one
start_2 = time.time()

z = [[3,2]]
count_2 = 0
for i in range(0,1000-1):
    c = sum(z[i])
    z.append([c+z[i][1],c])
    if len(str(y[i][0])) > len(str(y[i][1])):
        count_2 +=1

print(count_2)
print(time.time()-start_2)
