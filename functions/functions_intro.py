# Chapter 8: Functions (methods)
# defining, executing functions, docstring
# function overriding - resetting the content with same name
# wrong way of using the functions: calling before defining: Unresolved reference
# functions with parameters (arguments are passed when you execute)
# executing functions with positional arguments
# executing functions with parameters and arguments mentioned, position does not matter
# keyword arguments, passing the values mentioning the parameters

# built-in functions: print(arg1, arg2), input(), list.append(), sorted(),
# User defined functions, functions that user created
def greet_user():
    print("hello class!")
    print("Wonderful sunny day today!")

# Execution: call the function. If you call it many times, it will be executed many times
greet_user()


# overriding the function
def greet_user():
    print("hello world!")
    print("Enjoy your day!")


def greet_user_by_name(name, day_of_week):
    """function with argument: positional argument, required"""
    print(f"Hello, {name.title()}!")
    print(f"Enjoy your {day_of_week} today!")

def greet_user_by_name_with_def(name, day_of_week='monday'):
    """
    function with default value: name is required, day_of_the_week is not required
    """

    print(f"Hello, {name.title()}!")
    print(f"Enjoy your {day_of_week} today!")


# we are defining the function, declaring the function name
# registering in the python executable system

# Execution: call the function
greet_user()
print('logged in to the system')
greet_user()
greet_user_by_name("jane", 'Saturday')
greet_user_by_name("beni", 'sunday')
greet_user_by_name("mike", 'monday')
greet_user_by_name('monday', "mike")
print("# Keyword arguments -------------------------------------")
greet_user_by_name(day_of_week='monday', name="mike")
# H/w: 8-1, 8-2

print("# Default values -------------------------------------")
greet_user_by_name_with_def("kamran", 'sunday')
greet_user_by_name_with_def("nadia")
greet_user_by_name_with_def('jamshid', day_of_week='monday')
greet_user_by_name_with_def(day_of_week='wednesday', name="nina")

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

# h/w 8-4, 8-5