#Find the pandigital numbers which follow the substring divisibility

#Not my best work - in terms of efficiency - but this one just wasn't that 
#interesting to me

#I basically just make all my permutations and then check the divisibility rules
#I then store each of the pandigital numbers which meet the rules
#And then at the end I sum these up

import time as time
from itertools import permutations

start = time.time()


pans = permutations('0123456789')
pans_div=[]

for i in pans:
     if (int(''.join(i[7:10])) % 17 == 0 and
        int(''.join(i[6:9])) % 13 == 0 and
        int(''.join(i[5:8])) % 11 == 0 and
        int(''.join(i[4:7])) % 7 == 0 and
        int(''.join(i[3:6])) % 5 == 0 and
        int(''.join(i[2:5])) % 3 == 0 and
        int(''.join(i[1:4])) % 2 == 0):
        
        pans_div.append(int(''.join(i)))
        
        
print(sum(pans_div))
print(time.time()-start)