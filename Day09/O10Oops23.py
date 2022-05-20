
# duck types => any bird which quaks is considered as a duck

class Manager:
    def doJob(self):
        print("Manager Job")

class Developer:
    def doJob(self):
        print("Developer Job")

class CarMechanic:
    def doJob(self):
        print("Repair cars....")

def BankFunJobs(emps):
    print("Bank Started".center(40, "-"))
    for emp in emps:
        emp.doJob()
    print("Bank Completed".center(40, "-"))
    print("-" * 40)

Melvin = Manager()
David = Developer()
Kevin = CarMechanic()

BankFunJobs([Melvin, David, Kevin])
