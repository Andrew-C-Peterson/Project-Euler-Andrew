#Find the smallest cube for which 5 permutations of its digits are cubes

import time

start = time.time()

cubes = []
counts = []
i_val = []

#we'ere given the 345^3 results in 3 permutations which are cube. We will start here.
i = 345

while True:
    #I turn the cube into a list of digits, which is then sorted
    #If the digit list is not in my list storing these lists, I add it
    #I also add to the list storing the counts
    #I also store the value of i
    
    #If the digit list is in the cubes, I add to the index in counts 
    #Once one value of counts is equal to 5 I can break the loop
    cube = sorted(list(str(i**3)))
    if cube in cubes:
        ind = cubes.index(cube)
        counts[ind]+=1
        if counts[ind]>=5:
            break
    else:
        cubes.append(cube)
        counts.append(1)
        i_val.append(i)
    
    i+=1
    
#using the list of i values, I can print i^3 corresponding to the 
#correct counts
print(i_val[ind]**3)
print(time.time()-start)