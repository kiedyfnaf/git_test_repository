'''
number = 0
divisors = 1
while divisors < 500:
    number += 1
    print(number)
    sum = (number)*(number+1)/2
    divisors = 0
    for i in range (number):
        if number % (i+1) == 0:
            divisors += 1
print(number)
'''
from math import gcd
from sympy import divisor_count

# Function to calculate the first triangle number with over 500 divisors
def find_triangle_number_with_divisors(limit):
    n = 1
    triangle_number = 0
    while True:
        # Calculate the n-th triangle number
        triangle_number += n
        
        # Count divisors of the triangle number
        if divisor_count(triangle_number) > limit:
            return triangle_number
        
        n += 1

# Find the first triangle number with more than 500 divisors
result = find_triangle_number_with_divisors(500)
print(result)