
a = int(input("Enter the first number :"))
print(type(a))
print(f"a :{a}")

if a < 10: print(f"a is a single digit number :{a}")

b = int(input("Enter the second number :"))
c = int(input("Enter the third number :"))
print(f"b :{b}")
print(f"c :{c}")

if (a >= b and a >= c):
    print(f"a is the greatest :{a}")
elif (b >= a and b >= c):
    print(f"b is the greatest :{b}")
else:
    print(f"c is the greatest :{c}")
