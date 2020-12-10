#Triangle numbers are 1/2*n(n+1). I want to find the score of words in a txt
#file (a = 1, b= 2, ..) where the total score is a triangle number
#I just want to find the total number of triangle numbers in this txt file
#I converted the txt file to csv using excel, to make it easier

import pandas as pd
import time as time

start = time.time()

#Make a list of triangle numbers.
triangle=[]
for i in range(0,100):
    triangle.append(int(.5*i*(i+1)))
 
#Import the text file of names, convert to list
df = pd.read_csv('p042_words.csv', header = None)
names = df.to_numpy().tolist()
names = names[0]

#Initialize the total as 0
total = 0

#Loop through each word in list
#When writing the program, I forgot that each item was just a word
#Not a name. So that's why I called them name instead of word. oops.
for j in range(0, len(names)):
    #The word 'true' was in here. Python saw that as a bool, which
    #was confusing. Eventually figured it out. I just convert all words
    #to strings as it loops through to solve that. Probably a better way tho
    name = str(names[j])
    #word score for each word starts as o
    score = 0
    #assign the score for each letter
    for i in range(0,len(name)):
        x = int(ord(name[i]))-64
        score = score + x
    #If the total score is a triangle number, increase the total by 1
    if score in triangle:
        total +=1
        
print(total)
print(time.time()-start)


