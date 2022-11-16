cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw' and 2==2:
        print(f'car value was bmw and we use Upper(): {car.upper()}')
    else:
        print(f'expression returned false and we use Title(): {car.title()}')
#   and
#   true + true = true
#   true + false = false
#   false + true = false
#   false + false = false
#
#    or
#   true + true = true
#   true + false = true
#   false + true = true
#   false + false = false

car = 'tesla' # assigning the 'tesla' as a value of a car variable
car == 'bmw' # comparing the car value with 'bmw' string

for car in cars:
    if car == 'bmw' and (5==3+2):
        print(f'car value was bmw and we use Upper(): {car.upper()}')
    else:
        print(f'expression returned false and we use Title(): {car.title()}')

# Expressions: returns True/False
name = 'john'
num = 45.55
is_good = True
friends = []

# name == 'jane' # checkong if the value of the name variable is equal to 'jane'
# name > 'abc' # A-Z, True
# num == 45 # False
# num > 45 # True
# num < 45 # False
# num <= 45 # False
# num >= 45 # True
# is_good == True #True
# is_good == False # False
# name != 'jane' # True
# # name.lower() != 'jane' #True, Jane, jAne, JANE, jaNe, janE
# Multiple conditions with And/OR
#  name == 'john' or num > 45 # True or True >> True
#  name == 'john' or num < 45 # True or False >> True
#  name == 'jane' or num < 45 # False or False >> False

friends= []
if friends:
    print('friends is not empty list')
else:
    print('friends expression returned false, this means it is an empty list')

friends = ['jane']
if friends:
    print('friends is not an empty list')
else:
    print('friends expression returned false, this means it is an empty list')
# friends is not an emty list
#  cars = ['audi', 'bmw', 'subaru', 'toyota']
print('--------------------------------------------')
print(cars)
if 'tesla' in cars:
    print('cars list includes tesla')
else:
    print(f'tesla is not in the cars list.')


# H/W Ex 5-1. 5-2