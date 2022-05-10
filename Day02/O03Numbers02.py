
import random

print(random.random())
print(random.random())
print(random.random())
print("-" * 40)

print(random.randint(1, 50))
print(random.randint(1, 50))
print(random.randint(1, 50))

print("-" * 40)
lst = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(random.choice(lst))
print(random.sample(lst, 3))
print(random.sample(lst, 3))
print(random.sample(lst, 3))

print("-" * 40)
import math
print("Ceil 2.1 :", math.ceil(2.1))
print("Ceil 2.4 :", math.ceil(2.4))
print("Ceil 2.6 :", math.ceil(2.6))

print("-" * 40)
print("floor 2.1 :", math.floor(2.1))
print("floor 2.5 :", math.floor(2.5))
print("floor 2.8 :", math.floor(2.8))

print("5! = ", math.factorial(5))

print("-" * 40)
print(int(3.2))

print(math.sqrt(9))
from math import sqrt
print(sqrt(9))

print("-" * 40)
import cmath

print(cmath.sqrt(-1))

print((1 + 3j) * (3 + 4j))
print((1 + 3j) + (3 + 4j))
