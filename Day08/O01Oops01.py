"""
python, perl, ruby and lua =>  scripting tools
language features => compares it with C
OOPS => compares with C++, JAVA and DOTNET
"""

class Player:               # pascal casing

    def get_runs(self):        # self is like a this pointer
        print(self.__class__)
        print("Runs scored......")

sachin = Player()              # calls the constructor, calls the default constructor
sachin.get_runs()

print("-" * 40)
print(type(sachin))
print("Module Name :",__name__)

print("-" * 40)
print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance(sachin, str))

