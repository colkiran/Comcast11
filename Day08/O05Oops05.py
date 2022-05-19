
class Player:

    team = "India"          # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name = {self.name}\nAge = {self.age}")

ply1 = Player("Sachin", 36)
ply1.get_details()

print("-" * 40)
ply2 = Player("Rahul", 38)
ply2.get_details()

print("-" * 40)
print("Player :", Player.team)
print("ply1 :", ply1.team)
print("ply2 :", ply2.team)

print("-" * 40)
Player.team = "MI"
print("Player :", Player.team)
print("ply1 :", ply1.team)
print("ply2 :", ply2.team)

print("-" * 40)
ply2.team = "RR"
print("ply2 :", ply2.team)
print("Player :", Player.team)
print("ply1 :", ply1.team)

print(ply2.__dict__)
