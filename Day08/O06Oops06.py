
class Player:

    def __init__(self, name, age):
        print("Init....")
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name = {self.name}\nAge = {self.age}")

    @classmethod
    def CreatePlayer(cls, fname, lname, age):
        print("factory...")
        return cls(f"Mr. {fname} {lname}", age)         # call the constructor


ply1 = Player("Sachin", "36")
ply1.get_details()

print("-" * 40)
ply2 = Player.CreatePlayer("Virat", "Kholi", 30)
ply2.get_details()
