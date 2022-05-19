
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

emp1 = Employee("Mike Tyson", 30000)
print(emp1)

print("-" * 40)
print([c for c in emp1])

print("-" * 40)
print(len(emp1))