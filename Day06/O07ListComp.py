
fruits = [
    ('apple', 290),
    ('oranges', 60),
    ('grapes', 135),
    ('pineapple', 80),
    ('watermelon', 75),
    ('gauva', 90),
    ('strawberry', 380)
]

print(f"fruits :{fruits}")

print("-" * 40)
prices = ["fruit" for fruit in fruits]
print(f"pirces :{prices}")

print("-" * 40)
prices = [fruit for fruit in fruits]
print(f"prices :{prices}")

print("-" * 40)
prices = [fruit[0] for fruit in fruits]
print(f"prices :{prices}")

print("-" * 40)
prices = [fruit[1] for fruit in fruits]
print(f"prices :{prices}")

print("-" * 40)
prices = [fruit[1] * 0.9 for fruit in fruits]
print(f"prices :{prices}")

print("-" * 40)
prices = [fruit[1] * 0.75 for fruit in fruits]
print(f"prices :{prices}")

print("-" * 40)
prices = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit in fruits]
print(f"prices :{prices}")

print("-" * 40)
prices = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit in fruits if fruit[1] > 100]
print(f"prices :{prices}")
