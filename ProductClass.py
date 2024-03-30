class Product:
    def __init__(self, pid, pname, price, qty):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.qty = qty

    def amount(self):
        return self.price * self.qty

    def __str__(self):
        return f'{self.pid:03}\t{self.pname}\t{self.price:,.2f}\t{self.qty}\t{self.amount():,.2f}'
