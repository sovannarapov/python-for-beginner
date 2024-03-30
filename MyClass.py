class Class:
    def __init__(self, name, no, year, student):
        self.__name = name
        self.__no = no
        self.__year = year
        self.__student = student

    def __str__(self):
        return f'Name    : {self.__name} {self.__no}\n' \
               f'Year    : {self.__year}\n' \
               f'Student : {self.__student}'

    def get_no(self):
        return self.__no

    def set_no(self, no):
        self.__no = no

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_year(self):
        return self.__year

    def set_year(self, year):
        self.__year = year

    def get_student(self):
        return self.__student

    def set_student(self, student):
        self.__student = student

    # Override method
    def __add__(self, other):
        if type(other) is Class:
            no = f'{self.__no}.{other.get_no()}'
            student = self.__student + other.get_student()
            return Class(self.__name, no, self.__year, student)
        else:
            return Class(self.__name, self.__no, self.__year, (self.__student+other))

    def __sub__(self, other):
        student = self.__student-other
        return Class(self.__name, self.__no, self.__year, student)

    def __gt__(self, other):
        return self.get_year() > other.get_year()
