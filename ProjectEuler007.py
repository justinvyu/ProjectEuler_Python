i = 2
counter = 0
while(i>1):
    if Library.isPrime(i) is True:
        counter = counter + 1
    if counter == 10001:
        print i
        break
    i = i + 1
