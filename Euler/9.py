a = 1001
while a > 1:
    b = a-1
    a -= 1
    while b != 1:
        c = (a**2 + b**2)**(1/2)
        if c == int(c):
            if a+b+c == 1000:
                print(a)
                print(b)
                print(c)
                print(a*b*c)
        b -= 1
    

    