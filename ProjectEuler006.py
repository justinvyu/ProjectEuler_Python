import math

difference = 0
sum1 = 0
for i in range(1,101):
    sum1 = sum1 + i**2

sum2 = 0
for i in range(1,101):
    sum2 = sum2 + i

sum2 = sum2**2

difference = math.fabs(sum2-sum1)
print difference
