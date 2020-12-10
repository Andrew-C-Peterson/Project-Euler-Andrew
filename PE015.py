#grid movement
x=21
y=x+1
grid=[]
for i in range(1,y+1):
    innerlist=[]
    for j in range(1,y+1):
        innerlist.append(0)
    grid.append(innerlist)
    
grid[1][2]=1
grid[2][1]=1
    
i=1  
while i <=x:
    if i < 4:
            j = 4-i
    else:
            j=1
    while j<=i:
        grid[i][j]=grid[i][j-1]+grid[i-1][j]
        grid[j][i]=grid[i][j]
        j=j+1
    i=i+1
    
print(grid[x][x])