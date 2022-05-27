class NotEqual(Exception):
    pass
class L1G(Exception):
    pass
class L1S(Exception):
    pass

l1 = [1, 6, 3]
l2 = [1, 4, 3]
try:
    if l1 > l2:
        raise L1G("L1 is greater than l2")
    elif l1 < l2:
        raise L1S("l1 is smaller than l2")
    elif l1 != l2:
        raise NotEqual("L1 is not equal")
    else:
        print("equal")
except NotEqual as n:
    print(n)
except L1G as g:
    print(g)
except L1S as s:
    print(s)
except Exception as e:
    print(e)
finally:
    print("Process executed....")