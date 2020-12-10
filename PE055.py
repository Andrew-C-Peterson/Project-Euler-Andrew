#For this problem, I want to find the non-Lychrel numbers below 10,000

import time

start = time.time()

#Determines if the integer num is a palindrome
def is_pal(num):
    n = str(num)
    if len(n)==1:
        return False 
    for k in range(0, int(len(n)/2)):
        if n[k]!=n[len(n)-k-1]:
            return False
    return True
        
not_lychrel = []
lychrel = []
j = 1
for n in range(1,10000):
    j = n
    
    count = 0
    while count <= 50:
        n_str = str(n)
        r=[]
        for i in range(len(n_str)-1,-1,-1):
            r.append(n_str[i])
        
        n_rev = int("".join(r))   
        n_new = n+n_rev
        if n_new in not_lychrel:
            break
        if is_pal(n_new):
            not_lychrel.append(n_new)
            break
        else:
            n = n_new
        
        count+=1
    if count >=50:
        lychrel.append(j)
        
print(len(lychrel))
print(time.time()-start)