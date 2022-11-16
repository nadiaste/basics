# Class inheritance
# from classes.working_with_classes import Car, Bike
from classes.working_with_classes import *

print("---------------------------------------")


# Class B inherits class A
# Class A is a parent for class B
# Class B (child class) has access to everything in class A
# If there are 2 classes, independent of each other and third one is created
# the third one can inherit both classes separately ex: class C(A,B)
# one can inherit as many classes as needed
class A:
    name = 'I come from class A'

    def greet(self):
        print("Hello!")


class B:
    age = 25

    def get_age(self):
        print(f'My age is: {self.age}')


class C(A, B):
    pass


# item1 = B() - when class B inherits class
item1 = C()  # when class C inherits both A and B
print(item1.name)
print(item1.age)
item1.greet()
item1.get_age()

# parent class A does not have access to child class B's attributes and methods
item2 = A()
print(item2.name)
item2.greet()

print("\n ******* Implementing the concepts with Car Class **********")


class ElectricCar(Car):

    def __init__(self, make, model, year): # this is passed to you
        super().__init__(make, model, year) # you pass it to the new class
        # super.__init__ executes the constructor of the parent class
        self.battery_size = 80


    def fill_tank(self):
        """
        we are overriding the fill_tank() function from the parent class
        """
        print("Sorry, this car does not have a tank, please go to charging station.")


    def get_description(self):
        super().get_description()
        print(f"Battery size: {self.battery_size}")



ecar1 = ElectricCar('tesla', 'model X', 2022)
ecar1.get_description()
ecar1.fill_tank() # calling the function overriding

print("\n---------------------------------------")
car1 = Car('bmw', 'x5', '2022')
car1.fill_tank()
car1.get_description()


# H/W 9-6 to 9-9