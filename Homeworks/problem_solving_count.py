# def count(string):
#     dict = {}
#     for n in string:
#         keys = dict.keys()
#         if n in keys:
#             dict[n] += 1
#         else:
#             dict[n]= 1
#     return dict
#
# print(count('BGhhhTTyyyug'))


# initializing string
def test_str(): #= "GeeksforGeeks"

# using dict.get() to get count
# of each element in string
    dict = {}

    for keys in test_str:
        dict[keys] = dict.setdefault(keys, 0) + 1

# printing result
print("Count of all characters in GeeksforGeeks is : \n" + str(dict))