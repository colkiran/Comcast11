

class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['C', 'C++', 'JAVA', 'JSP', 'J2EE', 'Spring', 'Hibernate', 'Angular']

    def __str__(self):
        return "Name :{}\nSalary :{}".format(self.name, self.salary)

    def __iter__(self):
        return iter(self.tech)

    def __len__(self):
        return len(self.tech)

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, index):
        return self.tech[index]

    def __setitem__(self, index, value):
        self.tech[index] = value

emp1 = Employee("Kevin", 45000)
print(emp1)

print("-" * 40)
print([t for t in emp1])

print("-" * 40)
print(len(emp1))

print("-" * 40)
emp1.append("Python")
print([t for t in emp1])

print("-" * 40)
tech = emp1[5]
print(tech)

print("-" * 40)
emp1[3] = "EJB"
print([t for t in emp1])
