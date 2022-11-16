# Chapter 6: Dictionary - data structure (key -value pair)
# CRUD (create, read, update, delete)
# Creating an empty dictionary
print("#### 1. accessing the values (R)")
person1 = {}
person2 = dict()
languages_list = ['eng', 'esp', 'germ', 'marsian']
person1 = {'name': 'john doe', 'age': 25, 'location': 'ny',
           'cars': ['audi', 'bmw', 'subaru', 'toyota'],
           'languages' : languages_list} # two-way reference to the list (connected)

# person1 = {'name': 'john doe', 'age': 25, 'location': 'ny'}
# # accessing the values (R)
# print(f"getting the name of person1 '{person1['name']}'")
# print(f"getting the age of person1 '{person1['age']}'")

# next exercise

# person1 = {'name': 'john doe', 'age': 25, 'location': 'ny'}
print("#### 2. accessing the values (R)")
# person1['name']
print(f"getting the name of person1 '{person1['name']}' ...")
print(f"getting the age of person1 '{person1['age']}' ...")

print("### 3. adding/updating key value pair to the dictionary (U)")
person1['phone'] = '(123) 456-7891'  # phone key did not exist in previous keys,
# so we add it as a new key-value pair (element)
print('Updated with new key dictionary: ', person1)
print("updating the value of 'age' in the person1 dictionary")
person1 ['age'] = 30 # if you mistakenly made a typo in the square brackets,
# the 'age' will not update, a new key with the typo name will be created
print('Updated age in person1 dictionary: ', person1)
#  cars[0] = 'merc'
person1['cars'][0]= 'merc'
print('Updated list (audi to merc) in person1 dictionary : ', person1)

# languages_list = ['eng', 'esp', 'germ', 'marsian']
# person1['languages'] = languages_list
# print(person1)
print("updating the list languages_list (marsian to ger)...")
languages_list[3]= 'ger'
print('updated list: ', languages_list)
print('dictionary: ', person1)
print('updating the value of the list in the dictionary')
person1['languages'][2] = 'french'
print('updated list: ', languages_list)
print('dictionary: ', person1)

#  copying the list to a value of the dictionary (independent values)
#  languages_list = ['eng' 'ru', 'esp', 'marsian']
# person1['languages'] = languages_list [:]
# print(person1)

print('##### 4. Delete key-value pair from the Dictionary (D)')
print("Deleting the location key-value pair from person1 ...")
del person1['location']
print("updated person1 dictionary: ", person1)
person1['age'] = None # no value, like Null in sql
print("updated age in person1 dictionary: ", person1)


#  Exercise: 6-2 Favorite Numbers
fav_nums = {'nicole': 7, 'alex': 10, 'yulia': 5}
#  Print each person's name and their favorite number.
print(f"Nicole's favorite number is: {fav_nums['nicole']} ")
print(f"Alex's favorite number is: {fav_nums['alex']} ")
print(f"Yulia's favorite number is: {fav_nums['yulia']} ")

# HW: 6-1, 6-3
