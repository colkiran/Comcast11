
import re

st = "the quick brown fox jumps over the lazy dog"

print(f"st :{st}")

res = re.search(r'(\bj\w+)', st)

if res:
    print("Match found.....")
    print("String that was rejected by regex    :", st[:res.start()])
    print("String that matched the regex        :",res.group(0))
    print("String that is yet to be checked     :", st[res.end():])
else:
    print("Match not found.....")