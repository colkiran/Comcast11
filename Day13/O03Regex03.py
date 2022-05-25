"""
recall a regular expression -> by its grouping
your not only recalling the regex but also the data should be the same
"""
import re

st = "good blood bad blood"

res = re.search(r'(\w+)\s(\w+)\s(\w+)\s(\2)', st)

if res:
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found.....")