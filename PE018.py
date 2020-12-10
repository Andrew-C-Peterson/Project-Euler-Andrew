#maximum sum through triangle

#numbers copied as string
number = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''


#split this into a list of lists
number = number.strip().split('\n')

for i in range(1,len(number)):
	number[i] = number[i].strip().split(' ')
	number[i] = [int(x) for x in number[i]]
number[0]=75

#starting from the bottom, find the maximum value for each possible move and stores this
for i in range(14,1,-1):
    for j in range(0,len(number[i])-1):
        a = number[i][j]
        b = number[i][j+1]
        if a>=b:
            number[i-1][j]=number[i-1][j]+a
        else:
            number[i-1][j]=number[i-1][j]+b
        
print(max(number[1])+number[0])
for i in range(0,15):
    print(number[i])
