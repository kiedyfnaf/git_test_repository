#x = int(input("Wait: "))
#while x > 0:
    #if x % 3 == 0 and x % 5 == 0:
        #print("FizzBuzz")
    #elif x % 3 > 0 and x % 5 == 0:
        #print("Buzz")
    #elif x % 3 == 0 and x % 5 > 0:
        #print("Fuzz")
    #else:
        #print(x)
    #x = x - 1
'''
y = int(input("wait: "))
x = y - (y - 1)
while x < y:
    print(f"{x} " * x)
    x = x + 1
'''

from random import randint, choice

class postac():
    def __init__(self):
        self.nazwa = ""
        self.zycie = 5
        self.max_zycie = 5
    def atakuj(self, przeciwnik):

        atak = randint(0, 3)
        if atak == 0:
            unik = choice(["left", "right", "back"])
            print(f"{przeciwnik.nazwa} dodged {self. nazwa} w {unik}")
        else:
            print(f"{self.nazwa} attacks {przeciwnik.nazwa} and deals {atak} dmg")
            przeciwnik.zycie -= atak
class przeciwnik(postac):
    def __init__(self, gracz):
        super().__init__()
        self.nazwa = choice (["Goblin", "Skeleton", "Zombie"])
        self.zycie = randint(1, gracz.zycie)
class gracz(postac):
    def __init__(self):
        super().__init__()
        self.zycie = 10
        self.max_zycie = 10
        self.nazwa = input("Player's name: ")
    def odpoczynek(self):
        print(f"{self.nazwa} rests, life : {self.zycie}/{self.max_zycie}")
        self.zycie += 1
        if(self.zycie > self.max_zycie):
            self.zycie = self.max_zycie
    def walka(self, przeciwnik):
        walka_trwa = True
        while walka_trwa:
            print(f"Player's life: {self.zycie}")
            print(f"{przeciwnik.nazwa}'s life: {przeciwnik.zycie}")
            akcja_walki = input("Battle action (attack, run): ")
            if akcja_walki == 'attack':
                self.atakuj(przeciwnik)
                if przeciwnik.zycie <= 0:
                    print(f"{self.nazwa} kills {przeciwnik.nazwa}")
                    return True
                przeciwnik.atakuj(self)
            elif akcja_walki == 'run':
                print(f"{self.nazwa} runs away!")
                przeciwnik.atakuj(self)
                walka_trwa = False
            else:
                print("Action unavaliable.")
            if self.zycie <= 0:
                print(f"{self.nazwa} dies.")
                return False
        return True
gracz = gracz()
gra = True
while gra:
    akcja = input("What u want to do (explore, rest): ")
    if akcja == 'explore':
        if randint(0, 1) == 0:
            print(f"{gracz.nazwa} finds a cave.")
        else:
            przeciwnik = przeciwnik(gracz)
            print(f"{gracz.nazwa} meets {przeciwnik.nazwa}")
            gra = gracz.walka(przeciwnik)
    elif akcja == 'rest':
        gracz.odpoczynek()
    else: 
        print("Action unavaliable")


        
 