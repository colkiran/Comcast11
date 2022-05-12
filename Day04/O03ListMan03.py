
# delete elements from a list
print("pop".center(40, "-"))
lst1 = [1, 2, 3 ,4, 5, 6, 7, 8, 9]
print(f"lst1 :{lst1}")

res = lst1.pop(3)
print(f"res :{res}")
print(f"lst1 :{lst1}")

res = lst1.pop()
print(f"res :{res}")
print(f"lst1 :{lst1}")

print("remove".center(40, "-"))
lst1 = [1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 3, 1, 2, 3, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2]
print(f"lst1 :{lst1}")
res = lst1.remove(1)
print(f"res :{res}")
print(f"lst1 :{lst1}")

lst1 = [1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 3, 1, 2, 3, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2]

while True:
   try:
       lst1.remove(1)
   except ValueError:
       break

print(f"lst1 :{lst1}")

print("clear".center(40, "-"))
lst1 = list(range(1, 11))
print(f"lst1 :{lst1}")
lst1.clear()

print(f"lst1 :{lst1}")

print("count".center(40, "-"))
lst1 = [1, 2, 3, 1, 2,1,1, 2, 1, 2, 2, 1,1,1, 3, 1,3, 1, 1, 3, 2, 1,1]
print(f"lst1 :{lst1}")
print(f"1 :{lst1.count(1)}")
print(f"2 :{lst1.count(2)}")
print(f"3 :{lst1.count(3)}")
print(f"6 :{lst1.count(6)}")

print("index".center(40, "-"))
lst1 = [1, 2, 3, 1, 2, 1, 1, 2, 1, 2, 2, 1, 1, 1, 3, 1, 1, 1, 3, 2, 1, 1]
print(f"lst1 :{lst1}")
print(lst1.index(1))
print(lst1.index(3))
print(lst1.index(3, 4))
print(lst1.index(3, 15))
# print(lst1.index(3, 19))
