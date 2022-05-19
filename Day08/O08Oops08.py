
class Employee():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name = {self.name}\nSalary = {self.salary}"

    def __eq__(self, other):            # works for not equal also
        return self.salary == other.salary

    def __gt__(self, other):
        return self.salary > other.salary

emp1 = Employee("Jack", 45000)
emp2 = Employee("Jill", 40000)

print(emp1)
print("-" * 40)
print(emp2)
print("-" * 40)

# print(emp1 == emp2)             # comparing the addresses by default
if (emp1 == emp2):
    print("Salary equal of {0} and {1}".format(emp1.salary, emp2.salary))
else:
    print("Salary NOT equal of {0} and {1}".format(emp1.salary, emp2.salary))

print("-" * 40)
if (emp1 != emp2):
    print("Salary NOT equal of {0} and {1}".format(emp1.salary, emp2.salary))
else:
    print("Salary equal of {0} and {1}".format(emp1.salary, emp2.salary))

print("-" * 40)
if emp1 > emp2:
    print("{2} {0} is greater than {3} {1}".format(emp1.salary, emp2.salary, emp1.name, emp2.name))
else:
    print("{2} {0} is less than {3} {1}".format(emp1.salary, emp2.salary, emp1.name, emp2.name))

print("-" * 40)
if emp1 < emp2:
    print("{2} {0} is less than {3} {1}".format(emp1.salary, emp2.salary, emp1.name, emp2.name))
else:
    print("{2} {0} is greter than {3} {1}".format(emp1.salary, emp2.salary, emp1.name, emp2.name))
