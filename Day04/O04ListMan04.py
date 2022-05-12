
print("copy".center(40, "-"))
lst1 = [1, 2, 3, 4, 5]
print(f"lst1 Before :{lst1}")
lst2 = lst1                     # shallow copy - we are copying the address along with data
print(f"lst2 Before :{lst2}")

print("-" * 40)
lst2.append(6)
lst2.append(7)
lst2.append(8)

print(f"lst2 After :{lst2}")
print(f"lst1 After :{lst1}")

print("-" * 40)
lst3 = [5, 6, 7, 8, 9, 10]
print(f"lst3 Before :{lst3}")

lst4 = lst3.copy()
print(f"lst4 Before :{lst4}")

lst4.extend([7, 8, 9, 10])
print(f"lst4 After :{lst4}")
print(f"lst3 After :{lst3}")

print("-" * 40)
lst5 = [1, 2, 3, 4, [10, 20, 30, 40, 50], 5]
print(f"lst5 :{lst5}")
lst6 = lst5.copy()
print(lst5[4])

print("-" * 40)
lst6[4].insert(1, 15)
lst6[4].insert(3, 25)
lst6[4].insert(5, 45)
lst6[4].insert(7, 55)

print(f"lst6 After :{lst6}")
print(f"lst5 After :{lst5}")

print("-" * 40)
from copy import deepcopy

lst7 = [1, 2, 3, ['a', 'b', 'c', 'd', 'e'], 4, 5]
print(f"lst7  Before :{lst7}")
lst8 = deepcopy(lst7)
print(f"lst8 Before :{lst8}")

print("-" * 40)
lst8[3].append("f")
lst8[3].append("g")
lst8[3].append("h")
print(f"lst8 After :{lst8}")
print(f"lst7 After :{lst7}")
