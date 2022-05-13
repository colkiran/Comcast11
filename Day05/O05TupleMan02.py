
from collections import namedtuple

nmdTpl = namedtuple("Employee", "name des dep sal")
emp = nmdTpl(name="George", des="PM", dep="IT", sal=250000)
print(f"emp :{emp}")
print(f"Name        :{emp.name}")
print(f"Designation :{emp.des}")
print(f"Department  :{emp.dep}")
print(f"Salary      :{emp.sal}")

emp.name = "Micheal"
print(f"Name :{emp.name}")
