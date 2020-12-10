#Find the first 4 consecutive numbers that have at least 4 distinct prime factors
#Well shoot, this is still slow. A work in progress, I suppose

import time as time

start = time.time()

def PrimeFac(n):
    i=1
    a = set()
    while i<= (n/2)+1:
        k=0
        if(n%i==0):
            j=1
            while(j<=i):
                if(i%j==0):
                    k=k+1
                j=j+1
            if(k==2):
                a.add(i)
                if i > n**.5:
                    break
        i=i+1
    return len(a)

flag = True
i = 2*3*5*7

while flag:
    if PrimeFac(i)==4:
        i+=1
        if PrimeFac(i)==4:
            i+=1
            if PrimeFac(i)==4:
                i+=1
                if PrimeFac(i)==4:
                    print(i-3,i-2, i-1, i)
                    print(time.time()-start)
                    break
    i+=1