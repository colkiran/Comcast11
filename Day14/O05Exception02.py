
class TooOld(Exception):
    pass

class TooYoung(Exception):
    pass

class TooTiny(Exception):
    pass


age = 55

try:
    if age < 10:
        raise TooTiny("Too very young to decide the fate of the country......")
    if age < 18:
        raise TooYoung("Too young to select a leader.....")
    if age > 100:
        raise TooOld("Too Old to choose the rigth candidate......")


except TooYoung as y:
    print(y)

except TooTiny as t:
    print(t)

except TooOld as o:
    print(o)

except Exception as e:
    print(e)
else:
    print("Plaese cast your valuable vote to the right person.....")
finally:
    print("Completed the process of election.....")