def fun(*args):
    if args:
        print(args)
    else:
        print("Hello")

fun()
fun(1, 2)
fun(1, 2, 3)

print("-" * 40)

def sum(x, y):
    return x + y

def diff(x, y):
    return x - y

def log_details(fnc):               # HOF
    loginfo = "Logging into the service...."

    def innerFun(*args):
        print(loginfo)
        print(fnc(*args))
        print("-" * 40)
    return innerFun

sum_logger = log_details(sum)
diff_logger = log_details(diff)

sum_logger(20, 30)
diff_logger(40, 18)
