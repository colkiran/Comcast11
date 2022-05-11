
a = 1
while True:
    print(a, end=" ")
    a += 1
    if a > 10:
        break
print()

print("-" * 40)
print(f"After :{a}")

while a > 0:
    print(a, end=" ")
    a -= 1
print()
