
import re
st = "LCNO-KAR-73-2011-9999"
res = re.search(r'LCNO-(KAR|KER|TND|APN|TEL|MAH|GOA)-([0-6][1-9]|[1-7][0-3])-([2-9][0-9]{3})'
                r'-((?!0000)[0-9]{4})$', st)
if res:
    print(res.group(0))
    print("Match found....")
else:
    print('Match not found......')