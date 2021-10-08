# Question 10
import numpy as np
print("How many numbers to enter")
list = []
n = int(input())
print("Enter the numbers")
for i in range(n):
    temp =int( input())
    list.append(temp)
ma = np.max(np.array(list))
mi = np.min(np.array(list))
print("maximum=",ma)
print("minimum=",mi)