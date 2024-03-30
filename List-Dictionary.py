# ls = [(11, 22, 33), (44, 55, 66)]
#
# for tp in ls:
#     for v in tp:
#         # print until end then enter new line
#         print(v, end='')
#     print()

# peoples = [{'id': 1, 'name': 'python'}, {'id': 2, 'name': 'java'}, {'id': 3, 'name': 'c#'}]
#
# for people in peoples:
#     for value in people.values(): # loop access value of people
#         print(f'{value}\t', end='')
#     print()

peoples = []
amountOfPeople = int(input('Enter amount of people='))

if amountOfPeople > 0:
    for i in range(0, amountOfPeople):
        people = {}
        people['id'] = int(input('Enter ID='))
        people['name'] = input('Enter Name=')
        people['age'] = input('Enter Age=')
        people['address'] = input('Enter Address=')
        peoples.append(people)
        print('-----------------------------------')

    print('id\tname\tage\taddress', end='')
    print()

    for people in peoples:
        for value in people.values():
            print(f'{value}\t', end='')
        print()

# List comprehension approach
# Demonstrate how to use list comprehension to simplify code that generate a list of square for all even number from 0 - 10
# Traditional approach
# squares = []
# for number in range(11):
#     if number % 2 == 0:
#         squares.append(number*2)
# print('Traditional', squares)

# List comprehension approach
squares = [number*2 for number in range(11) if number % 2 == 0]
print('List comprehension', squares)
