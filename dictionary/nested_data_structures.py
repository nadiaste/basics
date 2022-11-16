alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

print(aliens)
print(aliens[1]) #{'color': 'yellow', 'points': 10}
print(aliens[1]['color']) #'yellow'
print(aliens[1]['points']) #'10'
print(f"alien 1 color is: {aliens[1]['color']} \nand points: {aliens[1]['points']}")

aliensd = {'alien_0': {'color': 'green', 'points': 5},
           'alien_1' : {'color': 'yellow', 'points': 10},
           'alien_2' : {'color': 'red', 'points': 15}}

print(aliensd['alien_1']['color']) #'yellow'
print(aliensd['alien_1']['points']) #'10'
print(f"alien 1 color is: {aliensd['alien_1']['color']} \nand points: {aliensd['alien_1']['points']}") # both