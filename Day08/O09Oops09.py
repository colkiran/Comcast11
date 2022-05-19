
class Emp:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return "{} : {}".format(self.name, self.salary)
    def __add__(self, x):
        return self.salary + x.salary
    def __sub__(self, x):
        return self.salary - x.salary
    def __mul__(self, x):
        return self.salary * x.salary
    def __truediv__(self, x):
        return self.salary / x.salary
    def __floordiv__(self, x):
        return  self.salary // x.salary

emp1 = Emp("MATHEW MURDOCK", 260000)
emp2 = Emp("FOGGY NELSON", 200000)
print(emp1)
print(emp2)
print("Add :", emp1 + emp2)
print("Subtract :", emp1 - emp2)
print("Multiply :", emp1 * emp2)
print("Divide :", emp1 / emp2)
print("Floor Division :", emp1 // emp2)
