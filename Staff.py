from People import People


class Staff(People):
    def __init__(self, id, name, age, address, job_title, salary):
        super().__init__(id, name, age, address)
        self.__job_title = job_title
        self.__salary = salary

    def __str__(self):
        return super().__str__() + f'\t{self.__job_title}\t{self.__salary}'

    def get_job_title(self):
        return self.__job_title

    def set_job_title(self, job_title):
        self.__job_title = job_title

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

