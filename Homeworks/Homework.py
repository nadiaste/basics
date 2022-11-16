# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.


# Ex 3-4
guests = ['akmal', 'said', 'lenur']
print('Hello ' + guests[0].title() + ', I am inviting you to the party')
print(f'Hello {guests[0].title()}, I am inviting you to the party')
print(f'Hello {guests[1].title()}, I am inviting you to the party')
print(f'Hello {guests[2].title()}, I am inviting you to the party')
# Hello Akmal, I am inviting you to the party
#Ex 3-5 change the list
removed_guest = guests.pop(1)
# a = 'said' this is the same thing as line 60
# Said cannot make it to the party
print(guests)
print(f'{removed_guest} cannot make it to the party')
guests.append('dima')
print(guests)
guests.insert(0, 'andy')
print(guests)
print(f'Hello {guests[0].title()}, Welcome to the party')
print(f'Hello {guests[1].title()}, Welcome to the party')
print(f'Hello {guests[2].title()}, Welcome to the party')
print(f'Hello {guests[3].title()}, Welcome to the party')


# Ex 3.6
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
print('----------------------------------------------')
print('Hi everyone, we you found a bigger dinner table and now we have more space!')
print('----------------------------------------------')

# • Use insert() to add one new guest to the beginning of your list.
guests.insert(0, 'alex')
print(guests)
print('----------------------------------------------')
# • Use insert() to add one new guest to the middle of your list.
guests.insert(2, 'vika')
print(guests)
print('----------------------------------------------')

# • Use append() to add one new guest to the end of your list.
guests.append('benny')
print(guests)
guests.append('eldar')
print(guests)

# • Print a new set of invitation messages, one for each person in your list.
for guest in guests:
    print(f'Hi {guest.title()}, please join me for an amazing dinner party!')
print('----------------------------------------------')

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.

# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.

print('Hi everyone, unfortunately circumstances have changed and we can invite only 2 people... ')
print('----------------------------------------------')

# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.

# guests.pop()
# print('Sorry eldar, I cant invite you anymore')
# print(guests)
# guests.pop()
# print('Sorry benny, I cant invite you anymore')
# print(guests)
# guests.pop()
# print('Sorry dima, I cant invite you anymore')
# print(guests)
# guests.pop()
# print('Sorry lenur, I cant invite you anymore')
# print(guests)
# guests.pop()
# print('Sorry akmal, I cant invite you anymore')
# print(guests)
# guests.pop()
# print('Sorry vika, I cant invite you anymore')
# print(guests)

removed_guest = guests.pop(7)
print(guests)
print(f'{removed_guest} I cant invite you anymore...')
print('----------------------------------------------')
removed_guest = guests.pop(6)
print(guests)
print(f'{removed_guest} I cant invite you anymore...')
print('----------------------------------------------')
removed_guest = guests.pop(5)
print(guests)
print(f'{removed_guest} I cant invite you anymore...')
print('----------------------------------------------')
removed_guest = guests.pop(4)
print(guests)
print(f'{removed_guest} I cant invite you anymore...')
print('----------------------------------------------')
removed_guest = guests.pop(3)
print(guests)
print(f'{removed_guest} I cant invite you anymore...')
print('----------------------------------------------')
removed_guest = guests.pop(2)
print(guests)
print(f'{removed_guest} I cant invite you anymore...')
print('----------------------------------------------')

# Print a message to each of the two people still on your list, letting them
# know they’re still invited.

for guest in guests:
    print(f'Hi {guest.title()} you are still invited to the party!')
print('----------------------------------------------')

# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

del guests
print('----------------------------------------------')

# 3-8. Seeing the World: Think of at least five places in the world you’d like to
# visit.
# • Store the locations in a list. Make sure the list is not in alphabetical order.
# • Print your list in its original order. Don’t worry about printing the list neatly,
# just print it as a raw Python list.

cities = ['capri', 'rome', 'milan', 'sicily', 'napoli']
print(cities)
print('----------------------------------------------')

# Use sorted() to print your list in alphabetical order without modifying the
# actual list.
# • Show that your list is still in its original order by printing it.

print(sorted(cities))
print(cities)
print('----------------------------------------------')

# Use sorted() to print your list in reverse alphabetical order without chang-
# ing the order of the original list.
# • Show that your list is still in its original order by printing it again.

print(sorted(cities, reverse=True))
print(cities)
print('----------------------------------------------')

# • Use reverse() to change the order of your list. Print the list to show that its
# order has changed.
cities.reverse()
print(cities)
print('----------------------------------------------')

# • Use reverse() to change the order of your list again. Print the list to show
# it’s back to its original order.

cities.reverse()
print(cities)
print('----------------------------------------------')

# • Use sort() to change your list so it’s stored in alphabetical order. Print the
# list to show that its order has been changed.
cities.sort()
print(cities)
print('----------------------------------------------')

# • Use sort() to change your list so it’s stored in reverse alphabetical order.
# Print the list to show that its order has changed.
cities.sort(reverse=True)
print(cities)
print('----------------------------------------------')

# 3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
# through 3-7 (page 46), use len() to print a message indicating the number
# of people you are inviting to dinner.

guests = ['akmal', 'said', 'lenur']
print(f'Hello {guests[0].title()}, I am inviting you to the party')
print(f'Hello {guests[1].title()}, I am inviting you to the party')
print(f'Hello {guests[2].title()}, I am inviting you to the party')
print('I am inviting',  len(guests),  'people to the dinner!')
print('----------------------------------------------')

# 3-10. Every Function: Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or any-
# thing else you’d like. Write a program that creates a list containing these items

fruits = ['strawberries', 'oranges', 'blueberries', 'mango', 'bananas']
print(fruits)
print('----------------------------------------------')

# and then uses each function introduced in this chapter at least once.
# Accessing Elements in a List - using index

print(fruits[0])
print('----------------------------------------------')

# Using Individual Values from a List - concatenation

message ='my favorite fruit is ' + (fruits[3]) + '.'
print(message)
print('----------------------------------------------')


# 3.9 Modifying Elements in a List

print(fruits)
fruits[0] = 'grapes'
print(fruits)
print('----------------------------------------------')

# 3.9 Adding Elements to a List - append

fruits.append('strawberries')
print(fruits)
print('----------------------------------------------')

# 3.9 Adding Elements to a List - insert

fruits.insert(1, 'raspberries')
print(fruits)
print('----------------------------------------------')

# 3.9 Removing Elements from a List - del
del fruits[0]
print(fruits)
print('----------------------------------------------')

# 3.9 Removing Elements from a List - pop() last in the list

popped_fruits = fruits.pop()
print(fruits)
print(popped_fruits)
print('----------------------------------------------')

# 3.9 Removing Elements from a List - pop() anywhere in the list using index
print(fruits)
removed_fruits = fruits.pop(0)
print('I make fresh squeezed juice from ' + fruits.pop(0) + '.')
print('----------------------------------------------')

# 3.9 Removing an Item by Value - remove()

print(fruits)
fruits.remove('blueberries')
print(fruits)
print('----------------------------------------------')

# 3.9 Organizing a List - Sorting a List Permanently with the sort() Method

fruits = ['strawberries', 'oranges', 'blueberries', 'mango', 'bananas']
fruits.sort()
print(fruits)
print('----------------------------------------------')

# 3.9 Organizing a List - Sorting a List Permanently with the reverse sort() Method
fruits.sort(reverse=True)
print(fruits)
print('----------------------------------------------')

# Sorting a List Temporarily with the sorted() Function
print('this is the list before sorting')
print(fruits)

print('this is the sorted list')
print(sorted(fruits))

print('this is the list before sorting again')
print(fruits)
print('----------------------------------------------')

# 3.9 Printing a List in Reverse Order - reverse

print(fruits)
fruits.reverse()
print(fruits)
print('----------------------------------------------')

# 3.9 Finding the Length of a List  - len()

fruits = ['strawberries', 'oranges', 'blueberries', 'mango', 'bananas']
len(fruits)
print('----------------------------------------------')

# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.

pizzas = ['margherita', 'capriciosa', 'funghi']
for pizza in pizzas:
    print(pizza.title())
print('----------------------------------------------')

# • Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni pizza.

for pizza in pizzas:
    print(f'My favorite pizza is {pizza.title()}')
print('----------------------------------------------')


# • Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!

for pizza in pizzas:
    print(f'My favorite pizza is {pizza.title()}')
print('I absolutely adore pizza!!' + '.\n')
print('----------------------------------------------')


# 4-2. Animals: Think of at least three different animals that have a common characteristic.
# Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal.

animals = ['lion', 'tiger', 'bobcat']
for wild_cats in animals:
    print(wild_cats.title())
print('----------------------------------------------')

# • Modify your program to print a statement about each animal, such as
# A dog would make a great pet.

for wild_cats in animals:
    print(f'{wild_cats.title()} is one of the fastest and fiercest animals in the world!')
print('----------------------------------------------')

# • Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would
# make a great pet!
for wild_cats in animals:
    print(f'{wild_cats.title()} is one of the fastest and fiercest animals in the world!')
print('Their habitats are endangered.')
print('----------------------------------------------')

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

for numbers in range(1,21):
    print(numbers)
print('----------------------------------------------')

# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)

#numbers= list(range(1,1000001))
#for a in numbers:
#    print(numbers)
#print('----------------------------------------------')

# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.

numbers= list(range(1,1000001))
min(numbers)
max(numbers)
sum(numbers)
print('----------------------------------------------')

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.

odd_numbers= range(1,21)
for odds in odd_numbers:
# for nums in range(1,21):
   print(odds)
print('----------------------------------------------')

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.

for nums in range(3, 30, 3):
    print(nums)
print('----------------------------------------------')


# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.
cubes = []
for nums in range(1,11):
    print(nums**3)
    cubes.append(nums**3)
print(f'Cubes list: {cubes}')
print('----------------------------------------------')

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.
# list comprehension- short syntax code to go through the list and then create a new list

cubes = [value**3 for value in range(1,11)]
print(cubes)
print('----------------------------------------------')

# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')

sneakers = 'nike', 'adidas', 'asics', 'new balance'
print('example 1')
print("is number two in the list =='adidas'? I predict True")
print(sneakers[1] == 'adidas')
print("\nIs number 4 in the list == 'asics'? I predict False")
print(sneakers[3] == 'asics')
print('--------------------------------------------')

top3_winners = ['tina', 'sky', 'angelo']
print('example 2')
print("Is second place held by == 'sky'? I predict True")
print(top3_winners[1] == 'sky')
print("\nIs first place held by == 'angelo'? I predict False")
print(top3_winners[0] == 'angelo')
print('--------------------------------------------')


# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# • Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.





# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to 10. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:
# • Tests for equality and inequality with strings
# correct_answers = [3, 10, 22, 45]
# if correct_answers != 2:
#     print('try again!')
# if correct_answers == 3:
#     print('you did it!')
# print('--------------------------------------------')
correct_answers = [3, 10, 22, 45]

if correct_answers == 3 and 10 or 22 or 45:
    print('you did it!')
else:
    print('try again!')
print('--------------------------------------------')
if correct_answers != 2:
     print('try again!')
print('--------------------------------------------')



card_pin = 2233
if card_pin == 2233:
    print('you can spend as much as you want')
print('--------------------------------------------')
if card_pin != 2323:
    print('error')
print('--------------------------------------------')

# • Tests using the lower() function
seasons = ['Summer', 'Autumn']
if seasons[0].lower() == 'summer':
    print('I love summer')
else:
    print('I love Autumn')
print('--------------------------------------------')
# • Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
# • Tests using the and keyword and the or keyword
# • Test whether an item is in a list
# • Test whether an item is not in a list

bicycles = 'trek', 'giant', 'cannondale'
if 'specialized' in bicycles:
    print('bicycles list includes specialized')
else:
    print(f'specialized is not in the bicycle list')
print('--------------------------------------------')

dolls = 'barbie', 'american girl', 'bratz'
if 'baby alive' and 'adora' in dolls:
    print('these are my favorite dolls')
else:
    print(f'I never played with these doll brands.')
print('--------------------------------------------')

if 'barbie' or 'bratz' in dolls:
    print("any of these for my birthday, please!")
print('--------------------------------------------')

# Problem 2 from elif
#  how can you loop through the list numbers and check that number 5 is in the list,
# when you find 5 then stop the loop print 'Hooraa'
# use 'break' keyword to stop the loop

# Break stops the loop. If printed outside the loop it is executable


for num in range(6):
    print(num)
    if num == 5:
        print('Hooraa')
        break
print('End of the list!')

# Problem1
# h/w if number divisible by 3 print 'Fuzz', if number divisible by 5 print 'Buzz',
#  if number divisible by 3 and 5 print 'FuzzBuzz'

# num = 15
# if num %3 ==0:
#     print('Fuzz')
# if num %5 == 0:
#     print('Buzz')
# if num %3 == 0 and num %5 == 0:
#     print('FuzzBuzz')
num = int(input('Please enter a number'))
if num != 0:
    if num %3 == 0 and num %5 == 0:
        print('FuzzBuzz')
    elif num % 3 ==0:
        print('Fuzz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print("this is not divisible by 3 or 5")
else:
    print('please enter a different number than 0')


# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live. You
# should have keys such as first_name, last_name, age, and city. Print each
# piece of information stored in your dictionary.

person = {'first_name': 'Julia', 'last_name': 'Stuart', 'age': 34, 'city': 'Chicago'}
print(f"first_name: '{person['first_name']}'.")
print(f"last_name: '{person['last_name']}'.")
print(f"age: '{person['age']}'.")
print(f"city: '{person['city']}'.")
print('----------------------------------------------')


# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

Glossary = {'title': 'first letter capital', 'append': 'add element end list',
            'del': 'delete object', 'index': 'return position of given index',
            'len': 'return number of items in object'}
print(f"title: '{Glossary['title']}'.\n")
print(f"append: '{Glossary['append']}'.\n")
print(f"del: '{Glossary['del']}'.\n")
print(f"index: '{Glossary['index']}'.\n")
print(f"len: '{Glossary['len']}'.\n")
print('---------------------------------------------------------')

# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.

Glossary = {'title': 'first letter capital', 'append': 'add element end list',
            'del': 'delete object', 'index': 'return position of given index',
            'len': 'return number of items in object'}
for word, meaning in Glossary.items():
    print(f'The function of {word.title()} command is: {meaning.title()}.\n')
print('---------------------------------------------------------')


# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.

Glossary['pop'] = 'remove item at given index'
Glossary['insert'] = 'add element at specified position'
Glossary['reverse'] = 'reverse order of the list'
Glossary['sort'] = 'sort the list'
Glossary['upper'] = 'convert string into upper case'
for word, meaning in Glossary.items():
    print(f'The function of {word.title()} command is: {meaning.title()}.\n')
print('---------------------------------------------------------')


# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
# variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
# • Write an if statement to test whether the alien’s color is green. If it is, print
# a message that the player just earned 5 points.
# • Write one version of this program that passes the if test and another that
# fails. (The version that fails will have no output.)

alien_color = ['green']
for color in alien_color:
    if color == 'green':
        print('You just earned 5 points')
print('---------------------------------------------------------')

for color in alien_color:
    if color == 'yellow':
        print('You just earned 5 points')
    else:
        print('Try again')
print('---------------------------------------------------------')

# 5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
# write an if-else chain.

# • If the alien’s color is green, print a statement that the player just earned
# 5 points for shooting the alien.
# • If the alien’s color isn’t green, print a statement that the player just earned
# 10 points.
# • Write one version of this program that runs the if block and another that
# runs the else block.



# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-
# else chain.
# • If the alien is green, print a message that the player earned 5 points.
# • If the alien is yellow, print a message that the player earned 10 points.
# • If the alien is red, print a message that the player earned 15 points.
# • Write three versions of this program, making sure each message is printed
# for the appropriate color alien.

alien_colors = ['green', 'yellow', 'red']
for color in alien_colors:
    if color == 'green':
        print('You just earned 5 points!')
    elif color == 'yellow':
        print('You just earned 10 points!')
    elif color == 'red':
        print('You just earned 15 points!')
print('---------------------------------------------------------')
#
# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
# stage of life. Set a value for the variable age, and then:
# • If the person is less than 2 years old, print a message that the person is
# a baby.
# • If the person is at least 2 years old but less than 4, print a message that
# the person is a toddler.
# • If the person is at least 4 years old but less than 13, print a message that
# the person is a kid.
# • If the person is at least 13 years old but less than 20, print a message that
# the person is a teenager.
# • If the person is at least 20 years old but less than 65, print a message that
# the person is an adult.
# • If the person is age 65 or older, print a message that the person is an
# elder.
# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
# independent if statements that check for certain fruits in your list.
# • Make a list of your three favorite fruits and call it favorite_fruits.
# • Write five if statements. Each should check whether a certain kind of fruit
# is in your list. If the fruit is in your list, the if block should print a statement,
# such as You really like bananas!


# 5-8. Hello Admin: Make a list of five or more usernames, including the name
# 'admin'. Imagine you are writing code that will print a greeting to each user
# after they log in to a website. Loop through the list, and print a greeting to
# each user:
# • If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?
#
# • Otherwise, print a generic greeting, such as Hello Eric, thank you for log-
# ging in again.

#  If list is empty we use else and print
# if list is not empty we use for loop

users = ['admin', 'salli', 'irma', 'neo', 'ace']
for user in users:
    if user == 'admin':
        print('Hello admin,would you like to see a status report?')
    elif user != 'admin':
        print(f'Hello {user.title()}, thank you for logging in again.')



#
# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct
# message is printed.
user_names = []
# if list is empty:
if not user_names:
    print('We need to find some users!')
else:
    for user in user_names:
        user = str(user)
        if user.lower() == "admin":
            print(f"$$$$$$  Hello admin, Would you like to see status report?")
        else:
            print(f"Hello {user}, thank you for logging in again")

# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username.
# • Make a list of five or more usernames called current_users.
# • Make another list of five usernames called new_users. Make sure one or
# two of the new usernames are also in the current_users list.
# • Loop through the new_users list to see if each new username has already
# been used. If it has, print a message that the person will need to enter a
# new username. If a username has not been used, print a message saying
# that the username is available.
# • Make sure your comparison is case insensitive. If 'John' has been used,
# 'JOHN' should not be accepted.

# 5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
# as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
# • Store the numbers 1 through 9 in a list.
# • Loop through the list.
#
# • Use an if-elif-else chain inside the loop to print the proper ordinal end-
# ing for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
#
# 7th 8th 9th", and each result should be on a separate line.
