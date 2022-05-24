
"""
if we open a file in write mode
    a. if already exists
        1. it will delete the existing data and strart writing newly into the file

    b. if the file is not present
        1. it will create a new file and add the contents into the file
"""

FW = open("myfile.txt", "w")

# st = input("Enter the contents of the file :")
# FW.write(st)

line1 = "This is the first line. \n"
line2 = "This is the second line. \n"
line3 = "This is the third line. \n"

FW.writelines([line1, line2, line3])

FW.close()