
import sys
# print(sys.path)         # path is a list that has all library paths

sys.path.append("C:\Delhi")

for pth in sys.path:
    print(pth)

print("#" * 40)

import gurgaon.mymodule as m
from gurgaon.mymodule import Player

m.greet("Sourav Ganguly")
ply1 = Player("Sourav Ganguly", 34)
ply1.get_details()
