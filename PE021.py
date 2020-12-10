#Amicable numbers
import math

#I use pair to store amicable numbers
pair = []
#Iterate through 1 - 10000
for i in range(1,10001):
    #I don't want to count pairs twice, so this skips if i is already in pair
    if i not in pair:
        #Find all the divisors for i (not including i), and then sum them
        a=[]
        for j in range(1,int(math.sqrt(i))+1):
            if i % j == 0 :
                if i/j==j:
                    a.append(j)
                elif j==1:
                    a.append(j)
                else:    
                    a.append(j)
                    a.append(int(i/j))
        totala = sum(a)
        
        #checks if i is an amicable number with it's pair
        k = totala
        b=[]
        if totala != i:
            for j in range(1,int(math.sqrt(k))+1):
                if k % j == 0 :
                    if k/j==j:
                        b.append(j)
                    elif j==1:
                        b.append(j)
                    else:    
                        b.append(j)
                        b.append(int(k/j))
            totalb = sum(b)
            
            if totalb == i:
                print("Amicable numbers: %d, %d" % (i,k))
                pair.append(i)
                pair.append(k)

print("Total sum of amicable numbers is %d" % sum(pair))