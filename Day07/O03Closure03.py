
def OuterFun(greet):

    def InnerFun(gname):

        print(greet, gname)

    return InnerFun

OuterFun("Welcome")("Sachin")
print("-" * 40)

# Simple Curry
hindiGrt = OuterFun("Namaskar")
engGrt = OuterFun("Welcome")
spnGrt = OuterFun("Hola")

hindiGrt("Sachin")
engGrt("Ponting")
spnGrt("Messi")