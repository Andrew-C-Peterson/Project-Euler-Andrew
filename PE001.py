#multiples of 3 and 5, below 1000, summed

x=1000
z=[]

for i in range(1,x):
    if i % 3 ==0:
        z.append(i)
    elif i % 5 ==0:
        z.append(i)
        
total = sum(z)
print(total)

