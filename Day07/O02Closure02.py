
# closure
def OuterFun(gname):        # HOF -> Higher Order Function

    def InnerFun():
        print("Hello World")
        print(f"Hello {gname}")

    return InnerFun

OuterFun("Sachin")
print("-" * 40)

print(OuterFun.__name__)
print(OuterFun("Sachin").__name__)

print("-" * 40)
OuterFun('Sachin')()            # directly calls the innerfun

print("-" * 40)
infun = OuterFun("Rahul")

print("Before calling the Innerfun")
print("Hello World")
print("Hello World")
print("Hello World")
print("-" * 40)
infun()