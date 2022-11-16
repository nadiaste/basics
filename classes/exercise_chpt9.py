print('--------------- 9-1 -----------------')
# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that prints a message
# indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes
#  individually, and then call both methods.

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type =  cuisine_type

    def describe_restaurant(self):
        print(f"Name of the restaurant is: {self.restaurant_name}")
        print(f"This restaurant serves: {self.cuisine_type} food")

    def open_restaurant(self):
        print(f"{self.restaurant_name} restaurant is now open!\n")

restaurant1 = Restaurant("Brooklyn pizza", "Italian") # making an instance called restaurant from the class
print(restaurant1.restaurant_name) # printing the two attributes individually
print(restaurant1.cuisine_type)  # printing the two attributes individually
restaurant1.describe_restaurant()  # calling both methods
restaurant1.open_restaurant()  # calling both methods

#  H/W: 9-2, 9-3


print('--------------- 9-2 -----------------\n')
# 9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instance.

restaurant2 = Restaurant("Flora", "Modern American")
print(restaurant2.restaurant_name)
print(restaurant2.cuisine_type)
restaurant2.describe_restaurant()
restaurant2.open_restaurant()

restaurant3 = Restaurant("The Purple Pig", "Mediterranean")
print(restaurant3.restaurant_name)
print(restaurant3.cuisine_type)
restaurant3.describe_restaurant()
restaurant3.open_restaurant()

restaurant4 = Restaurant("Joe's crab'", "Seafood")
print(restaurant4.restaurant_name)
print(restaurant4.cuisine_type)
restaurant4.describe_restaurant()
restaurant4.open_restaurant()



# 9-3. Users: 1.Make a class called User. 2.Create two attributes called first_name
# and last_name, and then create several other attributes that are typically stored
# in a user profile. 3. Make a method called describe_user() that prints a summary
# of the user’s information. Make another method called greet_user() that prints
# a personalized greeting to the user.
# Create several instances representing different users, and call both methods
# for each user.

print('--------------- 9-3 -----------------\n')

class User:

    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def describe_user(self):
        print(f"Full name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age} y.o")
        print(f"Country: {self.country}")

    def greet_user(self):
        print(f"Welcome {self.first_name}, you are now logged in.\n")

user1 = User('Jessica', 'Lynn', 23, 'USA')
# print(user1.first_name)
# print(user1.last_name)
# print(user1.age)
# print(user1.country)
user1.describe_user()
user1.greet_user()

user2 = User('Annie', 'Mann', 42, 'Germany')
# print(user2.first_name)
# print(user2.last_name)
# print(user2.age)
# print(user2.country)
user2.describe_user()
user2.greet_user()

user3 = User('Don', 'Scott', 18, 'UK')
# print(user3.first_name)
# print(user3.last_name)
# print(user3.age)
# print(user3.country)
user3.describe_user()
user3.greet_user()