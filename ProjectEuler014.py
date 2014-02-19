import time
 
start = time.time()

#takes a lot of time because of python
def numSequences(n):
    counter = 1
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            counter = counter + 1
        elif n % 2 != 0:
            n = (n*3) + 1
            counter = counter + 1
    return counter
    
#find number of sequences for all numbers under 1000000 and compare
i = 1000000
chains = 0
num = 0
maximum = 0
while i >= 1:
    chains = numSequences(i)
    if chains > maximum:
        maximum = chains
        num = i
    i = i - 1
print num

elapsed = (time.time() - start)
print elapsed + 'seconds to run code'
