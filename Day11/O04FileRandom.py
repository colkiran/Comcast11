
FL = open("data.txt", "rb")

pos = FL.seek(50, 0)

print(f"position01 :{pos}")

pos = FL.seek(100, 1)

print(f"position02 :{pos}")

pos = FL.seek(-85, 1)

print(f"position03 :{pos}")

pos = FL.seek(50, 1)

print(f"position04 :{pos}")

pos = FL.seek(300, 2)

print(f"position05 :{pos}")

pos = FL.seek(-200, 2)

print(f"position06 :{pos}")

pos = FL.seek(0, 2)

print(f"position07 :{pos}")

pos = FL.seek(0, 0)

st = FL.read(30)

print(FL.tell())


# pos = FL.seek(-50, 0)
#
# print(f"position08 :{pos}")


FL.close()