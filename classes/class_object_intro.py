# Chapter 9: Classes and Objects
# All Class names - Capital letters. All variables, file names, function names - lower letters
# PEP8: guidelines
# use lowercase letters and underscores for:
# package, folder, file, variable(object class), function names
# use combination of title case for:
# classes - attributes (variables), behaviour (actions, functions)
# __init__ - is also called constructor.
#  self keyword  - shows that functions or variables belong in the current class
msg = 'wouf wouf'
breed = 'General'

def run():
    print('Nobody is running.')

class Dog():
    """
    Model of dogs, template for dogs.
    """
    # attribute (description) - variables, instance variables
    name = 'a'
    #breed = 'no breed'  # no use because of this def __init__(self, name, breed, color, size: 'medium')
    #size = 'medium'  #default values for these variables within the class
    #age = '2'   # no use because of this def __init__(self, name, breed, color, size: 'medium')
    color = ''

    # Constructor (of the class when you instantiate)
    # default functions to make required arguments
    # executed automatically every time ehn you create an object (instance)
    # def __init__(self, nm, brd, clr):
    #     self.name = nm
    #     self.breed = brd
    #     self.color = clr
    def __init__(self, name, breed, color, size= 'medium'):
         self.name = name
         self.breed = breed
         self.color = color
         self.size = size

    # behaviour (actions) - functions. All functions inside a class should have a self key

    def eat(self):
        print(f'{self.name} is eating: ')
        print(f'{self.name} wants more...: ')
        print(f'{self.name} is done eating.')

    def run(self):
        # miles = 5
        print("dog is running.")

    def get_description(self):
        # run() # outside the class
        # self.run() # within the class
        print(f'Name of the dog: {self.name}')
        print(f'Breed of the dog: {self.breed}')
        print(f'Color of the dog: {self.color}')
        print(f'Size of the dog: {self.size}')
        print(f'Age of the dog: {self.age}')

#  get_description()

# instantiation - creating instance of the class - creating object
# dog1, dog2 are the object

# dog1 = Dog() # copying everything from the module

print("--------------dog1--------------")
dog1 = Dog('chubby', 'chow chow', 'brown') # copying everything from the module
print("name of the dog before: ",dog1.name)
dog1.name = 'trex' # assigning the value to the attributes
print("name of the dog after assigning new name: ",dog1.name)
dog1.eat()
dog1.breed = 'chow chow'
print('dog1.breed', dog1.breed)
dog1.get_description()

print("--------------dog2--------------")

dog2 = Dog('max', 'german shephard', 'brown', 'large')
print(dog2.name)
print(dog2.breed)
dog2.get_description()

print('--------------- 9-1 -----------------')
# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints these two pieces of
#
# information, and a method called open_restaurant() that prints a message indi-
# cating that the restaurant is open.
#
# Make an instance called restaurant from your class. Print the two attri-
# butes individually, and then call both methods.



