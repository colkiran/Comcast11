
def get_name(surname):
    print(f"Surname is {surname}")
    print("-" * 40)
    while True:
        name = yield
        print(f"received :{name}")
        if surname in name:
            print(f"Surname {surname} matched in {name}")
        else:
            print(f"Surname {surname} not found in {name}")
        print("-" * 40)

coObj = get_name("Pillai")
print(f"coObj :{coObj}")
coObj.__next__()
coObj.send("Virat Kholi")
coObj.send("Sachin Tendulkar")
coObj.send("Rahul Dravid")
coObj.send("Dhanraj Pillai")
