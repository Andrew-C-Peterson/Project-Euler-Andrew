#Smallest multiple

n=20;
m=n*(n-1)

while True:
    flag = 0
    for i in range(n-1,0,-1):
        if m % i != 0:
            flag = 1
            break
    if flag == 0:
        print(m)
        break
    else:
        m=m+n


