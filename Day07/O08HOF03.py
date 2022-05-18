
def funlogger(fnc):

    def helperfun():
        print("Logged into the service......")
        fnc()
        print("logged out of the service.......")

    return helperfun

def normalfun():
    print("I should be called as normal......")

funlogger(normalfun)
print("-" * 40)

funlogger(normalfun)()
print("-" * 40)

res_fun = funlogger(normalfun)
res_fun()
print("-" * 40)

normalfun = funlogger(normalfun)
normalfun()
print("-" * 40)
print("-" * 40)

@funlogger              # decorator
def basicfun():
    print("I should be called as BASIC....")

# basicfun = funlogger(basicfun)
# basicfun()

basicfun()