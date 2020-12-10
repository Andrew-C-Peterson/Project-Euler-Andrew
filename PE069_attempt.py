import time
start=time.time()

def gcd(n1,n2):
	remainder = 1
	while remainder != 0:
		remainder = n1%n2
		n1 = n2
		n2 = remainder
	return n1

high_n = 2
high_ratio = 2
    
for n in range(4,1001,2):
    RP=[]
    flag = 1
    count = 0
    threshold = n/high_ratio
    
    for i in range(1,n,2):
        if gcd(n,i)==1:
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