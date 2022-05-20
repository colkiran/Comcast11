
class MyDecorator:

    def __init__(self, fnc):
        self.fnc = fnc

    def __call__(self):
        self.fnc()

@MyDecorator
def fun():
    print("Hello World...")

fun()

print("#" * 40)

class MyDecorator1:

    def __init__(self, fnc):
        self.fnc = fnc

    def __call__(self, *args):
        self.fnc(*args)


@MyDecorator1
def fun1(x, y, z):
    print(x, y, z)

fun1(10, 20, 30)