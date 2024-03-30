from Product import *
# from msvcrt import getch

p1, p2, p3, disc = input_product()
total, disc_price, payment = calculate(p1, p2, p3, disc)
display_price(total, disc_price, payment)
# getch()
