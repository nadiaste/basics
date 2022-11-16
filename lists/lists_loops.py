# Chapter 4: Looping through the entire list

places = ['hawaii', 'paris', 'milan', 'london', 'kiiv']
# Loops - executing the code repetitively (what to look through, how many times)
print('Looping through the entire list: ')
print(f'I want to visit {places[0]} next summer')
# for var_each_element in iterative:
#    print('lines of code to be repeated')
print('we are looping through places')
for place in places:
    #comment line
    #print(a)
    print(f'I want to visit {place.title()} next summer')
print(f'ohhhh, I need to convince my wife now.')
#print(f'How far is the {place.title()} from new york?')
# sample for loop in Java to see the difference with Python loop
#  for a in places{
#     print(a)
# }

print('working with list of numbers, range() functions')
# range(5) -> 0, 1, 2, 3, 4
#  range (2, 6) -> 2, 3, 4, 5
#  range (4, 16, 3) -> 4, 7, 10, 13
print(range(5))
print(list(range(5)))
for num in range(5):
    print(f'Each number: {num}')

#nums = list(range(5))
#for num in nums:
#    print(f'Each number : {num}')

for num in range(5):
    print(f'Each number : {num}')
print('================================')

for num in range(2, 6):
    print(f'Each number : {num}')
print('================================')

for num in range(4, 16, 3):
    print(f'Each number : {num}')
print('================================')

print('# Problem solving:')
print('# problem: list all numbers between 21 and 36 that can be divided by 4')

for num in range(24, 37, 4):
    print(f'Each number : {num}')

print('# problem2: create a list of the squares of numbers between 25 and 30')
num_squares = []
for num in range(25, 31):
    print(f'num = {num} and square is: {num**2}')
    num_squares.append(num**2)
print('final list of squares', num_squares)
