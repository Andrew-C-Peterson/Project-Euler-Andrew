#finds how many distinct integers there are in a^b for a and b = 2 to high

high = 100
numbers=[]

for a in range(2,high+1):
    for b in range(2, high+1):
        x = a**b
        if x not in numbers:
            numbers.append(x)

numbers.sort()
print(len(numbers))