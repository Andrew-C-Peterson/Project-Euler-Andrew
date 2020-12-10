#Pretty boring

import time as time

start = time.time()
num_sum = 0

for i in range(1,1001):
    num_sum = num_sum+ i**i

print(str(num_sum)[-10:])