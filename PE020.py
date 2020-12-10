#Factorial Digit Sum

x = 100
product=x

for i in range(x-1, 0, -1):
    product=product*i


digits = [int(y) for y in str(product)]

total = sum(digits)

print(total)