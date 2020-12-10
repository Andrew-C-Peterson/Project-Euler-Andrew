#Find the first 4 consecutive numbers that have at least 4 distinct prime factors


import time as time

start = time.time()

def PrimeFac(n):
    i = 2
    a = set()
    while i < n**.5 or n == 1:
        if n % i == 0:
            n = n/i
            a.add(i)
            i -= 1
        i += 1
    return (len(a)+1)

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
