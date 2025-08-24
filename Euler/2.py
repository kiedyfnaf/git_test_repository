'''
Question:
By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.
'''
sum = 0
term_1 = 1
term_2 = 1
while term_2 < 4000000:
    if term_2 %2 == 0:
        sum += term_2
    term_3 = term_1 + term_2
    term_1 = term_2
    term_2 = term_3
print(sum)