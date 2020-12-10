#How to make 2 lbs using different cominbations of coins

#Dynamic programming    
coins = [1,2,5,10,20,50,100,200]

count = [1]+[0]*200

for coin in coins:
    for i in range(coin, 201):
        count[i] += count[i-coin]
print("Ways to make change =", count[200])
    
print("count = ", count)