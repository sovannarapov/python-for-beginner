class People:
    # constructor with parameter
    def __init__(self, _id, name, age, address):
        self._id = _id
        self.name = name
        self.age = age
        self.address = address

    # toString() method
    def __str__(self):
        return f'{self._id}\t{self.name}\t{self.age}\t{self.address}'


p = People(1, 'sovannara', 25, 'pp')
# p._id = 1
# p.name = 'sovannara'
# p.age = 25
# p.address = 'pp'

print(p)
