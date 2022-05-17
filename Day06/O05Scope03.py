
"""
outerFun is the parent of innerFun

"""

def outerFun(gname):
    inv = f"Mr. {gname}"

    def innerFun():
        nonlocal gname
        gname += " Tendulkar"
        print(f"Hello {inv}")
        print(f"Hello {gname}")

    innerFun()


outerFun("Sachin")
