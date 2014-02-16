import Library

total = 0
firstNum = 1
secondNum = 1
temp = 0
while temp < 4000000:
    temp = firstNum + secondNum
    if Library.isEven(temp):
        total += temp
    firstNum = secondNum
    secondNum = temp
print total
