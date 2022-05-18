
"""
**************
==============

##############
______________

"""
def doubleMesh(fnc):
    def helper(*args):
        print("=" * 40)
        fnc(*args)
        print("#" * 40)
    return helper


def startSingle(fnc):
    def helper(*args):
        print("*" * 40)
        fnc(*args)
        print("-" * 40)
    return helper

@startSingle
@doubleMesh
def fun1():
    print("fun1  called....")

@startSingle
@doubleMesh
def fun2(x):
    print(f"fun2 called.... {x}")

@startSingle
@doubleMesh
def fun3(x, y):
    print(f"fun3 called....{x}, {y}")

@startSingle
@doubleMesh
def fun4(x, y, z):
    print(f"fun4 called....{x} {y} {z}")

fun1()
fun2(10)
fun3(3, 5)
fun4(6, 7, 8)
