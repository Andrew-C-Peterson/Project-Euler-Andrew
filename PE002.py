#sum even number is fibonacci sequence below 4,000,000

maximum = 4000000
x=1
y=2
fib = [1,2]
total= y

while True:
    z=x+y
    if z >= maximum:
        break
    else:
        fib.append(z)
        x=y
        y=z
        if z % 2 == 0:
            total=total+z

print(total)



