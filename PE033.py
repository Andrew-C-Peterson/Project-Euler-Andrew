#Digit canceling fractions

import time as time

start = time.time()
#These are our digit canceling fractions, should be 4
num=[]
den=[]
for i in range (11,100):
    if i%10 != 0:
        x = str(i)
        for j in range(i,100):
            if j%10 !=0 and i !=j:
                y = str(j)
                
                val = i/j
                
                if x[0] == y[1]:
                    val1 = int(x[1])/int(y[0])
                    if val1 == val:
                        print(i,j,val)

                if x[1] == y[0]:
                    val1 = int(x[0])/int(y[1])
                    if val1 == val:
                        print(i,j,val)
                        num.append(i)
                        den.append(j)

Num = 1
for i in range(0,len(num)):
    Num=Num*num[i]
    
Den = 1
for i in range(0, len(den)):
    Den=Den*den[i]
    
print(Num)
print(Den)

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
    while b:
        a, b = b, a % b
    return a

a = gcd(Num,Den)
print("The product of the fractions is:" )
print(Num/a)
print(Den/a)
print("Total time is: ", time.time()-start)

