
def OuterFun(greet):

    def InnerFun(sep):

        def InnerMost(name):
            import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + name)
            print(emojized)

        return InnerMost
    return InnerFun

sepFun = OuterFun("Welcome")
tigerDgn = sepFun("tiger")
lionDgn = sepFun("lion")
elphDgn = sepFun("elephant")

tigerDgn("Sheroff")
lionDgn("Sourav")
elphDgn("Dhoni")

"""
OuterFun("Welcome")("----->")("Sachin")

sepFun = OuterFun("Welcome")
design1 = sepFun("======>")
design2 = sepFun("*****>>")

design1("Sehwag")
design2("Sourav")
"""