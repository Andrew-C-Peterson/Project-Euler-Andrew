#Py triplet that sums to 1000
number=1000
x=int(number/3)
y=int(number/2)

import math
flag=0
for a in range(1,x):
    for b in range(a+1,y):
        root = math.sqrt((a**2)+(b**2))
        if int(root)**2 == (a**2)+(b**2):
            c = int(root)
            if a+b+c==number:
                flag = 1
                break
    if flag ==1:
        break

if flag == 1:    
    print(a,b,c)
    print(a*b*c)
else:
    print("No perfect squares summed to this value")
            

        

