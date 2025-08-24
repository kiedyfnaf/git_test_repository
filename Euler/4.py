'''
Question:
Find the largest palindrome made from the product of two 
3-digit numbers.
'''
num_1 = 999
num_2 = 999
win=0
list = []
while num_1 != 499:
    if num_2 == 499:
        num_1 -= 1
        num_2 = 999
    pali = str(num_1 * num_2)
    print(pali)
    leng = len(pali)/2
    if leng != int(leng):
        leng -= 1/2
    count = 0
    for i in range(int(leng)):
        if pali[i] == pali[len(pali)-(i+1)]:
            count += 1
        if count == leng:
            list.append(num_1 * num_2)
    num_2 -= 1
print(f"Biggest is {max(list)}")


