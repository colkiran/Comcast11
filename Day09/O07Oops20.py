
class Animal:
    def __init__(self):
        self.a = 10
        print("Animal Ctor......")

    def eat(self):
        print("Animals eat......")

    def fun(self):
        print("fun method of Animal class........")

class Person:
    def __init__(self):
        self.b = 20
        print("Person Ctor.......")

    def talk(self):
        print("Person talks.....")

    def fun(self):
        print("fun method of Person class........")

class Girl(Animal, Person):
    def __init__(self):
        super().__init__()                # parent class Ctor
        Person.__init__(self)
        self.g = 30
        print("Girl Ctor.......")

tina = Girl()
tina.eat()
tina.talk()
tina.fun()

print("-" * 40)
print(tina.__dict__)
