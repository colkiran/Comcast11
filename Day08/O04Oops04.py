
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Initialized......")

    def get_details(self):
        print(f"Name = {self.name}\nAge = {self.age}")

    def get_info(self):
        print(self.__class__)

ply1 = Player("Sachin", 38)
ply1.get_details()

print("-" * 40)
ply2 = Player("Rahul", 34)
ply2.get_details()

print("-" * 40)
print(type(ply1))           # self will have the name of the of the object that called the method
ply1.get_info()

print("-" * 40)
print('ply1 :', ply1.__dict__)

print("-" * 40)
print('ply2 :', ply2.__dict__)
ply2.runs = 75

print("-" * 40)
print('ply2 :', ply2.__dict__)

print("-" * 40)
print('ply1 :', ply1.__dict__)

