
# C language syntax
format = "Welcome %s, What a %s player...."
print(format)
values = ("Sachin", "Class")                # tuple
print(values)
print(format % values)
print("-" * 40)

format = "Welcome %s, Your rating of %.3f, what a  %s player"
print(format)
print(format % ("Sachin", 9, "class"))
print(format % ("Sachin", 9.6, "class"))
print(format % ("Sachin", 9.568, "class"))
print(format % ("Sachin", 9.523642, "class"))
print("-" * 40)
print("Welcome %s, Your rating of %.3f, what a  %s player" % ("Sachin", 9, "class"))

print("-" * 40)


# unix style
from string import Template
# from string module import Template class
tmp = Template("Welcome $name, What a $adjective player")
print(tmp)

res = tmp.substitute(name= "Sachin", adjective = "Superb")
print(res)

print("-" * 40)


# format method of strings class in python
print("Welcome {}, what a {} player for {}".format("Sachin", "class", 'India'))

print("Welcome {0}, what a {1} player for {2}".format("Sachin", "class", 'India'))

print("Welcome {1}, what a {2} player for {0}".format('India', "Sachin", "class"))

print("Welcome {pname}, what a {adj} player for {cntry}".format(pname = "Sachin", adj="super", cntry="India"))

print("Welcome {pname}, what a {adj} player for {cntry} with a rating of {rat:.3f}".format(pname = "Sachin",
                                                        adj="super", cntry="India", rat = 4.8))

print("-" * 40)
# Interpolation
from math import pi, e
print(f"PI = {pi} and Eulers constant = {e}")

print("PI = {} and Euler's constant = {}".format(pi, e))
print("PI = {pi:.3f} and Euler's constant = {e:.3f}".format(pi = pi, e = e))
