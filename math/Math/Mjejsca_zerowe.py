import math
'''
a = float(input("Wprowadz a: "))
b = float(input("Wprowadz b: "))
c = float(input("Wprowadz c: "))
p = ((b**2) - (4*c*a))**(1/2)
if p < 0:
    print("Ta funkcja nie ma mjejsc zerowych.")
else:
    p = p**(1/2)
    x = (-b + p) / (2*a)
    y = (-b - p) / (2*a)
    x = round(x, 5)
    y = round(y, 5)
    print(f"x ~  {x} ")
    print(f"y ~  {y} ")
'''
k = float(input("a : "))
g = float(input("b : "))
h = float(input("c : "))
class Mz():
    def licz(self):
        print(f"Mjejsca zerowe to\nx = {self.x}")
        print(f"y = {self.y}") 

class Karp(Mz):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        p = ((b**2) - (4*c*a))
        if p < 0:
            print("Ta funkcja nie ma mjejsc zerowych.")
            self.x = "brak"
            self.y = "brak"
        else:
            p = p**(1/2)
            self.x = (-b + p) / (2*a)
            self.y = (-b - p) / (2*a)
            self.x = round(self.x, 5)
            self.y = round(self.y, 5)
            
Coo1 = Karp(k, g, h)
Coo1.licz()




