
"""
'clear', 'copy', 'fromkeys', 'get', 'items', 'keys',
 'pop', 'popitem', 'setdefault', 'update', 'values

"""

print("{:-^50}".format("get"))
player = {'name': 'Sachin', 'runs': 85, 'oppn': 'Aus', 'venue': 'chepauk', 'year': 2010}
print(f"player :{player}")
print(player.get('oppn',  "Please enter a valid key..."))
print(player.get('age', "Please enter a valid key..."))

print("keys".center(40, "-"))
player = {'name': 'Sachin', 'runs': 85, 'oppn': 'Aus', 'venue': 'chepauk', 'year': 2010}
print(f"player :{player}")

ky = player.keys()
print(f"ky :{ky}")
print(type(ky))

print("-" * 40)
for ky in player.keys():
    print(ky + " => " + str(player[ky]))
print("-" * 40)

print("values".center(40, "-"))
player = {'name': 'Sachin', 'runs': 85, 'oppn': 'Aus', 'venue': 'chepauk', 'year': 2010}
print(f"player :{player}")

vl = player.values()
print(f"values :{vl}")

print("fromkeys".center(40, "-"))
cities = ['blr', 'che', 'mum', 'del', 'kol', 'hyd', 'pun', 'mdr']
print(f"cities :{cities}")

# convert the list into a dictionary
res_dict1 = dict.fromkeys(cities)
print(res_dict1)

res_dict2 = dict.fromkeys(cities, 24)
print(res_dict2)

print("setdefault".center(40, "-"))
# add only new key value pairs into the dictionary
player = {'name': 'Sachin', 'runs': 85, 'oppn': 'Aus', 'venue': 'chepauk', 'year': 2010}
print(f"player :{player}")
player.setdefault('runs', 137)
player.setdefault('venue', 'Gaba')

player.setdefault('age', 37)
print(f"player :{player}")

print("pop".center(40, "-"))
player = {'name': 'Sachin', 'runs': 85, 'oppn': 'Aus', 'venue': 'chepauk', 'year': 2010}
print(f"player :{player}")

res = player.pop('oppn')
print(f"res :{res}")
print(f"player :{player}")

print("popitem".center(40,  "-"))
player = {'name': 'Sachin', 'runs': 85, 'oppn': 'Aus', 'venue': 'chepauk', 'year': 2010}
print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")
print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")
print(f"player :{player}")
