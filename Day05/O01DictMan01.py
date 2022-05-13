
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'Sachin'), ('runs', 120), ('oppn', 'Nzl'), ('venue', 'auckland')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name="Rahul", runs=79, oppn="WI", venue="sabina park")
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
# crud
player = {'name': 'Sachin', 'runs': 85, 'oppn': 'Aus', 'venue': 'chepauk'}
print(f"player :{player}")
print("-" * 40)
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")
print(f"Opponent :{player['oppn']}")

print("-" * 40)
# add a new key value pair
player['year'] = 2014
player['runs'] = 75
print(f"player :{player}")

print("-" * 40)
del player['venue']
print(f"player :{player}")

print("-" * 40)
# iterate
for x in player:
    print(x,"\t",player[x])

print("-" * 40)
d1 = {'a': 'apple', 'b': 'ball', 'c': 'cat', 'd': 'dog'}
print(f"d1 :{d1}")

d2 = {1: 'one', 2:'two', 3: 'three', 4: 'four', 5: 'five'}
print(f"d2 :{d2}")

d3 = {1: d1, 2 :d2}
print(f"d3 :{d3}")

print("-" * 40)
# unpack
d4 = {**d1, **d2}
print(f"d4 :{d4}")

print("-" * 40)
d0 = {'a': 'america', 'b': 'brazil', 'c': 'china', 'd': 'denmark'}
d5 = {**d1, **d0}
print(f"d5 :{d5}")

print("-" * 40)
print(f"d0 :{d0}")

print(d0.get('b'))
print(d0.get('e'))

print("-" * 40)
print(dir(d1))

