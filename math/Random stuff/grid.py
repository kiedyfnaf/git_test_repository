rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = (input("What symbol?: "))
for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
'''
import.math
s = {"1", "2", "3"}
for i in s:
    print(s.random)'''
'''cap = {'USA':'Wash', 'Pol':'dig', 'chin':'dog'}
print(cap['Pol']) # = dig
print(cap.get('chi'))'''

'''def shh(name, euler):
  print("Why?"+name+""+euler)
  print("Bruh")
pi = "Giga"
shh(pi, "")  # Why giga / Bruh
shh("Kid", "Uh") #Why kid uh/ bruh

def hello(fir,mid,las):
  print("Hello "+fir+" "+mid+" "+las)
hello(las="kod", mid="man", fir="bot")
text = "The {} jump {}."
print(text.format("cow", "moon"))
name = "Why"
cool = "dawg"
print("Hello, my name is {:10} cool".format(name)) # =Hello my name is why        cool.
print("Hello, my name is {:>10} cool".format(name)) # =Hello my name is       why cool.
print("Hello, my name is {name:10} cool".format(name)) # =Hello my name is    why    cool.
print("Hello, my name is {:^10} cool".format(name)) # =Hello my name is    why    cool.
import os
path = "C:\\Users\\bugal\\OneDrive\\Pulpit\\manga.txt" # Use double slashes
if os.path.exists(path):
  print("It does exist")
  if os.path.isfile(path):
    print("its a file")
else:
  print("It doesnt")
with open('C:\\Users\\bugal\\OneDrive\\Pulpit\\manga.txt') as file:
  print(file.read())'''
text = "Why\nSome text\nKid" # this \n means new line
with open('mana.txt', 'w' ) as file:
  file.write(text)
