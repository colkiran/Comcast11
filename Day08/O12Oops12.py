
class Employee:

    def __init__(self, name):
        self.__name = name              # private variable
        self.tech = ['C', 'C++', 'JAVA', 'JSP', 'J2EE', 'Spring', 'Hibernate', 'Angular']

    def __str__(self):
        return self.__name + " \nTechnologies :" + ", ".join([v for v in self.tech])

emp1 = Employee("Louis")
print(emp1)
# print(emp1.__name)
print(emp1.__dict__)
print("Name :", emp1._Employee__name)
emp1._Employee__name = "Charles"
print("Name :", emp1._Employee__name)
