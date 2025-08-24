'''
Question:
What is the 10,001-st prime?
'''
sum = 0
number = 1
while number< 2000000:
    number += 1
    divisors = 0
    for i in range (number):
        if number % (i+1) == 0:
            divisors += 1
    if divisors == 2:
        print(number)
        sum += number
print(sum)