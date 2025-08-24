import math
import random
again = True
e = 2.7182818284590452353602874713527
options = ["/", "*", "+", "-", "!","root","^", "ln", "log", "mod", "||", "exp", "random", "mz"]
question = input("What do you want to do (geo/alg)?:  ").lower()
if question == "alg":
    try:
        num_1 = float(input("Whats the number?: "))
        next = num_1 - 1
    except ValueError:
        print("Dont do that man.")
    else:
        while again == True: 
            work = input("What you want to do: (/,*,+,-,^,root,!,ln,log,mod,||,exp,random,Mz)")
            if work.lower() and work not in options:
                print("Are you stupid?")
            if work == "/":
                try:
                    num_2 = float(input("Whats the second number?: "))
                    sum = num_1/num_2
                    print(round(sum, 5))
                except ValueError:
                    print("Fuck off")
            elif work == "*":
                try:
                    num_2 = float(input("Whats the second number?: "))
                    sum = num_1*num_2
                    print(round(sum, 5))
                except ValueError:
                    print("Fuck off")
            elif work == "+":
                try:
                    num_2 = float(input("Whats the second number?: "))
                    sum = num_1+num_2
                    print(round(sum, 5))
                except ValueError:
                    print("Fuck off")
            elif work == "-":
                try:
                    num_2 = float(input("Whats the second number?: "))
                    sum = num_1-num_2
                    print(round(sum, 5))
                except ValueError:
                    print("Fuck off")
            elif work == "!":
                if int(num_1) == num_1 and num_1 > 1:
                    while next > 1:
                        sum = num_1 * (next)
                        num_1 = sum
                        next = next -1
                    print(sum)
                else:
                    print("You cant factorial this number bozo.")
            elif work == "^":
                try:
                    num_2 = float(input("Whats the second number?: "))
                    sum = math.pow(num_1, num_2)
                    print(round(sum, 5))
                except ValueError:
                    print("Fuck off")
            elif work == "root":
                try:
                    num_2 = (input("Whats the second number?: "))
                    sum = num_1**(1/num_2)
                    print(round(sum, 5))
                except ValueError:
                    print("Really...?")
            elif work == "ln":
                try:
                    if num_1 < 0:
                        print("Dont use complex numbers dude.")
                    else:
                        sum = math.log(num_1, e)
                        print(round(sum, 10))
                except ValueError:
                    print("You can't do that.")
            elif work == "log":
                try:
                    num_2 = float(input("Whats the base?: "))
                    sum = math.log(num_1, num_2)
                    print(round(sum, 10))
                except ValueError:
                    print("Fuck off")      
            elif work == "mod":
                try:
                    num_2 = float(input("Whats the base?: "))
                    sum = num_1 % num_2
                    print(round(sum, 5))
                except ValueError:
                    print("Fuck off")
            elif work.lower() == "mz":
                a = float(input("a : "))
                b = float(input("b : "))
                c = float(input("c : "))
                p = ((b**2) - (4*c*a))
                if p < 0:
                    print("Ta funkcja nie ma mjejsc zerowych.")
                    x = "brak"
                    y = "brak"
                    sum = 0
                else:
                    p = p**(1/2)
                    x = (-b + p) / (2*a)
                    y = (-b - p) / (2*a)
                    x = print(f"1-st is about: {round(x, 5)}")
                    y = print(f"2-nd is about: {round(y, 5)}")
                    sum = 0
            elif work == "exp":
                try:
                    sum = e**num_1
                    print(round(sum, 5))
                except ValueError:
                    print("Fuck off") 
            elif work == "||":
                try:
                    if num_1 < 0:
                        sum = num_1 * (-1)
                    else:
                        sum = num_1
                    print(sum)
                except ValueError:
                    print("Fuck off")
            elif work == "random":
                key = "ch"
                while True:
                    try:
                        if key == "ch":
                            st = int(input("What's the lower bound?: "))
                            nd = int(input("What's the higher bound?: "))
                        sum = random.randint(st, nd)
                        print(round(sum))
                    except ValueError:
                        print("Fuck off")
                    key = input("Want to keep going (enter). Change bound or end?: (end/ch)").lower()
                    if key == "end":
                        num_1 = float(input("Whats the number?: "))
                        sum = num_1
                        break
            again = input("....." * 10)
            if again == "":
                again = True
                num_1 = sum
            else:
                again = False
                print("Fuck off.")
elif question == "geo":
        options = ["tri", "ang","sqr","rect","cir","trap"]
        while again == True: 
            work = input("What you want to do: (tri,ang,sqr,rect,cir,trap)")
            if work.lower() not in options:
                print("Are you stupid?")
            elif work == "trap":
                work = input("Is there anything special about it? (90,równo,norm)")
                if work == "90":
                    work = input("What do you have? ()")
                elif work == "trap":
                    work = input("Is there anything special about it? (90,równo,norm)")
                elif work == "trap":
                    work = input("Is there anything special about it? (90,równo,norm)")

                print(f"Area is {math.pi * (rad**2)}")
                print(f"Perimeter is {2*math.pi*rad}")
                print(f"diagonal is {2*rad}")
            elif work == "rect":
                a = float(input("Whats the 1-st side?"))
                b = float(input("Whats the 2-nd side?"))
                area = a*b
                perimeter = (2*a) + (2*b)
                diagonal = math.sqrt((a**2)+(b**2))
                print(f"Area is {area}")
                print(f"Perimeter is {perimeter}")
                print(f"diagonal is {round(diagonal, 5)}")
            elif work == "sqr":
                x = float(input("Whats the side length?"))
                area = x**2
                perimeter = x*4
                diagonal = x*(math.sqrt(2))
                print(f"Area is {area}")
                print(f"Perimeter is {perimeter}")
                print(f"diagonal is {round(diagonal, 5)}")
            elif work == "ang":
                what = input("What you want (sin,cos,tg,ctg,csc,sec,inv)")
                ang = float(input("Whats the angle (degrees)?"))
                ang = math.radians(ang)                
                if what == "inv":
                    what = input("What you want (sin,cos,tg,ctg,csc,sec)")
                    if what == "sin":
                        x = math.asin(ang)
                        print(f"The value is {round(x, 4)}")
                    if what == "cos":
                        x = math.acos(ang)
                        print(f"The value is {round(x, 4)}")
                    if what == "tg":
                        x = math.atan(ang)
                        print(f"The value is {round(x, 4)}")
                    if what == "ctg":
                        ang = 1/(math.tan(ang))
                        x = math.act(ang)
                        print(f"The value is {round(x, 4)}")
                elif what != "inv":
                    if what == "sin":
                        x = math.sin(ang)
                        print(f"Its {round(x, 4)}.")
                    if what == "cos":
                        x = math.cos(ang)
                        print(f"Its {round(x, 4)}.")
                    if what == "tg":
                        x = math.tan(ang)
                        print(f"Its {round(x, 4)}.")
                    if what == "ctg":
                        x = math.tan(ang)
                        x = 1/x
                        print(f"Its {round(x, 4)}.")
                    if what == "csc":
                        x = math.sin(ang)
                        x = 1/x
                        print(f"Its {round(x, 4)}.")
                    if what == "sec":
                        x = math.cos(ang)
                        x = 1/x
                        print(f"Its {round(x, 4)}.")
            elif work == "tri":
                try:
                        what = input("What do you have (sides, 2s+ang, 2ang+s)").lower()
                        if what == "sides":
                            a = float(input("Put in 1-st length: "))
                            b = float(input("Put in 2-nd length: "))
                            c = float(input("Put in 3-th length: "))
                            cosa = (b**2 + c**2 - a**2) / (2 * b * c)
                            cosb = (a**2 + c**2 - b**2) / (2 * a * c)
                            cosc = (b**2 + a**2 - c**2) / (2 * b * a)
                            angle_bc = math.acos(cosa) * (180 / math.pi)
                            angle_ac = math.acos(cosb) * (180 / math.pi)
                            angle_ab = math.acos(cosc) * (180 / math.pi)
                            print(f"Angle bc = {angle_bc}")
                            print(f"Angle ac = {angle_ac}")
                            print(f"Angle ab = {angle_ab}")
                            k = 1/2*(a+b+c)
                            x = math.sqrt(k*(k-a)*(k-b)*(k-c))
                            print(f"Area is equal: {round(x,5)}")
                        elif what == "2s+ang":
                                print("The sides you have consider as A and B.")
                                angle = input("Which angle is it? (a-b,b-c,a-c): ")
                                if angle == "a-b":                                        
                                    a = float(input("Put in 1-st length: "))
                                    b = float(input("Put in 2-nd length: "))
                                    c_ang = float(input("Whats the angle (degrees)? "))
                                    c_ang = math.radians(c_ang)
                                    c = (b**2 + a**2) - (2 * b * a * math.cos(c_ang))
                                    c = math.sqrt(c)
                                    cosb = (a**2 + c**2 - b**2) / (2 * a * c)
                                    cosa = (b**2 + c**2 - a**2) / (2 * b * c)
                                    angle_bc = math.acos(cosa)
                                    angle_ac = math.acos(cosb)
                                    print(f"Side c has length: {round(c, 2)}")
                                    print(f"Angle ac = {round(math.degrees(angle_ac), 2)}")
                                    print(f"Angle bc = {round(math.degrees(angle_bc), 2)}")
                                    k = 1/2*(a+b+c)
                                    x = math.sqrt(k*(k-a)*(k-b)*(k-c))
                                    print(f"Area is equal: {round(x,5)}")
                                elif angle == "b-c":
                                    a = float(input("Enter the length of the 1st side: "))
                                    b = float(input("Enter the length of the 2nd side: "))
                                    a_ang = float(input("Enter the angle (in degrees): "))
                                    a_ang = math.radians(a_ang)
                                    x = math.sin(a_ang) * (b / a)
                                    x = math.asin(x)  # Angle bc in degrees # Convert back to radians for further calculations
                                    ang_ba = 180 - math.degrees(a_ang) - math.degrees(x)
                                    ang_ba = math.radians(ang_ba)  # Convert to radiansg
                                    c = (b ** 2 + a ** 2) - (2 * b * a * math.cos(ang_ba))
                                    c = math.sqrt(c)
                                    print(f"Length of side c: {round(c, 2)}")
                                    print(f"Angle ac: {round(math.degrees(ang_ba), 2)}")
                                    print(f"Angle bc: {round(math.degrees(x), 2)}") 
                                    k = 1 / 2 * (a + b + c)
                                    area = math.sqrt(k * (k - a) * (k - b) * (k - c))
                                    print(f"Area of the triangle: {round(area, 5)}")   
                                elif angle == "a-c":
                                    a = float(input("Enter the length of the 1st side: "))
                                    b = float(input("Enter the length of the 2nd side: "))
                                    c_ang = float(input("Enter the angle (in degrees): "))
                                    c_ang = math.radians(c_ang)
                                    x = math.sin(c_ang) * (a / b)
                                    x = math.asin(x)  # Angle bc in degrees # Convert back to radians for further calculations
                                    ang_ac = 180 - math.degrees(c_ang) - math.degrees(x)
                                    ang_ac = math.radians(ang_ac)  # Convert to radians
                                    c = (b ** 2 + a ** 2) - (2 * b * a * math.cos(ang_))
                                    c = math.sqrt(c)
                                    print(f"Length of side c: {round(c, 5)}")
                                    print(f"Angle ac: {round(math.degrees(ang_ac), 3)}")
                                    print(f"Angle bc: {round(math.degrees(x), 3)}") 
                                    k = 1 / 2 * (a + b + c)
                                    area = math.sqrt(k * (k - a) * (k - b) * (k - c))
                                    print(f"Area of the triangle: {round(area, 5)}")                                
                        elif what == "2ang+s":
                            print("The angles you have are opposite to A and B.")
                            a_ang = float(input("Whats the angle A?: "))
                            b_ang = float(input("Whats the angle B?: "))
                            c_ang = 180-a_ang-b_ang
                            angle = input("Which side you have (a,b,c)?: ").lower()
                            side = float(input("What is the length of this side: "))
                            c_ang = math.radians(c_ang)
                            b_ang = math.radians(b_ang)
                            a_ang = math.radians(a_ang)
                            if angle == "a":
                                    a = side
                                    b = (math.sin(b_ang)/math.sin(a_ang)) * side
                                    c = (math.sin(c_ang)/math.sin(a_ang)) * side
                                    c_ang = math.degrees(c_ang)
                                    print(f"Side a has length: {round(a, 3)}")
                                    print(f"Side b has length: {round(b, 3)}")
                                    print(f"Side c has length: {round(c, 3)}")
                                    print(f"Angle ab = {round(c_ang, 5)}")
                            elif angle == "b":                                                                       
                                    b = side
                                    a = (math.sin(a_ang)/math.sin(b_ang)) * side
                                    c = (math.sin(c_ang)/math.sin(b_ang)) * side
                                    c_ang = math.degrees(c_ang)
                                    print(f"Side a has length: {round(a, 3)}")
                                    print(f"Side b has length: {round(b, 3)}")
                                    print(f"Side c has length: {round(c, 3)}")
                                    print(f"Angle ab = {round(c_ang, 5)}")
                            elif angle == "c":
                                    c = side                                                                       
                                    b = (math.sin(b_ang)/math.sin(c_ang)) * side
                                    a = (math.sin(a_ang)/math.sin(c_ang)) * side
                                    c_ang = math.degrees(c_ang)
                                    print(f"Side a has length: {round(a, 3)}")
                                    print(f"Side b has length: {round(b, 3)}")
                                    print(f"Side c has length: {round(c, 3)}")
                                    print(f"Angle ab = {round(c_ang, 5)}")
                            k = 1/2*(a+b+c)
                            x = math.sqrt(k*(k-a)*(k-b)*(k-c))
                            print(f"Area is equal: {round(x,5)}")
                except ValueError:
                    print("Fuck off")                    
            key = input("Do you want to keep going (n/y)?") 
            if key == "y":
                again = True
            else:
                key = False
else:
    print("Are you stupid?")

            

