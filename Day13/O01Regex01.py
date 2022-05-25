
import re

# st = "This is a sample string"
# print(f"st :{st}")
# res = re.match(r'^This', st)
# res = re.search(r'String$', st, re.I)
# res = re.search(r'b.t', st)
# res = re.search(r'ba*t', st)            # zero or more occurances of a
# res = re.search(r'ba?t', st)            # zero or one occurance of a
# res = re.search(r'ba+t', st)            # one or more occurances of a
# res = re.search(r'ba{3}t', st)
# res = re.search(r'ba{3,}t', st)         # atleast 3 times or 3 or more times
# res = re.search(r'ba{3,8}t', st)
# res = re.search(r'b[a-zA-Z0-9]t', st)
# res = re.search(r'b[aeiou]t', st)
# res = re.search(r'b[^aeiou]t', st)
# res = re.search(r'b(ai|es)t', st)

st = "sample.py"

res = re.search(r'\.py$', st)

print("-" * 40)
print(res)
print("-" * 40)

if res:
    print("Match found.....")
    print(res.group(0))             # string that matched our regex
else:
    print("Match not found.....")