1.  #class of a variable
   x = 5
   print(f'"1"{type(x)}') 

2.  #String
   F_n = "M"
   L_n = "K"
   FF_n = F_n +" "+ L_n
   print("hello " + FF_n)

3. #Integer
   age = 2
   age += 1
   print(f'Your age is {age}') # =3

4. #Float
   h = 12.2
   print(type(h)) # = float
   print("Your height is: "+str(h)+"cm")

5. #Bool
  z = True
  print("Are you a human: " +str(z))

6. #Multiple
  n, k, p = 2, "no", False
  n = p = k = 4   

7. #Len, counts signs
  h = "Hello kk"
  print(len(h)) # = 8

8. # name.find / capitalize / upper / lower === find a sign / make first big / all big / all small
  h = "Hello kk"
  print(h.find("e")) # = 1

9. #name.isdigit / isalpha / count / replace
  h = "2"
  print(h.isdigit()) # = True
  h = "hello"
  print(h.count("l")) # = 2
  print(h.replace("l", "a")) # = heaao
  print(h*4) # = hellohellohellohello

10. #Changing
  y = 2.3
  y = int(y) # = 2
  z = "5"
  z = int(z) # = 5
  f = 3
  f = float(f) # = 3.0
  print("Why is this: "+f) # error/ cause you cant add float to str
  print("Why is this: "+str(f)) # Why is this 3

11. #Input
  z = int(input("How tall: "))
  z = z + 1
  print(z) # for z = 2 === 3
  print("You are" +str(z)+"years old") # You are 3 years old.

12. #Math
  import math
  pi = 3.14
  print(round(pi)) # = 3 / rounded to nearest
  print(math.ceil(pi)) # = 4 / rounded up
  print(math.floor(pi)) # = 3 / rounded down 
  print(abs(pi)) # absolute value
  print(pow(pi,2)) # pi ^2
  print(math.sqrt(pi)) # pi^1/2
  x = 1
  b = 2
  c = 3
  print(max(x, b, c)) # = 3
  print(min(x, b, c)) # = 1

13. # Slice   [start;stop;step]   Str has positive and negative numbers
  a = "bum and gone"
  k = a[0:2] #         = bu
  p = a[5:] #          = d gone
  p = a[0:12:2] #      = bmadgn
  p = a[::3] #         = b do
  p = a[::-1] #        = enog dna mub
  sli = slice(4 ,-3)
  print(a[sli]) #      = nd 

14. #not  flips 'true to false' and other way around
  k = 5
  if k >= 2:
  print("Man")  #Man
  if not(k >= 2):
  print("Guy")  #Nothing cause its true but with 'not' its false

15. # While loop     if you wont type your name it will ask again
  k = ""
  while len(k)== 0:
  k = input("Whats your name: ")
  k = None
  while not k:
  k - input("Whats you name: ")

16. # For loop
  for i in range (10):
  print(i)  # 0,1,2,3,4,5,6,7,8,9
  for i in range (50,100+1)
  print(i)  #50,51,52 ... 100 
  for i in range (50,100+1,2)
  print(i)  #50,52,54 ..100
  for i in "Why me"
  print(i)  # W h y   m e  each in different line
  for seconds in range(10,0,-1)
     print(seconds)
     time.sleep(1)
     print("Happy new year")  # it will count 10,9,8 each second until zero

17. #Nested loop (loop in a loop)
  rows = int(input("How many rows?: "))
  columns = int(input("How many columns?: "))
  symbol = int(input("How many symbols?: "))
  for i in range(rows)
    for j in range(columns)
      print(symbol, end="")
  print()   # will print symbols in the put amount of rows and columns

18. #Loop control
  #while True
  name = input("Enter your name: ")
  if name != ""
  #break
  z = "421-2414-244"
  for i in z
  if i =="-"
  #continue
  print(i, end="") # = 4212414244
  for i in range(1,21)
  if i == 13:
  pass
  else
  print(i)

19. #List
  food = ["pizza", "ham", "kick", "dog"]
  print(food[0]) #pizza
  food[0] = "cat"
  print(food[0]) #cat   I changed first string into cat
  for x in food
  print(x) # pizza, ham, kick, dog
  food.append("ice") # adds at the end
  food.remove("hotdog") # removes hot dog
  food.pop() #removes last value
  food.insert(0, "cake") #puts cake as first without deleting
  food.sort() #sorts alphabetically
  food.clear() #removes all elements

20. #2d list
  drink = ["cup", "water", "tea"]
  morning = ["why", "boom", "Johan"]
  noon = ["ham", "dog", "big"]
  food = [drink,morning,noon]
  print(food[1][0]) #prints why  (second list, first element)

21. #Tuple
  s = ("kid", 12, "guy")
  s.count("kid") # = 1  there is only one value 'kid'
  s.index("guy") # = 2  its 3th
  if "kid" in s:
  print("Keep him") # = keep him

22. #Set  (unordered, no indexed, faster to calculate)
  s = {"fork", "ten", "pen"}
  for x in s
  print(x)
  s.add("nap")
  s.remove("fork")
  s.clear() # all gone
  p = {"name", "kick", "up"}
  s.update(p) #prints all in 's' and 'p'
  din = s.union(p) #makes a set of both sets
  print(s.difference(p)) # prints what s has and p doesnt
  print(s.intersection(p)) # what the have in common
  
23. #dictionary  (unordered, changable, with key values)
  cap = {'USA':'Wash', 'Pol':'dig', 'chin':'dog'}
  print(cap['Pol']) # = dig
  print(cap.get('Pol')) # = dig
  print(cap.get('His')) # prints 'None'
  print(cap.keys()) # prints all keys
  print(cap.values()) # = prints all values
  print(cap.items()) #= prints all both key and value
  for key,value in cap.items():
  print(key, value)# prints whole dictionary
  cap.update({'Ger': 'Ber'}) # adds ger as key and ber as value
  cap.update({'USA': 'Vegas'}) #changes the value of USA to vegas
  cap.pop('chin') #removes the chin and its value from dictionary
  cap.clear() # deletes everything
  students = [
    {"name": "Herm", "house": "Griff", "patron": "Otter"}
    {"name": "Harry", "house": "Griff", "patron": "Stag"}
    {"name": "Ron", "house": "Griff", "patron": "Jack"}
    {"name": "Draco", "house": "Slyth", "patron": None}
  ]
for x in students:
  print(x["name"]) # gives their names is diff lines
  print(x["name"], x["house"], x["patron"], sep=", ")

24. #Index
  name = "kids"
  if(name[0].islower()):
  name = name.capitalize()
  print(name) # = Kids
  first = name[0:2].upper()
  print(first) # KID
  last = name[1:].lower()
  print(last) # = ids
  put = name[-1]
  print(put) #= s

25. #Function
 def hello(name):
  print("Why?"+name)
  print("Bruh")
  hello() # prints 'Why' and 'Bruh'
  hello("Pot") # prints Why Pot / Bruh
   def shh(name, euler):
  print("Why?"+name+""+euler)
  print("Bruh")
  pi = "Giga"
  hello(pi)  # Why giga / Bruh
  hello("Kid", "Uh")
def hello(to="world")
  print("hello, ", to)
hello() # = hello world/ to is a global value of world 
hello("name") # = hello name / global value was overwritten
def main():
  x = int(input("Whats the x: "))
  print("x squared it:", square(x))
def square(x):
  return x ** 2 # it gives back the input as different input
def main(): # This will check if a number is even or not
  x = int(input("Whats the number: "))
  if is_even(x):
    print("Even")
  else:
    print("Odd")
def is_even(n):
  return n % 2 == 0 # returns true or false


26. #Return statements
  def mul(num1, num2):
  result = num1 + num2
  #return result
  x = mul(6, 8)
  print(x) # = 14

27. #Keyword argument
  def hello(fir,mid,las):
  print("Hello "+fir+" "+mid+" "+las)
  hello(las="kod", mid="man", fir="bot") # = Hello bot man kod

28. #Nested calls
  print(round(abs(float(input("Whats the number: ")))))
  # Just writing in a smaller amount of lines

29. #Scope (second print wont work since variable is inside a function),
    #that way one name can have local and global value, but global will work
    #in functions if there arent ary local ones with this name)
 def dis():
  name = "code"
  print(name)
print(name)

30.#Args (unchangeable) , but you can change it into a list and then change the values
 def add(*stuff):
  sum = 0
  sum = list(sum)
  sum[0] = 0
  for i in stuff:
    sum += 1
  return sum
print(add(1,2,3,4,5,6)) # = 20, cause i changed 1 into 0, so its not 21

31.# Kwargs = Key word dictionary, pacs varying amount of key words into a dictionary
  def hel(**stuff):
  #print("Hello " + stuff['fir'] + stuff['sec'])
  print("Hello",end=" ")
  for key,value in stuff.items():
  print(value,end=" ") # this end will make it so everything will be in the same line
hel(title="Boom",fir+"Man",sec="Dom",las="Why") # = Boom Man Dom Why

32.#Format (more control when displaying output)
  animal= "cow"
  item = "moon"
  print("The"+animal+"jump"+ item)
  print("The {} jump {}".format(animal, item)) #same thing
  print("The {1} jump {0}".format(animal, item)) #the moon jump cow
  text = "The {} jump {}."
  print(text.format("cow", "moon")) # =The cow jump moon.
  name = "Why"
  print("Hello, my name is {:10} cool".format(name)) # =Hello my name is why        cool.
  print("Hello, my name is {:>10} cool".format(name)) # =Hello my name is        why cool.
  print("Hello, my name is {:^10} cool".format(name)) # =Hello my name is    why    cool.
  num = 3.14159
  god = 2400
  print("Number {:.2f}".format(num)) # = 3.14
  print("Number {:,}".format(god)) # = 2,400
  print("Number {:b}".format(god)) # = as binary code 1001101010
  print("Number {:e}".format(god)) # = as scientific notation 2,40000000+03

33. #Random
  import random
  x = random.randint(1,6) # random number from 1 to 6
  y = random.random() # random number from 0 to 1
  mylist = ['rock', 'paper', 'scissors']
  z = random.choice(mylist) # random string
  cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]
  random.shuffle(cards) #will print the list in random order

34. #Exception (interrupts a program)
  try:
  num = int(input("Enter: "))
  den = int(input("Enter: "))
  result = num/den
  print(result)
  except Exception:
  #OR
  except ZeroDivisionError:
  print("You cant divide by 0 man.")
  except ValueError as e:
  print(e) # = invalid literal for int() with base 10
  print("Only numbers man.")
  else:
  print(result) # if there is no error it works normally
  finally:
  print("End") # finally block always executes

35. #File detection
  import os
  path = "C:\\Users\\bugal\\OneDrive\\Pulpit\\manga.txt" # Use double slashes
  if os.path.exists(path):
  print("It does exist")
  if os.path.isfile(path): # if its not a file but a folder then it wont activate this if
  if os.path.isfile(path) # if its a file
  if os.path.isdir(path) # if its a directory
  print("its a file")
  else:
  print("It doesnt")

36. #Read a contexts of a file
  try:
  with open('C:\\Users\\bugal\\OneDrive\\Pulpit\\manga.txt') as file:
  print(file.read()) # prints text from a file
  print(file.closed) # if will print false if the file is open, and true if closed.
  except FileNotFoundError:
  print("File was not found")

37.# Write a file
  text = "Why\nSome text\nKid" # this \n means new line
  with open('mana.txt', 'w' ) as file: # 'w' is for write
  file.write(text) # makes a new txt file in project with given text
  with open('mana.txt', 'a' ) as file: # 'a' is for append so you add a text to a file without deleting the previous one   

38. #Copy files
  import shutil 
  shutil.copyfile('cheese.txt', 'Math.txt') #1. source, 2. destination(name of a file
  shutil.copyfile('cheese.txt', 'C:\\Users\\bugal\\OneDrive\\Pulpit\\math.txt')  # copies a file to a pulpit
  # copyfile() = copies the file
  # copy() = copyfile + permission mode + destination can be a directory
  # copy2() = copy() + copies metadata(file's creation and modification times)

39. #Move files
  import os
  source = "cheese.txt"
  des = "C:\\Users\\bugal\\OneDrive\\Pulpit\\cheese.txt" # if you want a file then just type (file name) in place of cheese.txt
  try:
  if os.path.exists(des)
  print("There is a file there")
  else:
  os.replace(source,des)  # we moved the file into the pulpit from the project
  print(source+ " was moved")
  except FileNotFoundError:
  print(source+" was not found")

40. #Delete files
  import os
  path = 'cheese.txt'
  try:
  os.remove(path) # if its not in project then paste a path
  except FileNotFoundError:
  print("Was not found")
  except PermissionError:
  print("You dont have permission to delete that")
  else:
  print(path + " was deleted")
  os.rmdir() # remove an empty directory
  except OSError:
  print("You cannot delete taht using that function")
  # if you want to delete a directory with files in it
  import shutil
  shutil.rmtree(path) # delete the directory with all files in it

41. #Modules Create a new file first
  def hello():
  print("Hello! Have a nice day")
  def bye():
  print("Why?") # Up to this point write this in the other file with name (snake).
  import snake as msg
  msg.hello() # will call a function from other file here
  #Also
  from snake import hello,bye
  hello()
  bye() # same thing
  help("modules") # will show you all modules you could use check them out in a browser

42. #Basic game
  import random
  player = None
  choices = ["rock", "paper", "sci"]
  computer = random.choice(choices)
  while player not in choices:
  player = input("rock, paper or sci?").lower() # it will keep asking if your answer is not in here, and we make it all lowercase so that Rock will be equal to rock
  print("Computer: ",computer)
  print("Player: ",player)
  if player == computer:
  print("Tie")
  elif player == "rock":
  if computer == "paper":
  print("You lost.")
  if computer == "sci":
  print("You Won.")
  elif player == "paper":
  if computer == "sci":
  print("You lost.")
  if computer == "rock":
  print("You Won.")
  elif player == "sci":
  if computer == "rock":
  print("You lost.")
  if computer == "paper":
  print("You Won.")
  if play != "yes": # != just means doesnt equal
  #break  This will break a while loop

43. #Basic quiz game
  def new_game():
    guesses = []
    correct = 0
    question_num = 1
    for key in questions:
        print("---------------------")
        print(key) # prints all questions
        for i in options[question_num - 1]:  # Use question_num - 1 to access the correct options list
            print(i)
        guess = input("Enter (A, B, C, D)")
        guess = guess.upper()
        guesses.append(guess)
        correct += check(questions.get(key), guess)
        question_num += 1
    display(correct, guesses)
def check(answer, guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0
def display(correct, guesses):
    print("--------------------")
    print("Results")
    print("--------------------")
    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()
    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()
    score = (correct/len(questions))*100
    print("Your score is: "+str(score)+"%")
def play_again():
  response = input("Do you want to play again? (yes or no): ")
  response = response.upper()
  if response == "YES":
    return True
  else:
    return False
questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
    }

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]
new_game()
while play_again():
  new_game()
print("Byeeeee")


44. #Object
class Car: # if a class is long make it in the other tab
  def __init__(self,make,model,year,color):
    self.make = make
    self.model = model
    self.year = year
    self.color = color
  def drive(self):
    print("This " +self.car+" is driving")
  def stop(self):
    print("This " +self.car+" is stopped")
from car import Car
car_1 = Car("Chevy","Corvetter",2021,"blue")
car_2 = Car("Ford","Mustand",2022, "red")
print(car_1.make)  
print(car_1.model)  
print(car_1.year)  
print(car_1.color) 
car_1.drive()  
car_1.stop() 
car_2.drive()  
car_2.stop()

45. #Class variable
class Car:
  wheels = 4
  car_1 = Car("Chevy","Corvetter",2021,"blue")
  car_2 = Car("Ford","Mustand",2022, "red")
  car_2.wheels = 2
  def __init__(self,make,model,year,color):
    self.make = make
    self.model = model
    self.year = year
    self.color = color
print(car_1.wheels) # = 4 (overall value is signed to everything)
print(car_2.wheels) # = 2 (our 505 line overwrote the global value)
-----------------------------------------------------------------
Car.wheels = 2 #both car 1 and 2 will have (2 wheels)

46. #Iheritance (classes can inherit other classes value) child classes is our Cat/ child call can use mothers commands
class Animal:
  alive = True
  def eat(self):
    print("This animal is eating")
  def sleep(self):
    print("This animal is sleeping")
class Cat(Animal):
  def run(self):
    print("This cat is running")
class Fish(Animal):
  def swim(self):
    print("This fish is swimming")
class Hawk(Animal):
  def fly(self):
    print("This hawk is flying")
Cat = Cat()
Fish = Fish()
Hawk = Hawk()
print(Cat.alive) # = True

47. #Child inheritance
class Organism:
  alive = True
class Animal(Organism):
  def eat(self):
    print("This animal is eating")
class Dog(Animal):
  def bark(self):
    print("This dog is barking")
dog = Dog()
print(dog.alive)# = True
print(dog.bark)# = this dog is barking

48. # Multiple inheritance
class Predator:
  def hunt(self):
    print("Hunts")
class Prey:
  def hide(self):
    print("Hides")

class Fish(Predator, Prey):
  pass
fish = Fish()
print(fish.hunt) # = Hunts

49. #Method overwriting/ the def inside the called class has priority over the one globaly
class Animal:
  def eat(self):
    print("Eating")
class Cat(Animal):
  def eat(self):
    print("This cat is eating")
cat = Cat()
cat.eat() # = This cat is eating

50. #Method chaining (call multiple methods)
class Car:
  def turn_on(self):
    print("Engine started")
    return self
  def turn_off(self):
    print("Engine off")
    return self
  def brake(self):
    print("Slows down")
    return self
  def speed(self):
    print("Speed is up")
    return self
car = Car() # alaws change it like that much more less errors
car.turn_on().brake() # = Engine started \n Slows down
car.turn_off()\
    .brake()\
    .turn_on()\
    .speed()  # a bit more readible
car.turn_off().brake().turn_on().speed()  #= same thing as one before just print all 4 values in diff lines

51. #print
print("Kid", sep='???', end="god") # = Kid???mangodNah
print("Nah") # sep = means whats in between values, normally a space
# end means what a prints ends with normally \n (new line) 
name = input("Whats your name: ")
name = name.strip().title()  
print(f"Hello, {name}") # hello, David Boston
# even if i input(      david boston    ) 
#strip deletes all spaces from left and right
#title capitalises every first letter of a new word you put
#split
first, last = name.split(" ")
print(f"Hello, {first}") # if you input Dog God it will = Hello Dog, splits into two values
print(f"{name:,}")# for name = 1000 it will give you 1,000 
name = round(x, 2) # to 2 digits
print(f"{name:.2f}") # rounds to 2 digits

52. #Inreactive
code cal.py # opens you a tab named cal.py
pyhton cal.py # runs a code inside cal.py 

53. #Match
name = input("Whats your name: ") # when you say harry or any other it will print griff
match name:
  case "Harry" | "Hermi" | "Ron":
    print("Griff")
  case _:
    print("Who?")

54. #Build a column
def main():
  print_column(3)
def print_column(height):
  for _ in range(height):
    print("#")
  # or
  print("#\n" * height, end="")
main()
def print_row(width):
  for _ in range(width):
    print("#")
  # or
  print("#\n" * width, end="")
main()
def main():
  print_square(3)
def print_square(size):
  for i in range(size): # for each row in square
    for j in range(size): # for each brick in row
      print("#", end="") # print brick
    print()

55. #print
hilarious = False
joke = "Czy to było to śmieszne? {}"
print(joke.format(hilarious)) # Czy to było śmieszne False
joke = "{} {} {} {}"
print(joke.format(1,2,3,"kiedy tak to tak")) # 1 2 3 kiedy tak to tak
print("when\ndo\nwe\neat")
# when
# do
# we
# eat     
"A" < "a" #True
"Adrian" < "Adrianna"#True
"adrian" < "Adrianna" #False
"Polska" == "Polski" #False
"Kiedy będzie obiad?".find("y") #1
kot = 2
kot # will print 2
dog = "yolo "
dog += "man" #yolo man

56. #Time
import time
time.perf_counter() #12:00:00:2186532
time.perf_counter() #12:00:00:8972611


57. 39 "key words"
False = #is accually just a zero
  print(int(False)) # = 0
True = #is accually just a one
  print(True + True) # = 2
None # just nothing
and # if both are correct then its True
as
  import math as m
  from random import randint as ri
  m.cos(10)
Assert
  limit: int=10
  n: int = 20
  assert n < limit, f'{n} is not less than the limit ({limit})' # if its okay it wont show up, when its false then we get AsserionError explained in f''
  # it just makes sure that the code above is working properly
import asyncio
  async def main() -> None:
  print('I am an asynchronous function!')
  if __name__ == '__name__':
  asyncio.run(main=main())
Graph
  import matplotlib.pyplot as plt
  import math as m
  import numpy as np
  fig, ax = plt.subplots()
  a = pow(10,4)
  a = 10
  b = 10
  x = np.linspace(-100,100,10**5)
  y = x**3
  ax.set_xlim(-100,100)
  ax.set_ylim(0,100)
  ax.scatter(x,y, c="#407", marker = "*",s = 20)
  z = 0
  ax.plot(z)
  plt.show()----------
  yrs = [2004 + x for x in range (16)]
  weights = [80, 81, 83, 85, 86, 89, 78, 79, 80,72,88,77,78,82,91,85]
  plt.plot(yrs, weights, c = "green", linestyle="--")
  plt.show()-----
  yrs = [2004 + x for x in range (16)]
  weights = [80, 81, 83, 85, 86, 89, 78, 79, 80,72,88,77,78,82,91,85]
  plt.bar(yrs, weights)        # individual towers
  plt.show()-----------
  ages = np.random.normal(20, 1.5,1000)
  print(ages)
  plt.hist(ages, bins=100)          #towers
  plt.show()----------
  ages = np.random.normal(20, 1.5,1000)
  print(ages)
  plt.hist(ages, bins=[ages.min(),18,21,ages.max()])      #towers
  plt.show()-----------
 ages = np.random.normal(20, 1.5,1000)
  print(ages)
  plt.hist(ages, bins=100, cumulative =True) #towers
  plt.show()--------------
  langs = ["Python", "C++", "Java", "C#", "Go"]
  votes = [21,45,112,4,14]
  plt.pie(votes, labels = langs) #circle
  plt.show()--------------
  langs = ["Python", "C++", "Java", "C#", "Go"]
  votes = [21,45,112,4,14]
  explodes = [0,0,0.05,0,0]  
  plt.pie(votes, labels=langs, explode=explodes) #circle with one part outwards
  plt.show()





