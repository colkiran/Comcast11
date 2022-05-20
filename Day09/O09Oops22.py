
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass

class Manager(Employee):
    def doJob(self):
        print("Manager Job")

class Developer(Employee):
    def doJob(self):
        print("Developer Job")

def BankFun(emp):           # polymorphism
    print("Bank Job Started".center(40, "-"))
    emp.doJob()
    print("Bank Job Completed".center(40, "-"))
    print("-" * 40)

Melvin = Manager()
David = Developer()

BankFun(Melvin)
BankFun(David)

def BankFunJobs(emps):           # polymorphism
    print("Bank Job Started".center(40, "-"))
    for emp in emps:
        emp.doJob()
    print("Bank Job Completed".center(40, "-"))
    print("-" * 40)


BankFunJobs([Melvin, David])
