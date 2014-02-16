num = 2520
counter = 0
found = False

while found is False:
    for i in range(1,21):
        print num
        if num % i != 0:
            break
        else:
            counter = counter + 1  
    if counter == 20:
        print num
        found = True
    else:
        counter = 0
        num = num + 1   
