
def funlogger(fnc):

    def helperfun(a, b):
        print("Logged into the service......")
        res = fnc(a, b)
        print("logged out of the service.......")
        return res
    return helperfun

@funlogger
def add(x, y):
    print(f"add called with {x} and {y}....")
    return x + y

@funlogger
def sub(x, y):
    print(f"sub called with {x} and {y}....")
    return x - y

@funlogger
def mul(x, y):
    print(f"mul called with {x} and {y}.....")
    return x * y

print(add(20, 45))
print("-" * 40)
print(sub(30, 14))
print("-" * 40)
print(mul(20, 20))
