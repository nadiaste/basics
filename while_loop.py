# Chapter 7: user input and while loop

name = 'john'


# while expression:
#     code to repeatedly execute with each iteration
#     code to repeatedly execute with each iteration
#     code to repeatedly execute with each iteration
#     code to change the expression

# Be cautious of INFINITE loop,
# to avoid make sure the condition is changing with each iteration
current_number = 1
while current_number <= 5:
    print("current number: ", current_number)
    current_number += 1 # shortcut += 1 to add +1 to current_number
#   current_number = current_number +1

current_number = 1
while current_number > -10:
    print("current number: ", current_number)
    current_number -= 1


def while_loop_increment():
    """
    Docstring - While loop when we are setting upper limit in the condition, we need to increment
    :return:
    """
    print("While loop when we are setting upper limit in the condition, we need to increment")
    current_number = 1
    while current_number <= 2:
        print('current number :', current_number)
        current_number = current_number + 1


def while_loop_decrement():
    """Docstring - "While" loop when we are setting bottom limit in the condition, we need to decrement
    :return:"""
    print("While loop when we are setting bottom limit in the condition, we need to decrement")
    current_number = 1
    while current_number > 0:
        print('current number :', current_number)
        current_number = current_number - 1

# print("_______ Fuzz Buzz example with while loop ___________")
# answer = ''
# while (answer.lower() != 'n') and (answer.lower() != 'no'):
#         # n == n -> True, n != n -> False, not executable , y != n -> True, '' != n -> True
#     num = int(input('Please enter a number: '))
#         # num = 3
#     if num != 0:
#         if num % 3 == 0 and num % 5 == 0:
#             print('FuzzBuzz')
#         elif num % 3 == 0:
#             print('Fuzz')
#         elif num % 5 == 0:
#             print('Buzz')
#         else:
#             print('This is not divisible by 3 or 5')
#     else:
#         print("please enter different number than 0")
#     answer = input("Do you want to continue? y/n: ")

# While loop exercise from book
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# fuzz_buzz()
def fuzz_buzz():
    print("_______ Fuzz Buzz example with while loop ___________")
    answer = ''
    while (answer.lower() != 'n') and (answer.lower() != 'no'):
        # n == n -> True, n != n -> False, not executable , y != n -> True, '' != n -> True
        num = int(input('Please enter a number: '))
        # num = 3
        if num != 0:
            if num % 3 == 0 and num % 5 == 0:
                print('FuzzBuzz')
            elif num % 3 == 0:
                print('Fuzz')
            elif num % 5 == 0:
                print('Buzz')
            else:
                print('This is not dividable by 3 or 5')
        else:
            print("please enter different number than 0")
        answer = input("Do you want to continue? y/n: ")


# fuzz_buzz()
# while_loop_increment()
# while_loop_decrement()

#  Examplex chapter 7 with input promps

# prompt = "Let us know more about you, for better assistance."
# prompt += "\nHow old are you?"
#
# age = input(prompt)
# print("\nI am" + age + '!')




# Start with users that need to be verified,
# and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)