# 8-1. Message: Write a function called display_message() that prints one sentence
# telling everyone what you are learning about in this chapter. Call the
# function, and make sure the message displays correctly.

def display_message():
    print("I'm learning about functions in this chapter.")

display_message()


# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice in Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.

def favorite_book(title):
    print("\nOne of my favorite books is: " + title.title() + '.')

favorite_book('alice in wonderland')


# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.

print('############ exercise 8-3 ###############')
def make_shirt(size, text_to_print):
    '''
    Print message and size of the shirt
    :return:
    '''
    print(f'The size of your shirt is: {size}.')
    print(f"The message to be printed on your shirt is: \n\t\t'{text_to_print}'")

make_shirt('medium','Level Up cgi') #- this is positional argument
make_shirt(text_to_print='Level Up cgi', size= 'medium') # this is keyword argument

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different message.

print('############ exercise 8-4 ###############')
def make_shirt(size, text_to_print='I love Python'):
    '''
    Print message and size of the shirt
    :return:
    '''
    print(f'The size of your shirt is: {size}.')
    print(f"The message to be printed on your shirt is: \n\t\t'{text_to_print}'")

make_shirt('large')
make_shirt(size= 'medium')
make_shirt('X-small', 'Python 4ever')
make_shirt(text_to_print='Python 4ever!!!!', size= 'XL')



# 8-5. Cities: Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.


print('############ exercise 8-5 ###############')
def describe_city(city_name, country_name= "Italy"):
    '''print a simple sentence and accept city and default country name'''
    print(f'{city_name.title()} is located in {country_name.title()}.')

describe_city('padova')
describe_city(city_name= 'Venice')
describe_city('berlin', 'germany')


# 8-7. Album: Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.


print('############ exercise 8-7 ###############')
def make_album(artist_name, album_title):
    '''function returns dictionary describing a music album'''
    # album = {'artist': artist_name, 'title': album_title}
    # return album   # this is correct but you can also write this like this
    return {'artist': artist_name, 'title': album_title}

album = make_album('John Doe', "country")
print("First album: ", make_album('John Doe', "country"))
print("Second album: ", make_album('Jane Sue', "jazz"))
print("Third album: ", make_album('Lilly May', "rock"))

# Add an optional parameter to make_album() that allows you to store the
# number of tracks on an album. If the calling line includes a value for the number
# of tracks, add that value to the album’s dictionary. Make at least one new
# function call that includes the number of tracks on an album.

print('############ exercise 8-7 part 2 ###############')
def make_album_tracks(artist_name, album_title, tracks_count=0):
    '''function returns dictionary describing a music album'''
    album = {'artist': artist_name, 'title': album_title}
    # if tracks_count:
    #     album['tracks_count']= tracks_count
    # return album
    if tracks_count > 0:
        #add tracks key value pair to dictionary
        album['tracks_count']= tracks_count
        return album
album = make_album_tracks('John Doe', "country", 1)
print(album)
album1 = make_album_tracks('Jane Sue', "jazz", 15)
print(album1)
album2 = make_album_tracks('Lilly May', "rock", 8)
print(album2)
# album2.setdefault()


# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

print('############ exercise 8-8 ###############')
#
# def make_album_8(artist_name, album_title):
#     '''function returns dictionary describing a music album'''
#     album = {'artist': artist_name, 'title': album_title}
#     return album
# while True:
#     print("\nPlease enter the album's artist name and title")
#     print("(enter 'q' at any time to quit)")
#     artist_name = input('artist: ')
#     album['artist'] = artist_name
#     if artist_name == 'q':
#         break
#     album_title = input('title: ')
#     album['title'] = album_title
#     if album_title == 'q':
#         break
# print(album)

# new_album = ''
# while new_album != 'n':
#     artist = input('Enter the artist name: ')
#     alb = input('Enter the album name: ')
#     trck = input('Enter the track number: ')
#     trck = int(trck)
#     album5 = make_album_tracks(artist, alb, trck)
#
#     print('album5:', album5)
#     new_album = input('do you want to continue? y/n: ')

# Problem solving (amazon):
# write a function that returns letters with counts, i.e how many times each letter is used in the string (word, sentence, bigger text...)
# Sample Input and Output: 'hello' -> {'h':1, 'e':1, 'l':2, 'o':1}
# album['letter'] += tracks #adding the value to a previous value of the key in the dictionary
# album['letter'] = album['letter'] + tracks


# letter_counts= '0'
#     # '''return dictionary with letter counts'''
#     # return {"word": word, "count": letter_count}
# while letter_counts != '0':
#     letter_counts['word'] += input('Enter a word: ')
#     letter_counts['letter_count'] += input ("Enter letter count: ")
#     letter_counts = dict.setdefault(word, letter_count)
#
#     print(letter_counts)
#     letter_counts = input('Do you want to continue: y/n? ')

def count(string):
    dict = {}
    for n in string:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n]= 1
    return dict

count(count('BGhhhTTyyyug'))



