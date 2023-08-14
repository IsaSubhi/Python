# imports
import math
import random


# fuction definitions
def multiply_by_random(num):
    return num * random.randint(MIN, MAX)


# main
x = 5
y = 7
MIN = 5
MAX = 20
z = multiply_by_random(x)
print(z)
