
def greet(msg):
    print(msg)

greet("Welcome")
fun_name = greet

print(fun_name.__name__)
print(greet.__name__)

fun_name("Hello")

print("-" * 40)

def bank_flow(fnc):         #HOF
    print("-" * 40)
    print("Logging in....")
    fnc()               # callback
    print("Logging out....")
    print("-" * 40)

def withdraw():
    print("Debit.....")

def deposit():
    print("Credit.....")

def transfer():
    print("transfer......")

bank_flow(withdraw)
bank_flow(deposit)
bank_flow(transfer)
