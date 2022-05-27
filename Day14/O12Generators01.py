
from sys import getsizeof

val1 = [x ** 2 for x in range(1, 11)]                     # comprehensions
print(f"val1 :{val1}")
print(type(val1))
print("-" * 40)

val2 = (x ** 2 for x in range(1, 11))
print(f"val2 :{val2}")
print(type(val2))
print("-" * 40)

print("#" * 40)

val3 = [x ** 2 for x in range(1, 10000)]
val4 = (x ** 2 for x in range(1, 10000))

print(f"Comprehension size of val3 :{getsizeof(val3)}")
print(f"Generator size of val4     :{getsizeof(val4)}")
