def input_product():
    p1 = float(input('Enter P1 =$'))
    p2 = float(input('Enter P2 =$'))
    p3 = float(input('Enter P3 =$'))
    disc = float(input('Enter Discount ='))
    return p1, p2, p3, disc


def calculate(p1, p2, p3, disc):
    total = p1 + p2 + p3
    disc_price = total * disc / 100
    payment = total - disc_price
    return total, disc_price, payment


def display_price(total, disc_price, payment):
    print('----------------------------')
    print(f'Total = ${total:,.2f}')
    print(f'Discount Price = ${disc_price:,.2f}')
    print(f'Payment = ${payment:,.2f}')
