# Functions with return statement

def build_full_name(firstname, lastname):
    '''Returns beautiful full name.'''
    print('starting to build the full name...')
    full_name =f'{firstname} {lastname}'
    return full_name.title()

print("Result of the function: ", build_full_name('john', 'doe'))
person2 = build_full_name('john', 'doe')
print('Person2: ', person2)

'''
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned.
'''

def city_country(city: str, country: str):
    '''returns name of the city with country'''
    return f"{city.title()}, {country.title()}"


print('________8-6 _________________________________')
print(city_country('paris', 'france'))
print(city_country('london', 'united kingdom'))
print(city_country('new york', 'united states'))

 # H/W  8-7, 8-8               