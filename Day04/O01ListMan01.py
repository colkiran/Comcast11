
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)

l2 = [1, 2, 3, 'four', 'five', 'six', 7.1, 8.9, 9.4, True, False, 3+5j]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
values = list(range(10, 31, 10))
print(f"values :{values}")

# unpack list
a, b, c = values
print(a, b, c, sep=", ")
values = list(range(10, 101, 10))
print(values)
a, b, *c = values
print(a, b, c, sep=", ")

print("-" * 40)
*a, b, c = values
print(a, b, c, sep=", ")

print("-" * 40)
a, *b, c = values
print(a, b, c, sep=", ")

print("-" * 40)
lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]
lst3 = [lst1, lst2]
print(lst3)
print(len(lst3))

print("-" * 40)
lst3 = [*lst1, *lst2]
print(lst3)
print(len(lst3))

print("-" * 40)
letters = ['a', 'b', 'c', 'd', 'e']
print(f"letters :{letters}")

for letter in letters:
    print(letter, end=" ")
print()

print("-" * 40)
print(list(enumerate(letters)))

for letter in enumerate(letters):
    print(letter, end=" ")
print()

print("-" * 40)
for letter in enumerate(letters):
    print(letter[0], letter[1])

print("-" * 40)
for (index, letter) in enumerate(letters):
    print(index, letter)

print("-" * 40)
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"my_list :{my_list}")

print("-" * 40)
for lst in my_list:
    print(lst)

print("-" * 40)
print(list(enumerate(my_list)))

for index, lst in enumerate(my_list):
    print(f"List({index})")
    for idx, num in enumerate(lst):
        print(f"\t{idx}\t{num}")
