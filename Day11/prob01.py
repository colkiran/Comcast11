
FL = open("EMP.csv", "r")

gen = {}
dept = []
desig = []
sal = 0
HrFSal = 0

for line in FL.readlines():

    g = line.split(",")[2]
    dp = line.split(",")[4]
    ds = line.split(",")[3]

    if g not in gen:
        gen[g] = 1
    else:
        gen[g] += 1

    if dp not in dept:
        dept.append(dp)

    if ds not in desig:
        desig.append(ds)

    sal += int(line.split(",")[5])

    if g == "f" and dp == "HR":
        HrFSal += int(line.split(",")[5])

FL.close()
print(f"Gender :{gen}")
print(f"Department :{dept}")
print(f"Designation :{desig}")
print(f"Total Salaries :{sal}")
print(f"HR Female Salary :{HrFSal}")