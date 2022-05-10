"""
1. Arithmetic
2. Relational or Comparison
3. Logical
4. Augmentor
5. Bitwise
6. Ternary

"""

print("Arithmetic Operators".center(40, "-"))
print(f"10 + 3 = {10 + 3}")
print(f"10 - 3 = {10 - 3}")
print(f"10 * 3 = {10 * 3}")
print(f"10 / 3 = {10 / 3}")
print(f"10 // 3 = {10 // 3}")
print("-" * 40)
print(f"10 % 3 = {10 % 3}")
print(f"10 ** 3 = {10 ** 3}")


print("Augmentor".center(40, "-"))
# =, +=, -=, /=, *=

x = 10
print(f"x :{x}")
x += 3              # x = x + 3
print(f"x :{x}")
print("-" * 40)
x //= 3
print(f"x :{x}")

print("Comparison".center(40, "-"))
# ==, >=, <=, !=
a = 10
b = 20

print(f"a == b :{a == b}")
print(f"a >= b :{a >= b}")
print(f"a <= b :{a <= b}")
print(f"a != b :{a != b}")

print("logical".center(40, "-"))
# and, or, not
a = 10
b = 20
print(a <= b and b >= a)
print(a <= b and a >= b)

print(a <= b or a >= b)
print(a == b or b >= a)

print(not(a == b or b >= a))
print(not(a <= b and a >= b))

print("-" * 40)
print(ord("a"), ord("A"))           # integer representation of Unicode Character
print(ord("z"), ord("Z"))
print("apple" > "orange")
print("apple" < "orange")

print("Bitwise Operators".center(40, "-"))

print(5 | 3)
print(5 & 3)
print(5 ^ 3)
print(5 << 1)
print(8 << 1)
print(5 >> 1)
print(int("0010", 2))

print(~0)
print(~5)

"""
OR operator
5 - 0101
3 - 0011
    0111  -  7
    
0101 => 1010
1000 => 10000

0101 => 0010

~ = negation (convert 0 to 1 and 1 to 0)
0000 => 1111 = -1
0101 => 1010 = -6

"""
print("ternary".center(40, "-"))

a = 18
print("Elgible" if a >= 18 else "Not Eligible")
