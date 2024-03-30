# patient_name = "John Smith"
# patient_age = 20
# print(type(patient_age)) # check datatype
# print(id(patient_age)) # check address variable
# print("We check in a patient name " + patient_name)
# print("He is ", patient_age, "years old")
# print("He is a new patient.")
# from MyLib import *
from ProductClass import *

# first = float(input("First: "))
# second = float(input("Second: "))
# sum = first + second
# print('Sum: {0:,.2f}'.format(sum)) # print value by index and format
# print(f'Sum: {sum:,.2f}') # print value by variable and format

# weight = float(input("Weight: "))
# unit = str(input("(K)g or (L)bs: "))
#
# if unit.upper() == 'L':
#     convertedWeight = weight * 0.45
#     print("Weight in Kg: ", convertedWeight)
# elif unit.upper() == 'K':
#     convertedWeight = weight / 0.45
#     print("Weight in Lbs: ", convertedWeight)
# else:
#     print("Invalid chosen!")

# index = 1
# while index <= 5:
#     print(index)
#     index += 1

# list
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for item in numbers:
#     print(item)

# mostly range() use in for loop
# don't need to store result in seperate variable
#for number in range(5):
#    print(number) # 0 1 2 3 4

# tuple is unchangable, unassignable, readonly
# tp = (1, 2, 3, 4, 5)
# tp[0]=10 # error
# for el in range(len(tp)):
#    print(f"tp[{el}]={tp[el]}")

# set is the same as list
# data in set is unorder, no index, and not redundant
# st = set() # or st = {1, 2, 3, 4, 5}
# print(type(st))
# st = {1, 2, 3, 4, 4, 5, 6}
# print(st) # 1 2 3 4 5 6
# print(st[0]) # error

# dictionaries is unorder, changable
# data in dictionaries is key & value
# dic = dict() # or dic = { "id": 1, "name": "python" }
# print(type(dic))
# dic = {"id": 1, "name": "python"}
# print(dic.get("name")) # get value by key using get() method
# print(dic["name"]) # get value by key
# dic["id"]=2 # update value by key
# print(dic["id"])
# dic["address"]="phnom penh" # update value by key if key not exist automatically add new
# print(dic)
# loop to access key & value
# for k, v in dic.items():
#    print(f"Dic[{k}]={v}")

# do while loop
# while True:
#     score = float(input('Enter score='))
#     if 0 <= score <= 100:
#         break
# print(f'Your score is {score}')

# display_name('Sovannara')
# display_number(20)

products = []
amountOfProduct = int(input('Enter amount of product='))

if amountOfProduct > 0:
    for i in range(0, amountOfProduct):
        pid = int(input('Enter product id='))
        pname = input('Enter product name=')
        price = float(input('Enter price='))
        qty = int(input('Enter quantity='))
        product = Product(pid, pname, price, qty)
        print(f'Amount=${product.amount():,.2f}')
        products.append(product)
        print('--------------------------------------')

    total = 0
    for product in products:
        total += product.amount()

    print(f'\t\t\t\tTotal=${total:,.2f}')
