
"""

1. int
2. float
3. complex

"""
a = 10
b = -10

print(type(a))              # RTTI - Run Time Type Indentification
print(f"a :{a}")
print(type(b))
print(f"b :{b}")

print("-" * 40)

c = 10.0
d = -10.0

print(type(c))
print(f"c :{c}")
print(type(d))
print(f"d :{d}")

print("-" * 40)

e = +2e3
f = -2e3

print(type(e))
print(f"e :{e}")
print(type(f))
print(f"f :{f}")

print("-" * 40)

g = 2 + 4j
h = 2 - 4j
print(type(g))
print(f"g :{g}")
print(type(h))
print(f"h :{h}")

print("-" * 40)
print(max(34, 78, 98))
print(min(34, 78, 98))

print("-" * 40)
x = 2 + 3.5
print(type(x))
print(f"x :{x}")

print("-" * 40)
x = 1
y = 2.5
z = x + y
print("x :",type(x))
print("y :",type(y))
print("z :",type(z))

print("conversion".center(40, "-"))
a = -10
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{complex(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(40, "-"))
print(11)           # decimal
print(0b11)         # binary
print(0b101)        # binary
print(0o11)         # octal
print(0o111)        # octal
print(0xe)          # hexa
print(0xa)          # hexa

print("Number System Conversion".center(50, "-"))
a = 100
print(f"a :{a}")
print("Binary :", bin(a))
print("Hexa   :", hex(a))
print("Octal  :", oct(a))
