# To print a message
from itertools import islice

from pygments.lexer import words

print("Welcome")

'''
 this can be used for multiline comments
 You can use either single quotes or double quotes
 name = 'Sam'
 name = "Chris"
'''
current_year = 2025
print(current_year)
print(type(current_year))

current_year = "Two thousand and twenty five"
print(current_year)
print(type(current_year))

pi = 3.14
print(type(pi))

# Datatypes
# int, float, str, bool

# boolean
age = 20
isEligible = age > 17
print(isEligible)
print(type(isEligible))

if age > 17:
    print('Eligible for employment')
elif age > 58:
    print('Eligible for pension')
else:
    print('Not Eligible for employment')

# list - ordered, duplicates, changeable
car_list = ['i10','i20','swift','alto','i10']
print(car_list)

# for cars in car_list:
#     print(cars)
#     # if(cars == 'swift'):
#         # continue - stops the current iteration
#         # break # breaks the loop, else part wont be executed
#     print('Car printed')
# else:
#     print('End of iteration')

# # Tuple - ordered, duplicates, unchangeable
# car_list = ('i10','i20','swift','alto','i10')
# # print(type(car_list))
# #
# # for x in car_list:
# #     print(x)
#
# car_list[2] = 'corolla'
# print(car_list)

# duplicates not allowed, order is not mantained
# car_list = {'i10','i20','swift','alto','i10'}
# print(type(car_list))
#
# for cars in car_list:
#     print(cars)

# car_list = {"car1": "i10","car2":"i20"}
# print(car_list)
# print(type(car_list))
#
# print(len(car_list))
#

#
# x = 100
# x+=9
# print(x)
#
# countries = ['India', 'Romania', 'Poland','Moldova']
#
# print("Poland" in countries)
# print("Romania" not in countries)

# welcomemsg = "Welcome to Python Programming"
# print(welcomemsg[0])
# wordlist = welcomemsg.lower().capitalize().split(" ")
# print(wordlist)
# print(welcomemsg.find('P'))
# print(welcomemsg.index('P'))

name = 'Sam'
welcomemsg = f'Hi {name}, Welcome to Python Programming'
print(welcomemsg)
