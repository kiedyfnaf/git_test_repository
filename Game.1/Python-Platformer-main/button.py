import time
import random
from pynput import keyboard

questions = [
    "Kiedy urodził się Jan Paweł 2? ",
    "Jak umarł Putin?: ",
    "Kiedy padły wieże?: "
]

# The key combination to check
COMBINATIONS = [
    {keyboard.KeyCode(char='s')},
    {keyboard.Key.shift, keyboard.KeyCode(char='A')},
    {keyboard.KeyCode.from_char(' ')}  # Added space key
]

# The currently active modifiers
current = set()

def execute():
    print(random.choice(questions))
    time.sleep(1)

def on_press(key):
    if any(key in combo for combo in COMBINATIONS):
        current.add(key)
        if any(all(k in current for k in combo) for combo in COMBINATIONS):
            execute()

def on_release(key):
    if any(key in combo for combo in COMBINATIONS):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

        