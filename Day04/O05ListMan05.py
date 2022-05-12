"""
a. sort     => will sort the original list
b. sorted   => will take a copy of the list and sort it

"""

lst1 = [10, 5, 8, 6, 9, 1, 4, 2, 7, 3]
print(f"lst1 :{lst1}")

asc_res = sorted(lst1)
print(f"Ascending order :{asc_res}")
desc_res = sorted(lst1, reverse=True)
print(f"Descending order :{desc_res}")
lst1.sort()
print(f"lst1 :{lst1}")

lst1 = [10, 'zebra', 'apple', 5, 'yellow', 'blue', 8, 'x mas', 'green', 6, 'violet', 'magenta' ,
        9, 'pink', 'snake', 1, 'cat', 'dog', 4, 'king', 'queen', 2, 297, 28, 2687, 20987, 7, 3,
        38, 365, 3164,  49, 450, 4067]

# intlst1 = sorted([i for i in lst1 if type(i) is int])
# strlst1 = sorted([i for i in lst1 if type(i) is str])
# print(intlst1+strlst1)

res = sorted(lst1, key=ascii)
print(f"res :{res}")

print("-" * 40)
cities = ['kaynakumari', 'chennai', 'vishakapatnam', 'bangalore', 'hyderabad', 'thiruvananthapuram',
          'ooty', 'mysore', 'mumbai', 'delhi', 'kolkotta', 'pune', 'vijayawada']
print(f"cities :{cities}")

# sort the cities by the number of characters

res = sorted(cities, key=len)
print(f"res :{res}")
