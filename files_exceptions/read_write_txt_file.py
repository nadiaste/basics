# Chapter 10: files and Exceptions

# with open('filepath') as aliasNameForTheFile:
#     line1 = aliasNameForTheFile.readline()
#     line2 = aliasNameForTheFile.readline()
#     line3 = aliasNameForTheFile.readline()
#
#     all_lines = aliasNameForTheFile.readlines(), list of values
#
#     file_content = aliasNameForTheFile.read()
#     aliasNameForTheFile.close(), no need to close when you read
filepath1 = '../data/product.txt' # .. relative path, better use and share because not everyone has the files in the same location
filepath = 'c:/dev/basics/data/product.txt'



# with open('../data/product.txt') as prod_list:
print('**************** Read file *****************')
with open(filepath) as prod_list:
    contents = prod_list.read()
    print("Contents of the file:\n", contents)

with open('../data/product.txt', 'r') as prod_list:
    print("now we are trying to loop through the contents")
    all_lines = prod_list.readlines()
    print(all_lines)
print('printing line 5: ', all_lines[4])

for line in all_lines:
    print(line)

print('**************** WRITE file appending new content *****************')
with open(filepath, 'a') as prod_list:
    prod_list.write('\nplaystation 5\n')
    prod_list.write('Learning Python book\n')
    prod_list.write('First head to Selenium book\n')
    print("Contents of the file:\n", contents)

# print('*** WRITE file rewriting new content(delete old content)****')
# with open(filepath, 'w') as prod_list:
#     prod_list.write('spiderman jacket\n')
#     prod_list.write('batman mask\n')
#     prod_list.write('smart tv samsung 70"\n')
#     print("Contents of the file:\n", contents)
    #chech the file contents

# H/W: 10-3, 10-4, 10-5