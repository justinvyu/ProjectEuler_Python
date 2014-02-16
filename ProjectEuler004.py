import Library 

largest = 0

for i in range(100,999):
    for j in range(100,999):
        product = i * j
        if Library.isPalindrome(product) == True:
            if product > largest:
                largest = product

print largest
