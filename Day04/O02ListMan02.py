"""
'append', 'clear', 'copy', 'count', 'extend',
'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
"""


lst1 = [1, 2, 3, 4, 5]
print(f"lst1 ;{lst1}")

# we cannot add a new element without a function
lst1[4] = 4.5
# lst1[5] = 6
print(f"lst1 :{lst1}")

print("-" * 40)
# delete a value from the list
print(f"lst1 :{lst1}")
del lst1[1]
print(f"lst1 :{lst1}")

print("-" * 40)
lst1 = [1, 2, 3, 4.5, 5.3, 6.4, 'seven', 'eight', 'nine']
print(f"lst1 :{lst1}")

print(f"lst1[0]\t\t{lst1[0]}\t\t{id(lst1[0])}")
print(f"lst1[1]\t\t{lst1[1]}\t\t{id(lst1[1])}")
print(f"lst1[2]\t\t{lst1[2]}\t\t{id(lst1[2])}")
print(f"lst1[3]\t\t{lst1[3]}\t\t{id(lst1[3])}")

print("-" * 40)
print(dir(lst1))

# add elements into a list

print("{:-^40}".format("append"))
lst1 = [1, 2, 3, 4, 5]
print(f"lst1 :{lst1}")

lst1.append(6)
lst1.append(7)
lst1.append(8)
print(f"lst1 :{lst1}")

lst1.append([9, 10, 11, 12, 13])
print(f"lst1 :{lst1}")
print(lst1[8][1:4])

# add more than one element at a shot
print("extend".center(40, "-"))
lst1 = list(range(1, 6))
print(f"lst1 :{lst1}")

lst1.extend([6, 7, 8])
print(f"lst1 :{lst1}")

lst1.extend([9, 10, 11, 12])
print(f"lst1 :{lst1}")

# insert elements in a specific location
lst1 = list(range(1, 6))
print(f"lst1 :{lst1}")
lst1.insert(1, 1.5)
lst1.insert(3, 2.5)
lst1.insert(5, 3.5)
lst1.insert(7, 4.5)

print(f"lst1 :{lst1}")
print(len(lst1))

lst1.insert(10, 6.5)
print(f"lst1 :{lst1}")

lst1.insert(15, 10.5)
print(f"lst1 :{lst1}")
print(len(lst1))
