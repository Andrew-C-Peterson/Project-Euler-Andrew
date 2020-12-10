import itertools
import time 

start = time.time()

# 4 digit numbers
tria = [int(n*(n+1)/2) for n in range(45, 141)]
squa = [int(pow(n, 2)) for n in range(32, 100)]
pent = [int(n*(3*n-1)/2) for n in range(26, 82)]
hexa = [int(n*(2*n-1)) for n in range(23, 71)]
hept = [int(n*(5*n-3)/2) for n in range(21, 64)]
octa = [int(n*(3*n-2)) for n in range(19, 59)]
    
def is_cyclical(n, m):
    if (n%100 == int(m/100)):
        return True
    else:
        return False
    
def find_cyclicals(haystack, needle):
    cyclicals = []
    for item in haystack:
        if is_cyclical(needle, item):
            cyclicals.append(item)
    return cyclicals

permutations = list(itertools.permutations(range(0, 5+1)))
shapes = [tria, squa, pent, hexa, hept, octa]
cyclical_groups = []
for perm_list in permutations:
    
    if perm_list[0] != 0:
        break
    
    root = shapes[perm_list[0]]
    for item in root:
        for number in find_cyclicals(shapes[perm_list[1]], item):
                
                for n2 in find_cyclicals(shapes[perm_list[2]],number):
                   
                    for n3 in find_cyclicals(shapes[perm_list[3]], n2):
                        
                        for n4 in find_cyclicals(shapes[perm_list[4]], n3):
                            
                            for n5 in find_cyclicals(shapes[perm_list[5]], n4):
                                
                                if is_cyclical(n5, item):
                                    cyclical_groups.append([item, number, n2,n3,n4,n5]) 

for i in range(0, len(cyclical_groups)):
    print(sum(cyclical_groups[i]))
    print(cyclical_groups[i])
    
print(time.time()-start)
    
    