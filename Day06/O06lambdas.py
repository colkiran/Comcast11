
"""
result_of_expression = lambda var1, var2, var3... : expression(using the variables)

"""

def add(x, y):
    return x + y

a = add
print(a(10, 20))

print("-" * 40)
b = lambda x, y: x + y
print(b(10, 20))

# lambdas are best used with these functions - map, filter, reduce
l = list(range(1, 11))

sqrNum = list(map(lambda x: x ** 2, l))
print(f"squares :{sqrNum}")

# conversion of temperature, currencies
# convert the temperature from celsius to farenheit
t = [23, 25, 28.7, 18.5, 20, 30.2, 34.6, 36, 40]
fehren=list(map(lambda x:(x*9/5)+32,t))
print(fehren)

print("-" * 40)
print("-" * 40)
print("-" * 40)
# use sort or sorted function of lists and sort the months as they appear in the calendar
months = ['dec', 'aug', 'oct', 'apr', 'feb', 'nov', 'jan', 'sep', 'may', 'mar', 'jul', 'jun']

from calendar import month_name
def month_sort(mth):
    mon = []
    for m in list(month_name):
        mon.append(m[0:3].lower())
    if mth in mon:
        return mon.index(mth)


print(f"months :{months}")
res = sorted(months, key=month_sort)
print(f"sorted :{res}")

print("-" * 40)
print("-" * 40)

sorted_lst = sorted(months, key=list(map(lambda mn: mn[0:3].lower(), list(month_name))).index)
print(f"sorted_lst :{sorted_lst}")

print("-" * 40)
print("-" * 40)

print("filter".center(40, "-"))
l = list(range(1, 25))
print(f"l :{l}")

res = list(filter(lambda x: x % 3 == 0, l))
print(f"res :{res}")

print("reduce".center(40, "-"))

from functools import reduce
l = [8, 1, 4, 7, 3, 6, 9, 2, 5, 11, 10]
print(f"l :{l}")

res = reduce(lambda x, y: x if x > y else y, l)
print(f"res :{res}")

res = reduce(lambda x, y: x + y, l)
print(f"res :{res}")
