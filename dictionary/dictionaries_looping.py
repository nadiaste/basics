# CHAPTER 6l  Dictionary looping
# Dictionaries keys, only values, key and value

person1 = {'name': 'john doe', 'age': 25, 'location': 'ny'}

# default case, looping through keys only
for key in person1:
    print(key)
    print('value in this iteration is: ', person1[key])


# looping through keys only using .keys()
print("looping through keys only --------------------")
for key in person1.keys():
    print(key)
    print('value in this iteration is: ', person1[key])

# looping through values only. If in upper exercise, having the key,
# you can get the value. In this exercise you can't get the key for the value.
# Keys in Dictionaries are unique. Values are not unique. only one way: KEY TO VALUE (not value to key)

print("looping through values only ------------------")
for value in person1.values():
    print('value in this iteration is: ', person1)

#  looping through both: keys (first) and values (2nd) using items()

print("looping through both keys and values  ------------------")
for key, value in person1.items():
    print('key in this iteration is: ', key)
    print('value in this iteration is: ', value)
print('---------------------------------------------------------')

# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

rivers_countries = {'nile': 'egypt',
                    'mississippi': 'usa',
                    'amazon': 'brazil',
                    'thames': 'uk',
                    'nistru': 'md'}
print("##### Exercise 6-5 -------------------------------------")
print('#1 Use a loop to print a sentence about each river')
for river, country in rivers_countries.items():
    print(f'The {river.title()} runs through {country.title()}.')
print('---------------------------------------------------------')

print('#2 Use a loop to print the name of each river included in the dictionary.')
for river in rivers_countries.keys():
    print(f'river: {river.title()} ')
print('---------------------------------------------------------')

print('#3 Use a loop to print the name of each country included in the dictionary.')
for country in rivers_countries.values():
    print(f'Country: {country.title()}.')
print('---------------------------------------------------------')

# HW 6-4, 6-6