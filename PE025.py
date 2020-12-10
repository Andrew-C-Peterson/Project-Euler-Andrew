#Fib Sequence, first with 1000 digits

F=[]
F.append(1)
F.append(1)
i=0

while True:  
    x=F[i]+F[i+1]
    F.append(x)
    digits = [int(y) for y in str(F[i+2])]
    if len(digits)>= 1000:
        break
    i = i+1

print(len(F))