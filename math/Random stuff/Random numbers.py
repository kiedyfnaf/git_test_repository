import random
l = []
f = ""
n = 1
try:
    f = int(input("How many numbers: "))
except ValueError:
    print("Dont do that.")
else:
    with open('cheese.txt', 'a') as file:
        while n <= f:
            k = [str(random.randint(1,7))]
            l.append(k)
            n = n + 1
        file.write("\nNumbers are: {}".format(l))

