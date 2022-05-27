
numbers = [1, 2, 3, 4, 5]
iterObj = iter(numbers)

while True:
    try:
        elem = next(iterObj)
        print(elem)
    except StopIteration:
        break

print("-" * 40)
st = "Hello World"
print(st)
print("-" * 40)

for x in st:
    print(x, end=" ")
print()

