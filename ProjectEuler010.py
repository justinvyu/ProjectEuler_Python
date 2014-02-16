import Library

total = 0
for i in range(2,2000001):
    if Library.isPrime(i) is True:
        total = total + i
print total
