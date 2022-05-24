
FL = open("data.txt", "r")

# st = FL.read(500)
# st = FL.readline(860)              # can read one line at a time
st = FL.readlines(857)                 # reads all the lines in a file and store it in a list

# for line in st:
#     print(line)

print(st)


FL.close()