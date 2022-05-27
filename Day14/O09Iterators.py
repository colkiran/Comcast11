
l = [1, 2, 3, 4, 5]
print(f"l :{l}")
print(type(l))
print("-" * 40)
print(dir(l))

itrObj = l.__iter__()
print(itrObj)
print("-" * 40)
print(dir(itrObj))                  # __iter__(), __next__() protocols of iteration
print("-" * 40)

print(itrObj.__next__())
print(itrObj.__next__())
print(itrObj.__next__())
print(itrObj.__next__())
print(itrObj.__next__())
# print(itbObj.__next__())
print("-" * 40)

for i in l:
    print(i)
