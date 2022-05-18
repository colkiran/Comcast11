
# closure
def OuterFun(gname):

    def InnerFun():
        print("Hello World")
        print(f"Hello {gname}")

    InnerFun()

OuterFun("Rahul")
