
import re

url = "www.google.com / search='%new hindi movies?' % / get_data2019 / " \
      "fetch_data frm_1 / imdb? %hindi%movies$& / result = page1.aspx"

while re.search(r'/', url):
    res =  re.search(r'/', url)
    print(url[:res.start()])
    url = url[res.end():]

print(url)