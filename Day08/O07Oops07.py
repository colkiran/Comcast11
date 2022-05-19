# Magic Method
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name = {self.name}\nAge = {self.age}"

ply1 = Player("Rahul", 32)
print(f"ply1 :{str(ply1)}")

print("-" * 40)
strname = ply1
print(strname)              # calls __str__ implicitly