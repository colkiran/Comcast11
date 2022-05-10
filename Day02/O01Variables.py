
Player_count = 11
rating = 8.5
has_won_world_cup = True
team_name = "India"

print(Player_count)
print(rating)
print(has_won_world_cup)
print(team_name)

print("-" * 40)
print(__name__)         # double underscores    => dunder name

print("-" * 40)
a, b, c = 1, 2, "hello"
print(f"a = {a} , b = {b}, c = {c}")                # interpolation

print("-" * 40)

first_name = "Sachin"
last_name = "Tendulkar"
print("My name is " + first_name + " and I am more familiar as " + last_name)           # concatenation
print(f"My name is {first_name} and I am more familiar as {last_name}")                 # Interpolation

a = 1
b = 1
print(a + b)

a = "hello"
b = "world"
print(a + b)

print("-" * 40)
a = "hello"
b = 20
print(a + str(b))               # type casting

print("-" * 40)
# interpolation
nm1 = "Sachin"
nm2 = "Rahul"
st = f"Hello {nm1}, Hai {nm2}"
print(st)

print(f"{nm1} is the best in the world with a rating of {1 + 2 + 3 + 3 + 0.6}")

print(f"{nm1}'s top score in ODI is 205")
print(f"{nm1}'s top score in ODI is 205")
print(f'{nm1}\'s top score in ODI is 205')



