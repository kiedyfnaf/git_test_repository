'''
Question:
What is the largest prime factor of the number: 600851475143 
'''
list = []
number = 600851475143
divisor = 2
something = divisor - 1
while divisor <= number:
    if number % divisor == 0:
        number /= divisor
        list.append(divisor)
    divisor += 1
print(max(list))
