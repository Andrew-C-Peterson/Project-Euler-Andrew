#Finds all numbers that are palindromes in base 10 and binary and sums
#My first attempt was pretty messy, so  I tried it again
#And then compare the run times
import time


start = time.time()

#Here is where I store my palindromes, binary palindromes, and then both
#This is not necessary, but it helps me check that my code is working
#Removing these would make code run faster
palindromes =[]
pal_bin=[]
both=[]

#I have to check all the single digit numbers by themself
for i in range(1,10):
    i_bin = bin(i)[2:].zfill(20)
    i_bin_str = str(i_bin)
    i_bin_list = list(i_bin_str)
    for j in range(0,len(i_bin_list)):
        if i_bin_list[j]==0:
            i_bin_list.remove("0")
        else:
            break
    i_bin_1 = int("".join(i_bin_list))
    pal_bin.append(i_bin_1)
    z=str(i_bin_1)
    zz=list(z)
    flag = True
    for k in range(0, int(len(zz)/2)):
        if zz[k]!=zz[len(zz)-k-1]:
            flag = False
            break
    if flag == True:
        both.append(i)

#Here's where I look at multi digit numbers
for i in range(10,1000000):
    #Convert number to string
    i_str = str(i)
    #Convert to list
    i_list = list(i_str)
    #I swap every item in the list so the list is reversed
    for j in range(0,int(len(i_str)/2)):
        i_list[j],i_list[len(i_list)-j-1]=i_list[len(i_list)-j-1],  i_list[j]
    i_pal=int("".join(i_list))
    
    #I check if the number is a palindrome
    if i_pal == i:
        #If it is, I add it to my list of palindromes
        palindromes.append(i)
        #I was being dumb and didn't know how to make binary numbers
        #So I had a bunch of leading 0's and had to get rid of them
        i_bin = bin(i)[2:].zfill(20)
        i_bin_str = str(i_bin)
        i_bin_list = list(i_bin_str)
        for j in range(0,len(i_bin_list)):
            if i_bin_list[j]==0:
                i_bin_list.remove("0")
            else:
                break
        i_bin_1 = int("".join(i_bin_list))
        pal_bin.append(i_bin_1)
        z=str(i_bin_1)
        zz=list(z)
        flag = True
        #Finally, I check if the binary number is a palindrome
        #At any point that it is not, I stop the loop to save time of looping
        #the whole thing
        for k in range(0, int(len(zz)/2)):
            if zz[k]!=zz[len(zz)-k-1]:
                flag = False
                break
        if flag == True:
            both.append(i)
            
print(sum(both))
print(time.time()-start)
print("")

#Alright, code 2
start2=time.time()
pal_sum=0
#I can go through all my numbers in one go, no need to split out single digits
for i in range (1,1000000):
    #Checks the string of 'i' vs the reverse of the string of 'i'
    if str(i)==str(i)[::-1]:
        #This gets my binary numbers without leading 0's
        #Check the bin of i vs reverse
        #add 'i' to the sume if it is
        if bin(i)[2:]==bin(i)[2:][::-1]:
            pal_sum=pal_sum + i

print(pal_sum)   
print(time.time()-start2)   