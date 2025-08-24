import turtle
import time
import random
import math

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'cyan', 'blue', 'black', 'brown', 'orange', 'violet', 'pink', 'gray']

def get_numer_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Are you stupid?. Again")
            continue
        if 2 <= racers <= 10:
            return racers
        else:
            print("I said (2 - 10).")
        return racers

def race(colors):
    turtles = create_turtles(colors)
    color_to_turtle = {t.color()[0]: t for t in turtles}
    while True:
        random.shuffle(turtles)  # Shuffle turtles before moving
        for racer in turtles:
            distance = random.randrange(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT//2 - 29:
                return racer.color()[0]  # Return the color of the winning turtle
            elif abs(x) == (WIDTH)//2 + 20:
                racer.right(180)

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // len(colors)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        if i < racers:
            racer.setpos(-(WIDTH)//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)
    racer.speed(0)
    racer.color('red')
    racer.penup()
    racer.setpos(-(WIDTH)//2 + 20, HEIGHT//2 - 30)
    racer.pendown()
    racer.right(90)
    racer.speed(2)
    racer.forward(460)
    racer.hideturtle()
    racer.right(180)
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Racing.")

racers = get_numer_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers +1]

winner = race(colors)
print(f"The winner is the color: {winner}")
time.sleep(5)
