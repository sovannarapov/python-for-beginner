class People:
    # Use double underscore sign __ in front of variable to declare private variable
    # constructor with parameters
    def __init__(self, id, name, age, address):
        self.__id = id
        self.__name = name
        self.__age = age
        self.__address = address

    # toString() method
    def __str__(self):
        return f'{self.__id:03}\t{self.__name}\t{self.__age}\t{self.__address}'

    # getter & setter
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address
