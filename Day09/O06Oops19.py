
class Animal:

    def eat(self):
        print("Animals eat.....")

class Bird(Animal):

    def fly(self):
        print("Birds fly.....")

class Chicken(Bird):

    def disp(self):
        print("Chicken's are breeded for consumption.....")

chick  = Chicken()
chick.eat()
chick.fly()
chick.disp()
