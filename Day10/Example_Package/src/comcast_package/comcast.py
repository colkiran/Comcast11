
guestName = "Sachin Tendulkar"

sports = ['cricket', 'soccer', 'tennis', 'hockey', 'swimming', 'basketball']

runs = {'odi': 25400, 'test': 26750, 't20': 2800}

def greet(gst):
    print(f"Greetings Mr. {gst}, Welcome to the event.....")


class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is :{self.name}\nAge is :{self.age}")

