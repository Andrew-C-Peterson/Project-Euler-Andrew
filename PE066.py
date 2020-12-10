import time
start = time.time()

squares = []
num =[]
max_x = 0
max_D = 0

for k in range(0,10000000):
    squares.append(k**2)
    
for D in range(2,1000):
    min_x = 0
    if D not in squares: 
        for j in range(1,len(squares)):
            y2 = squares[j]
            
            x2 = D * y2 + 1
            x = x2**.5
            
            if x%1 == 0:
                min_x = int(x)
                if min_x > max_x:
                    max_x = min_x
                    max_D = D
                break
                
        
        if min_x == 0:
            while True:
                k+=1
                squares.append(k**2)
                y2 = squares[k]
                
                x2 = D * y2 + 1
                x = x2**.5
                if x%1 == 0:
                    min_x = int(x)
                    if min_x > max_x:
                        max_x = min_x
                        max_D = D
                    
                    break
                
print(max_x)
print(max_D)
print(time.time()-start)            