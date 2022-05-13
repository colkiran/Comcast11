
emp = {
    'emp1':{'empid': 1098, 'empname': 'Jack', 'age': 29, 'dept': 'Finance', 'desig': 'FE', 'sal': 65000},
    'emp2':{'empid': 2820, 'empname': 'Jill', 'age': 35, 'dept': 'HR', 'desig': 'MGR', 'sal': 95000},
    'emp3':{'empid': 3751, 'empname': 'Kevin', 'age': 24, 'dept': 'IT', 'desig': 'Dev', 'sal': 75000}
}

print(f"emp :{emp}")
print("-" * 40)
print(f"emp1 :{emp['emp1']}")
print(f"emp2 :{emp['emp2']}")
print(f"emp3 :{emp['emp3']}")

print("-" * 40)
for ky, info in emp.items():
    print(ky)
    print("------")
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

print("update".center(40, "-"))
emp1 = {'empid': 1098, 'empname': 'Jack', 'age': 29, 'dept': 'Finance', 'desig': 'FE', 'loc': 'Hyd'}
emp2 = {'empid': 2820, 'empname': 'Jill', 'age': 35, 'dept': 'HR', 'desig': 'MGR', 'sal': 95000}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

emp1.update(emp2)
print(f"emp1 :{emp1}")

print("clear".center(40, "-"))
emp1 = {'empid': 1098, 'empname': 'Jack', 'age': 29, 'dept': 'Finance', 'desig': 'FE', 'sal': 65000}

print(f"emp1 Before :{emp1}")
emp1.clear()
print(f"emp1 After :{emp1}")

