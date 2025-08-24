import random
import math
import time
import pygame
import os
hp = 2
# Start
k = True
def letter(message, delay=0.1):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)
def start(name):
    path = "script.py"
    if os.path.exists(path):
        name = ("Please enter your name")
        print(f"Welcome to Joh {name} .\n")
        inpu = input("Do you want an introduction? (ye/no)")
        if inpu == "ye":
            letter("Warning, the script you made seems to have some problems \nand it might sometimes make decisions for itself, if you want to change that cli.....\nThere is no need for that so enjoy a game my very valuable player")
            

        time.sleep(1)
    else:
        print("Please create a file named 'script.txt' before starting a game.") 

inpu = input("Do you want an introduction? (ye/no)")

def clock(tick=0):
    if k == True:
        time.sleep(1)
        tick += 1

    

start("Jan")
def main():
    run = True
    while run:
        clock(0)
    

main()
print("Man")

# dictionary of inputs and later i will call for them given their key
# on the mountain and desert if you dont take action in less than 2 min you die.        



# Player movement

# Player actions
    
# Environment

# Hp
    
# Items
    
# Enemies
    
# Rest
    
# Loot
    
# Npc's
    
# Likeability
    
# Fame

# Team mates
    
# Instruction
    
# Stats
    
# Random action
    
# Fights
    
# Effects
    
# Smith
    
# Wall street
    
# Casino




class Player():

    def main(window):
        clock = pygame.time.Clock()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
            player.loop(FPS)
            handle_move(player)
            draw(window, background, bg_image, player)
        pygame.quit()
        quit()