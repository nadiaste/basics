# Chapter 9: Working with Classes and Instances
# OOPs - class, object, encapsulation
# encapsulation - hiding from the object, child classes
# polymorphism - ovveriding methods inherited in child class

class Car:
    # attribute - required, optional (default)
    # behaviour - CRUD operations -> set (create, update, delete), get (read), other functions (create, delete)
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = int(year)
        self.__mileage =0 # hiding from the object, child classes - encapsulation

    def get_description(self):
        """gets all details of the car."""
        print(f"Car details: \tManufacturer: {self.make.title()}\tModel: {self.model.title()}\tYear: {self.year}")
        print(f"Current mileage: {self.__mileage}")

    def set_mileage(self, new_mileage):
        """sets new mileage but not less than current mileage"""
        if new_mileage > self.__mileage:
            print("Setting the new value a mileage")
            self.__mileage = new_mileage
        else:
            print("Mileage entered is less than current. Please enter valid number")

    def add_to_mileage(self, miles):
        """increments the mileage with given miles. Adds to existing value"""
        if miles > 0:
            self.__mileage = self.__mileage + miles
            #self.__mileage += miles # same thing as the upper
            print(f"{miles} miles were added to the odometer.")
        else:
            print("Cannot accept negative numbers. It's called cheating. Try again" )

    def fill_tank(self):
        print('filling the tank with gas...')
        print("Done! It's ready to hit the road.")
class Bike:
    pass
# # Use input
# make = input('Enter the make of the car: ')
# model = input('Enter the model of the car: ')
# year = input('Enter the year of the car: ')
# car2 = Car(make, model, year)

#Commented lines below due to import in INHERITANCE CLASS FILE
# car1 = Car('bmw', 'x5', '2022')
# print(car1.make, car1.year+1)
# print("## Getter functions")
# car1.get_description()
# print("## Setters - updating the values of the attributes.")
# car1.model = 'X5 M'
# car1.set_mileage(50) # setting a value. Since mileage is hidden from the user, mileage can't be updated
# car1.get_description()
# car1.set_mileage(10)
# car1.get_description()
# car1.add_to_mileage(100)
# car1.get_description()
# # input: -15
# car1.add_to_mileage(-15)
# car1.get_description()
