import time
start=time.time()

def ReP(n1,n2):
    i = 2
    while i < n1:
        if n1%i ==0 and n2%i ==0:
            return False
        i+=1
    return True

high_n = 2
high_ratio = 2
    
for n in range(4,1001,2):
    RP=[]
    flag = 1
    count = 0
    threshold = n/high_ratio
    
    for i in range(1,n,2):
        if ReP(n,i):
            count+=1
            if count > threshold:
                flag = 0
                break
            RP.append(i)
     
    if flag ==1:
        phi = len(RP)
        ratio = n/phi
    
        if ratio > high_ratio:
            high_ratio = ratio
            high_n = n
        
print(high_n, high_ratio)        
print(time.time()-start)