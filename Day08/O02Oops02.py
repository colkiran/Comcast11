
class Player:

    def __init__(self):             # constructor , double underscore init => dunder init
        print("Player Initialized......")

    def get_runs(self):
        print("Runs scored......")


sachin = Player()
sourav = Player()
rahul = Player()
print("-" * 40)
sachin.__init__()

print("-" * 40)
sachin.get_runs()
rahul.get_runs()
sourav.get_runs()