
import re

st = "the quick brown fox jumps over the lazy dog."

print(f"st :{st}")

res = re.sub("\s", "9", st, 3)

print(f"res :{res}")

res1 = re.sub('b\w+', 'BROWN', st)
print(f"res1 :{res1}")