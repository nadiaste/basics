nums = [] #empty
nums = [4, 10, 6]
friends = []
players = list() #creates empty list
names = ['john', 'mark', 'jane']
bool_values = [True, False, True]
print(nums)
print(names)
print('Hi, ', names[1].title())
print('Hi, ', names[0].title())
## listname.append(newvalue) - adds newvalue to the end of the list
#other values shifted to the left
names.append('alex')
print(names)
#listname.insert()
names.insert(0, 'nadia')
print(names)
#updating the last element of the list 'alex' -> 'andreea'
names[-1] = 'andreea'
print(names)
#removing can be done
#remove element by index using del listname[]. Removing 'jane'. elements after 'jane' shifted to the left.Index changed
del names[3]
print(names)
#remove element by index using listname.pop() - it removes the last in the list
names.pop()
print(names)
names.pop(0)
print(names)

# by value using listname.remove(value)
names.remove('mark')
print(names)

###  10/16/22
# Excercises (Chapter 3 book  ex 3-7)
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

print('----------------------------------------------')
print('Hi everyone, we you found a bigger dinner table and now we have more space!')
print('----------------------------------------------')


guests.insert(0, 'alex')
print(guests)
guests.insert(2, 'vika')
print(guests)
print('----------------------------------------------')
guests.append('benny')
print(guests)
guests.append('eldar')
print(guests)




