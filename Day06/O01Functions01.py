
def greet():
    print("Greetings Mr. Sachin, Welcome to the event....")

def greetGst(gname):
    print(f"Greetings Mr. {gname}, Welcome to the event.....")

# city is a default argument and gname is non default argument
def greetGstCty(gname, city="Mumbai"):
    print(f"Greetings Mr. {gname} from {city}, Welcome to the event......")


greet()
greetGst("Rahul")

print("-" * 40)
greetGstCty("Sachin")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

print("-" * 40)
def admission(fname, lname, age, conno, adr, edqlf, des):
    print(f"Name :{fname}{lname}")
    print(f"Age :{age}")
    print(f"Contact No :{conno}")
    print(f"Address :{adr}")
    print(f"Education Qulalification :{edqlf}")
    print(f"Designation :{des}")

# named arguments
admission(age=34, adr="indira nagar, bangalore", des="MGR", fname="Mike",
          lname="Tyson", conno=23492394, edqlf="Graduate")

print("-" * 40)

def muliply_me(x, y):
    return (x * y)
    print("Hello World")

print(f"The product of 5 and 8 is {muliply_me(5, 8)}")


print("-" * 40)
# recursive calls
def fun(n):
    if n == 0:
        return n
    # print("Hello World")
    print(n)
    fun(n-1)

fun(10)

def fact(n):
    if n==1:
        return n
    else:
        return n * fact(n-1)
n = int(input("Enter the nummber to find the factorial :"))
print(f"factorial of {n} is :{fact(n)}")

print("Fibanocci Series".center(40 ,"-"))

def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")
for i in range(n):
    print(fibonacci(i))



