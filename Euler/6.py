'''
Question: The sum of the squares of the first ten natural numbers is 385,
The square of the sum of the first ten natural numbers is 3025
Hence the difference between the sum of the squares of the first
 ten natural numbers and the square of the sum is 2640

Find the difference between the sum of the squares of the first
 one hundred natural numbers and the square of the sum.
'''
sum = 0
square = 0
for i in range(100):
    sum += (i+1)**2
for a in range(100):
    square += a+1
square = square**2
print(square-sum)