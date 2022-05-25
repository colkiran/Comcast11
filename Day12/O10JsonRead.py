
import json

JFR = open("books.json", "r")
jsonfile = json.load(JFR)

for book in jsonfile['books']:
    for k, v in book.items():
        print(k, "=>", v)
    print("-" * 40)
