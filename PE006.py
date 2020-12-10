#Sum of squares, square of sums difference

n=100
diff = 0

for i in range(1,n):
    for j in range(i+1,n+1):
               diff = diff + (2*i*j)
    
print(diff)


