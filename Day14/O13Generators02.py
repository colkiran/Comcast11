
def fun():
    n = 1
    print("apples from Ooty")
    yield n
    n += 9
    print("Oranges from Kanpur")
    yield n
    n += 10
    print("Grapes from Hubli")
    yield n

res = fun()
print(type(res))
print(f"res :{res}")

print(res.__next__())
print(res.__next__())
print(res.__next__())

print("-" * 40)

def get_val():
    for i in range(1, 11):
        yield i

res = get_val()
print(next(res))
print(next(res))
print(next(res))

for i in get_val():
    print(i, end=" ")
print()