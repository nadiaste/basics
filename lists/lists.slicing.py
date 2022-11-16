# Chapter 4: Slicing the list

pizzas = ['margherita', 'capriciosa', 'funghi', 'pepperoni', 'tres fommage', 'chicken']

for pizza in pizzas[0:3]:
    print(f'we have {pizza} pizza today')

print(pizzas[0:3])
# for pizza in pizzas[0:3]: includes index 0,1,2
# for pizza in pizzas[2:5]: includes index 2,3,4
# for pizza in pizzas[3:]: #means from 3rd index to the last index

for pizza in pizzas[:3]: # means from beginning of the list to the third element
    print(f'we have {pizza} pizza today')

print('------------- copy the list----------------')
new_pizzas = pizzas # creates new reference list to the same list
copy_pizzas = pizzas[:] # creates totally independent list (copy_pizzas)
print(f'Lists before updating {pizzas}\n{new_pizzas}\n{copy_pizzas}')
pizzas.append('four cheese')
copy_pizzas.append('new york')
copy_pizzas.append('caloroso')
print(f'Lists after updating {pizzas}\n{new_pizzas}\n{copy_pizzas}')

print('# Tuples - immutable data structure --------')
animals = ('dog', 'cat', 'horse')
dog_index= animals.index('dog')
print(f'index of the dog element in the tuple: {dog_index}')
sorted_animals = sorted(animals)
print(f'sorted animals: {sorted_animals}')
for animal in animals[0:2]:
    print(f'each animal : {animal}')

#H/W: 4-10, 4-11, 4-12
#styling the code: ctrl + alt + l