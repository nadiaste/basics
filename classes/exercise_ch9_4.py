
# 9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
# Add an attribute called number_served with a default value of 0. Create an
# instance called restaurant from this class. Print the number of customers the
# restaurant has served, and then change this value and print it again.
from classes.working_with_classes import Car


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Name of the restaurant is: {self.restaurant_name}")
        print(f"This restaurant serves: {self.cuisine_type} food")

    def open_restaurant(self):
        print(f"{self.restaurant_name} restaurant is now open!\n")

    def set_number_served(self, new_number_served):
        """method lets set a number of customers served"""
        self.number_served = new_number_served

    def increment_number_served(self, num_served):
        """method lets increment the number of customers served"""
        self.number_served += num_served


# making an instance called restaurant from the class
restaurant1 = Restaurant("Brooklyn pizza", "Italian")

# printing the number of customers served
print(f"Number of customers the restaurant has served: {restaurant1.number_served}.")

# changed value of customers served
restaurant1.number_served = 15
print(f"Number of customers the restaurant has served: {restaurant1.number_served}.")

# Add a method called set_number_served() that lets you set the number
# of customers that have been served. Call this method with a new number and
# print the value again.

restaurant1.set_number_served(20)
print(f"Number of customers the restaurant has served: {restaurant1.number_served}.")

# Add a method called increment_number_served() that lets you increment
# the number of customers who’ve been served. Call this method with any number
# you like that could represent how many customers were served in, say, a
# day of business."""

restaurant1.increment_number_served(7)
print(f"Number of customers the restaurant has served: {restaurant1.number_served}.")

# H/W : 9-5, 9-6, 9-7, 9-8, 9-9

# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166).
print('--------------- 9-5 -----------------\n')


class User:
    username = 'john'
    password = '$Today2023'

    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0

    def describe_user(self):
        print(f"Full name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age} y.o")
        print(f"Country: {self.country}")

    def greet_user(self):
        print(f"Welcome {self.first_name}, you are now logged in.\n")

    # Write a method called increment_
    # # login_attempts() that increments the value of login_attempts by 1.
    def increment_login_attempts(self):
        """number of login attempts will be incremented by 1"""
        self.login_attempts += 1
    def login_to_website(self, username:str, password:str):
        if username.lower() == self.username and password == self.password:
            self.reset_login_attempts()
            print("You have logged in successfully. Welcome to your homepage!")
        else:
            if self.login_attempts > 3:
                print("your account is blocked. Please try again later.")
            else:
                self.increment_login_attempts()
                print("Your username or password was incorrect. Try again.")

    # Write another method called reset_login_attempts() that resets the value of login_
    # # attempts to 0.
    def reset_login_attempts(self):
        """number of login attempts will be set to 0"""
        self.login_attempts = 0


# # Make an instance of the User class and call increment_login_attempts() several times.

user1 = User('Jessica', 'Lynn', 23, 'USA')
print(f"Welcome {user1.first_name} {user1.last_name} from {user1.country}.")
user1.increment_login_attempts()
print(f"Your login attempts = {user1.login_attempts}")
user1.increment_login_attempts()
print(f"Your login attempts = {user1.login_attempts}")
user1.increment_login_attempts()
print(f"Your login attempts = {user1.login_attempts}")

#  Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.

# user1.reset_login_attempts()
# print(f"Your total login attempts set to: {user1.login_attempts}")

user1.reset_login_attempts()
print(f"Your total login attempts set to: {user1.login_attempts}")
user1.login_to_website('john', 'as;sdf')
print(f"Your total login attempts set to: {user1.login_attempts}")
user1.login_to_website('john', '$today2023')
print(f"Your total login attempts set to: {user1.login_attempts}")
user1.login_to_website('john', '$Today2023')

# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote
# in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
# the class will work; just pick the one you like better. Add an attribute called
# flavors that stores a list of ice cream flavors. Write a method that displays
# these flavors. Create an instance of IceCreamStand, and call this method.

print('\n--------------- 9-6 -----------------\n')


# class IceCreamStand(Restaurant):
#
#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#
#
#     def display_flavors(self, flavors):
#         self.display_flavors = flavors
#         print(f"These are the flavors available today:"
#               f"\n {self.display_flavors}")
#
#
# restaurant2 = IceCreamStand("Gelato", "italian ice cream")
# print(f'In our restaurant called {restaurant2.restaurant_name}, \nwe serve '
#       f'delicious {restaurant2.cuisine_type}')
# restaurant2.display_flavors (["strawberry", "vanilla", "coconut", "chocolate"])


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavors(self):
        print(f"These are the flavors available today:")
        for flavor in self.flavors:
            print(f"\t{flavor}")


restaurant2 = IceCreamStand("Gelato", "italian ice cream")
restaurant2.flavors = ['strawberry', 'vanilla', 'chocolate', 'coconut']
print(f'In our restaurant called {restaurant2.restaurant_name}, \nwe serve '
      f'delicious {restaurant2.cuisine_type}')
restaurant2.display_flavors()


# 9-7. Admin: An administrator is a special kind of user. Write a class called
# Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
# or Exercise 9-5 (page 171).

# print('\n--------------- 9-7 -----------------\n')
#
#
# class Admin(User):
#
#     # Add an attribute, privileges, that stores a list
#     # # of strings like "can add post", "can delete post", "can ban user", and so on.
#     def __init__(self, first_name, last_name, age, country):
#         """add attribute privileges that stores a list"""
#         super().__init__(first_name, last_name, age, country)
#         self.privileges = []
#
#     # Write a method called show_privileges() that lists the administrator’s set of
#     # privileges.
#     def show_privileges(self):
#         """function show_privileges displays admin's set of privileges"""
#         print(f"{admin1.first_name.title()} has the following privileges:")
#         for privilege in self.privileges:
#             print(f"\t{privilege}")
#
#
# # Create an instance of Admin, and call your method.
# admin1 = Admin('jackie', 'jones', 34, 'japan')
# admin1.privileges = ['can add post', 'can delete post', 'can ban user']
# print(f"Admin information: {admin1.first_name.title()} {admin1.last_name.title()}, "
#       f"{admin1.age}, {admin1.country.title()}")
# admin1.show_privileges()


# 9-8. Privileges: Write a separate Privileges class. The class should have one
# attribute, privileges, that stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class.

class Admin(User):

    def __init__(self, first_name, last_name, age, country):
        """add attribute privileges that stores a list"""
        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges()


print('\n--------------- 9-8 -----------------\n')


class Privileges:

    def __init__(self):
        self.privileges = []

    def show_privileges(self):
        """function show_privileges displays admin's set of privileges"""
        print(f"Privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"\t{privilege}")
        else:
            print(f"\nNo privileges.")


# # Make a Privileges instance as an attribute in the Admin class.
# Create a new instance of Admin and use your method to show its privileges.

admin1 = Admin('jackie', 'jones', 34, 'japan')
admin1.describe_user()
admin1.privileges.show_privileges()


print('\nNew addition ->')
admin1_privileges = [
    'can override error',
    'can reset account',
    'can moderate comments',
]
admin1.privileges.privileges = admin1_privileges
admin1.privileges.show_privileges()


# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 85 if it isn’t already.
# Make an electric car with a default battery size, call get_range() once, and
# then call get_range() a second time after upgrading the battery. You should
# see an increase in the car’s range.

class Battery():

    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def get_range(self):
        """Print a statement about the range this battery provides."""
        range = 0
        if self.battery_size == 70:
            range = 260
        elif self.battery_size == 85:
            range = 310

        # message = f"This car can go approximately {range}"
        # message += " miles on a full charge."
        # print(message)
        print(f'This car can go approximately {range} miles on a full charge. ')

    def upgrade_battery(self):
        if self.battery_size < 85:
            self.battery_size = 85
            print(f'Battery size upgraded to 85.')
        else:
            print('Battery size is at the upgraded level.')


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()


print('Check the battery of this electric car:')
electric_car1 = ElectricCar('Rivian', 'R1T', 2022)
electric_car1.battery.get_range()

print('\nCheck the upgraded battery of this electric car:')
electric_car1.battery.upgrade_battery()
electric_car1.battery.get_range()
