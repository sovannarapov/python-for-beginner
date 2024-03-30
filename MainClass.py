from MyClass import Class


sp5 = Class('SP', '5', 4, 25)
sp6 = Class('SP', '6', 4, 12)
sp8 = Class('SP', '8', 4, 5)
sp15 = Class('SP', '15', 2, 9)

# overloaded operator (+, -, *, /, power, ...etc)
# when we want to calculate classes
# sp56 = sp5 + sp6
# sp7 = sp5 - sp6
# sp8 += 10

if sp8 > sp15:
    print('SP8 is greater than SP15')
else:
    print('SP8 is less than SP15')

# print(sp56)
# print(sp7)
# print(sp8)
