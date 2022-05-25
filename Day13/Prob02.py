
import re

date = "10-12-2022"

res = re.search(r'([0-2][1-9]|[1-3][0-1])(/|-)(0[1-9]|1[0-2])(\2)(19[0-9]{2}|[2-9][0-9]{3})', date)

if res :
    print("Match found.....")
    print(res.group(0))
else:
    print("Match not found.....")