def divisors(n):
    counter = 0
    for i in range(1,int(n**0.5) +1):
        if n % i == 0:
            counter = counter + 1
    return counter * 2

findvalue = False
x = 2
j = 1
while findvalue is False:
    if divisors(j) > 500:
        print j
        findvalue = True
    else:
        j = x + j
        x = x + 1
