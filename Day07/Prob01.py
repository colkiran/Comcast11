
import time

def timelogger(fnc):
    def helperfun(a, b):
        t1 = time.time()
        res = fnc(a, b)
        t2 = time.time()
        print(f"Time for execution {t2 - t1}")
        return res
    return helperfun

@timelogger
def add(x, y):
    l = []
    for i in range(1, 5000):
        for j in range(1, i+1):
            l.append(j ** 2)
    print(f"add called with {x} and {y}...")
    print(x + y)


add(100, 300)