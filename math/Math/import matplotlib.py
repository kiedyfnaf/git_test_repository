import matplotlib.pyplot as plt
import math as m
import numpy as np
langs = ["Python", "C++", "Java", "C#", "Go"]
votes = [21,45,112,4,14]
explodes = [0,0,0.05,0,0]  
plt.pie(votes, labels=langs, explode=explodes) #circle with one part outwards
plt.show()
