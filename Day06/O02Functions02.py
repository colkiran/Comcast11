
from collections import namedtuple

# function return values
def Arithmetic_Calc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    nmdTpl = namedtuple("ArithmeticCalc", "sum diff prod quot")
    calc = nmdTpl(sum = sum, diff = diff, prod = prod, quot = quot)
    return calc

res = Arithmetic_Calc(20, 8)
print(f"res :{res}")
print(f"sum :{res.sum}")
print(f"difference :{res.diff}")
print(f"product :{res.prod}")
print(f"Quotient :{res.quot}")


# variable length arguments
# *nums - can accept more than one n

def prodAll(*nums):
    res = 1
    print(nums)
    print(*nums)        # unpack
    for num in nums:
        res *= num
    print(f"res :{res}")
prodAll(1, 2, 3, 4, 5)

print("-" * 40)
def extract_details(**details):
    print(details)
    print(f"Name :{details['name']}")
    print(f"Runs :{details['runs']}")
    print(f"Opponent :{details['oppn']}")
    print(f"Venue :{details['venue']}")

extract_details(name="sachin", runs=125, oppn="Australia", venue="perth")

print("-" * 40)
# doc string

def fun():
    # this is a comment
    "This is a doc string"
    print("Hello World")

fun()
print(fun.__doc__)

print("-" * 40)

def fun1(x, y):
    """

    funtion fun1 takes two arguments
        res = fun1(x, y)
    if the arguments are integers then the function will return the sum of the numbers
    if the arguments are strings then the function will return the concatenation of the strings

    """
    return x + y

print(fun1(10, 20))
print(fun1('hello', 'world'))


print("-" * 40)
help(fun1)

"""
functions
---------
declare a function
call a function
pass arguments
recursive calls
default arguments
named arguments
variable length arguments
variable length named arguments
doc strings
help
"""