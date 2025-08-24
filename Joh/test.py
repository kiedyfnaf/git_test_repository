import time

def print_letter_by_letter(message, delay=0.1):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(delay)

# Example usage
print_letter_by_letter("Warning, the script you made seems to have some problems \nand it might sometimes make decisions for itself, if you want to change that cli", 0.1)
time.sleep(3)
print_letter_by_letter(".....", 1)
time.sleep(2)
print_letter_by_letter("There is no need for that", 0.3)