math = []
train = ['X','X','X']
english = ['X','X','X']
physics = ['X','X','X']
photo= ['X','X','X']
lecture = []
language = ['X']
clouds = []
els_e = ['X']
# ,'X'
lis = [math, train, english, physics, photo, lecture, language, clouds, els_e]
dog = ["math", "train", "english", "physics", "photo", "lecture", "language", "clouds", "something else"]
k = input("Do you want to check or place?: ")
if k == "place":
    
    for i in range(len(lis)):
        (lis[i]).clear()
        user = input(f"Have you learned {dog[i]} today?")
        if user == "yes":
            lis[i].append("X")
    for i in range(len(lis)):
        print(lis[i])
if k == "check":
    for i in range(len(lis)):
        print(f"{dog[i]}: {len(lis[i])}")     
else:
    print("Are you stupid or what?")    

    

