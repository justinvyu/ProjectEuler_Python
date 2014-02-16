n = 600851475143
i = 2

while i * i < n: #largest prime factor won't be more than the square root of the number
    while n % i == 0: #the number is a factor of the number
        n = n / i #keep dividing until you can't divide anymore
    i = i + 1 #keep adding 1 to the number

print n
