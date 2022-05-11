
# Conversions
print("Conversions".center(40, "-"))
print("{val} {val} {val}".format(val="A"))
print("{val!s} {val!r} {val!a}".format(val="A"))

print("-" * 40)
print("The number {num} {num} {num}".format(num = 36))
print("The number {num} {num:f} {num:b}".format(num = 36))
print("The number {num:10} {num:f} {num:b}".format(num = 36))
print("The number {num:5} {num:f} {num:b}".format(num = 36))
print("The number {num:5} {num:f} {num:b}".format(num = 36987023))
print("The number {num:10} {num:f} {num:b}".format(num = 36))

print("Alignment".center(40, "-"))
print("{num:15}Tendulkar".format(num = 36))
print("{num:15}Tendulkar".format(num = "Sachin"))
print("{}".format("Sachin Tendulkar"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

print("-" * 40)
from math import pi
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))

print("One googol is {}".format(10 ** 100))
print("One googol is {:,}".format(10 ** 100))

print("Alignment".center(40, "-"))
print("{}".format(pi))
print("{pi:10.3}".format(pi = pi))
print("{pi:010.3}".format(pi = pi))
print("{pi:010.4}".format(pi = pi))
print("{pi:010.5}".format(pi = pi))

print("Alignment".center(40, "*"))
print("{}".format(pi))
print("{:10.2f}Sachin".format(pi))
print("{:<10.2f}Sachin".format(pi))             # left alignment
print("{:>10.2f}Sachin".format(pi))             # right alignment
print("{:^10.2f}Sachin".format(pi))             # center alignment

print("-" * 40)
print("{:*<15}Tendulkar".format("Sachin"))
print("{:*^15}Tendulkar".format("Sachin"))
print("{:*>15}Tendulkar".format("Sachin"))

print("Sachin Tendulkar".center(50, "-"))
print("{:-^50}".format("Sachin Tendulkar"))

print("Alignment fill characters".center(40, "-"))
print("{0:10.2f}\n{1:10.2f}".format(pi, -pi))

print("-" * 40)
print("{0:10.2f}\n{1:10.2f}".format(pi, -pi))
print("{0:10.2f}\n{1:=10.2f}".format(-pi, -pi))

print("-" * 40)
print("{0}\n{1}".format(pi, -pi))
print("-" * 40)
print("{0:.2}\n{1:.2}".format(pi, -pi))
print("-" * 40)
print("{0:-.2}\n{1:-.2}".format(pi, -pi))
print("{0:+.2}\n{1:+.2}".format(pi, -pi))
