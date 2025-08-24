import random

MAX_LINES = 3  
MAX_BET = 100
MIN_BET = 1
stop = "_____________________________"

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def winnings_get(columns, lines, bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def start_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column= []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row])

def deposit():
    while True:
        amount = input(stop + "\nWhat would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(stop +"\nAre you stupid :D?")
        else:
            print(stop +"\nEnter a number.")
    return amount

def get_lines():
    while True:
        lines = input(stop + "\nHow many lines? (1-" + str(MAX_LINES) + ")? : ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print(stop +"\nAre you stupid :D?")
        else:
            print(stop +"\nEnter a number.")
    return lines

def get_bet():
    while True:
        amount = input(stop +"\nWhat would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <=MAX_BET:
                break
            else:
                print(stop + f"\nHas to be between ${MIN_BET} - ${MAX_BET}?")
        else:
            print(stop +"\nEnter a number.")
    return amount    

def spin(balance):
    balance = deposit()
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(stop + f"\nYou are too broke for that. You have: ${balance}"+ "\nTry again.")
        else:
            break
    print(stop + f"\nYou are betting ${bet} on {lines} lines. Total bet: {total_bet}")
    slots = start_spin(ROWS, COLS, symbol_count)
    print_slot(slots)
    winnings, winning_lines = winnings_get(slots, lines, bet, symbol_value)
    print(f"You won {winnings}.")
    print(f"You won on line:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play (q to quit). : ")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")

main()