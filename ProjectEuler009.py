#2 independent variables, 1 dependent variable (on the other two)
c = 0
for a in range(1,1001):
    for b in range(a,1001):
        c = 1000-a-b
        if c > a and c > b:
            if (a*a + b*b) == c*c:
                print a*b*c
                break
