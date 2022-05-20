
"""
1. class
2. object
3. isinstance
4. __init__
5. self
6. class attribute
7. @classmethod
8. cls
9. __str__
10. __eq__, __gt__.....__add__, __truediv__.....
11. private variables with __
12. __dict__
13. setter getter and deleter
14. property, @poperty, setter, deleter...

"""

class Animal:
    def __init__(self):
        print("Animal Ctor....")
        self.age = 1

    def eat(self):
        print("Animal's eat......")

class Bird(Animal):             # inheritance
    def fly(self):
        print("Birds fly.....")

class Fish(Animal):             # inheritance
    def swim(self):
        print("Fishes Swim......")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

print("-" * 40)
dolphin = Fish()
dolphin.eat()
dolphin.swim()

print("-" * 40)
print(cuckoo.__dict__)
print(dolphin.__dict__)

print("-" * 40)
print(f"isinstance(cuckoo, Animal) :{isinstance(cuckoo, Animal)}")
print(f"isinstance(cuckoo, Bird) :{isinstance(cuckoo, Bird)}")
print(f"isinstance(cuckoo, Fish) :{isinstance(cuckoo, Fish)}")
