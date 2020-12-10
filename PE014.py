#CollatzNumbers
starting=[]
lengths2=[]
collatz=[]
maxlength=1
for i in range(1,1000001):
    n=i
    length=1
    numbers=[n]
    while n != 1:
        if n < i:
            length=length+lengths2[int(n-1)]-1
            break
        else:
            if n%2 !=0:
                n=(3*n)+1
            else:
                n=n/2
            length=length+1
            numbers.append(n)
            if n == 1:
                break
    starting.append(i)
    lengths2.append(length)
    collatz.append(numbers)
    if length > maxlength:
        maxlength=length
        start=(i)
    
print(maxlength)
print(start)

