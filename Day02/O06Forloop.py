
for i in range(10):
    print(i, end=" ")
print()

print("-" * 40)

for i in range(10, 0, -1):
    print(i, end=" ")
print()

print("-" * 40)

for i in range(1, 26):
    if i % 2 == 0:
        continue
    # if i >= 18:
    #     break
    print(i, end=" ")
else:
    print("\ncompleted generating numbers")
print()



