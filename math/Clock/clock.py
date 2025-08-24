import time
from playsound import playsound
CLEAR = "\033[2J" 
def print_and_delete(text):
    print(text, end='', flush=True)
    time.sleep(1)
    print('\r\033[K', end='', flush=True)
k, i = 1, 1
i1, i2 = 0, 0
user_input = input("Do you want a countdown or timer? (c/t/tf): ")
if user_input == "t":
    try:
        t1 = int(input("How many hours do you want?: "))
        t2 = int(input("How many minutes do you want?: "))
        t3 = int(input("How many seconds do you want?: "))
        print(CLEAR)
        print("---------------------------------------------------------------")
        while i1 < t1 or (i1 == t1 and i2 < t2) or (i1 == t1 and i2 == t2 and k <= t3):
            if k == 60:
                k = 0
                i2 += 1
            if i2 == 60:
                i2 = 0
                i1 += 1
            value = f"{i1:02d} hours, {i2:02d} minutes, {k:02d} seconds"
            print_and_delete(value)
            k += 1
        else:
            print("Time is up.")
            playsound("alarm.mp3")
    except ValueError:
        print("Are you stupid?")
elif user_input == "c":
    try:
        i1 = int(input("How many hours do you want?: "))
        i2 = int(input("How many minutes do you want?: "))
        k = int(input("How many seconds do you want?: "))
        print(CLEAR)
        print("---------------------------------------------------------------")
        while i1 != 0 or i2 != 0 or k != 0:
            if k == 0:
                k = 59
                if i2 != 0:
                    i2 -= 1
            if i1 != 0:
                if i2 == 0:
                    i2 = 59
                    if i1 != 0:
                        i1 -= 1
            value = f"{i1:02d} hours, {i2:02d} minutes, {k:02d} seconds"
            print_and_delete(value)
            k -= 1
        else:
            print("Time is up.")
            playsound("alarm.mp3")
    except ValueError:
        print("Are you stupid?")
elif user_input == "tf":
    print(CLEAR)
    while k > -1:
        if k == 60:
            k = 0
            i2 += 1
        if i2 == 60:
            i2 = 0
            i1 += 1
        value = f"{i1:02d} hours, {i2:02d} minutes, {k:02d} seconds"
        print_and_delete(value)
        k += 1
    else:
        print("Time is up.")
        playsound("alarm.mp3")
else:
    print("Kys.")
