# Chapter 5: ELIF STATEMENTS
#  else if >> elif

# if expression1:
#     code to execute when expression1 is True
# elif expression2:
#     code to execute when expression2 is True
# elif expression3:
#     code to execute when expression3 is True
# elif expression3:
#     code to execute when expression3 is True
# else:
#     code to execute when none of the above expressions are True

# Q: if age is less than 17 then you can not get a DL, from 17-25 pay more insurance,
# older than 25 print don't drink and drive
#age = 26
# #age = int(age)
# age = int(input('Please enter your age:'))
# if age < 17:
#     print('Sorry, cannot drive yet')
# elif age >= 17 and age < 25:
#     print('Good, you are eligible to get a DL, but will pay mor for Insurance')
# elif age >= 25:
#     print('If you have a DL, please do not Drink and Drive')

#  to simplify this upper code, last elif, can use else:
# #age = 30
# if 0 < age < 17:
#     print('Sorry, cannot drive yet')
# elif age >= 17 and age < 120:
#     print('Good, you are eligible to get a DL, but will pay mor for Insurance')
# else:
#     print('Come on be realistic, unless you are a vampire')

#  repeat consecutively a code using range()
for i in range(5):
    print(f'Iteration # : {i}')
#age = 30
# age = int(age)
    age = int(input('Please enter your age:'))
    if 0 < age < 17:
        print('Sorry, cannot drive yet')
    elif age >= 17 and age < 120:
        print('Good, you are eligible to get a DL, but will pay mor for Insurance')
    else:
        print('Come on be realistic, unless you are a vampire')


#          Interview questions:
# Problem1
# h/w if number divisible by 3 print 'Fuzz', if number divisible by 5 print 'Buzz',
#  if number divisible by 3 and 5 print 'FuzzBuzz'

n= 3
if n %3 == 0:
    print('divisible by 3')
    #break  #this will stop the loop
    #print('abcde') # this line will not be executable because of the break
else:
    print('this is not divisible by 3')

# Problem 2
#  how can you loop through the list numbers and check that number 5 is in the list,
# when you find 5 then stop the loop print 'Hooraa'
# use 'break' keyword to stop the loop

# Break stops the loop. If printed outside the loop it is executable




