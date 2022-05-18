
def callMe():
    print("Apples from Ooty....")

def fun(fnc):
    print('Hello....')
    fnc()
    print("Hi.....")
    print("-" * 40)

    def defineMe():
        print("Oranges from Kanpur.....")
    return defineMe

def funCallback(fnc):
    print("Mera Bharath mahan..........")
    fnc()
    print("India is great.......")

funCallback(fun(callMe))
