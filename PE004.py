#palindromic numbers


for i in range(99,10,-1):
    for j in range(99,10,-1):
        flag = 1
        x=i*j
        digits = [int(k) for k in str(x)]
        z=len(digits)
        for w in range(1,int((z/2)+1)):
            if digits[w-1] != digits [z-w]:
                flag = 0
                break
        if flag == 1:
            print(i, j, x)
            break
    if flag == 1:
        break


