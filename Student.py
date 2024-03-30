from People import People


class Student(People):  # inheritance
    def __init__(self, id, name, age, address, subject, gpa):
        super().__init__(id, name, age, address)
        self.__subject = subject
        self.__gpa = gpa

    def __str__(self):
        return super().__str__() + f'\t{self.__subject}\t{self.__gpa}'

    def get_subject(self):
        return self.__subject

    def set_subject(self, subject):
        self.__subject = subject

    def get_gpa(self):
        return self.__gpa

    def set_gpa(self, gpa):
        self.__gpa = gpa
