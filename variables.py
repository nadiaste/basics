print("Hello World!")
print ('Hello, this is my first coding practice!')
msg = "Hello, this is my first coding practice!" # string
name = 'john doe'
print ('name before title', name)
print ('name with title:', name.title())
print ('name after title', name)
print ('using is lower:', name.islower())
print ("# concatenation ")
print ("my message: " + name + ', ' + msg)
print ("my message: " + name.title() + ', ' + msg.upper())
print ("Special characters : \\t \\n")
print ("my message: \t\t\t" + name.title() + ', \n\t\t\t\t' + msg.upper())
print ('Message to everyone:\n\t\t\tplease have fun! !')
# SyntaxError, NameError

location = '   \thawai\n\t'
print(location)
print ('my wedding venue: ' + location.strip().upper()+ " islands")
# working with numbers #
num1 = 3
num2 = 8
print('addition: ', num1 + num2)
print('subtraction: ', num2 - num1)
print('multiplication: ', num1 * num2)
print('division: ', num1 / num2)
print('exponent: ', num1 ** 2)
print('floor division: ', num2 // num1)
print('modulo: ', num2 % num1)
print('addition: :' +str(num1 + num2))
num3 = '456' # this is a string data type
num4 = 45.7566 # this is a float data type, int(num4) will get only int part of it
print('addition with num3: ' , num1 + int(num3))
print('converted to int: ' , int(num4))