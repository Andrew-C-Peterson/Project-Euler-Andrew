permutations=[]
high=5
for i in range(0,high):
    x=[i]
    for j in range(0,high):
        if j not in x:
            x=[i,j]
            for k in range(0,high):
                if k not in x:
                    x = [i,j,k]
                    for l in range(0,high):
                        if l not in x:
                            x=[i,j,k,l]
                            for m in range(0,high):
                                if m not in x:
                                    x=[i,j,k,l,m]
                                    permutations.append(x)
                            x=[i,j,k,l]
                    x=[i,j,k]
            x=[i,j]