'''
Question:
What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
'''
number = 2519
win = 0
# Its always divisible by 1 so we dont need it
# If its divisible by 4 and 5 it has to be divisible by 20 so dont need to check it too
# Same case with 2*9 = 18, no need for 18
# Same for 6,10,12,14,15
# Now dont need to check for 3 if we check 9
# Same goes for 2,4,8 cause we check 16
# And so we end up with these
# As all except one are prime they wont interfere
# So just do 5*7*9*11*13*16*17*19
# This is a math way to do it but i wrote the code anyway
list = [5,7,9,11,13,16,17,19] 
while win != 8:
    print(number)
    win = 0
    number += 1
    for i in range(len(list)):
        reminder = number % (list[i])
        if reminder == 0:
            win += 1
print(number)