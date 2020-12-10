#Create a spiral matrix, sum the diagonals
#Must be an odd number for the dimensions, otherwise there is no center

import numpy as np
import time

start = time.time()

#Dimensions of our square
high = 1001

#There has to be a better way to make a matrix of all 0's. Figure this out!
row=[]
matrix=[]
for x in range(1,high+1):
    row.append(0)
for y in range(1,high+1):
        matrix.append(row)
        
#Spiral is going to be my spiral, diag is going to store just the diagonals
#Probably faster to just sum the diagnols as you go, but I wanted to store
#them to check my code
spiral =np.array(matrix)
diag = np.array(matrix)

#We're going to start in the center with the value of 1
x=int((high)/2)
y=int((high)/2)

spiral[x,y]=1
diag[x,y]=1

#k is going to count what value we're on: i.e. 1, 2, 3,...
k=2

#The way I envision this, is we are making larger and larger squares around
#the center. first is 1x1 (which we already did)
#Then a 3x3, then a 5x5, then a n x n. This is how many we need to make
squares = int(len(matrix)/2)

#So this iterates through and makes each of our squares
for i in range(1,squares+1):
    #width is the dimensions of each square, i.e. 3x3, 5x5, nxn
    width=(2*i)+1
    #Move to the right to start our new square and store the counter
    y=y+1
    spiral[x,y]=k
    #If we're on the diaganol, add to the diaganol matrix
    if x == y:
        diag[x,y]=k
    #Increase counter by 1
    k=k+1
    for j in range(1,width-1):
        #Move down to the bottom of the square
        x = x+1
        spiral[x,y]=k
        if x == y:
            diag[x,y]=k
        k=k+1
    for l in range(1,width):
        #Move to the left of the square
        y=y-1
        spiral[x,y]=k
        if x == y+width-1:
            diag[x,y]=k
        k=k+1
    for m in range(1,width):
        #Move to the top of the square
        x=x-1
        spiral[x,y]=k
        if x == y:
            diag[x,y]=k
        k=k+1
    for n in range(1,width):
        #Move to the right and finish the square
        y=y+1
        spiral[x,y]=k
        if x + width -1 == y:
            diag[x,y]=k
        k=k+1
            
end = time.time()
print(sum(sum(diag)))
print(end-start)