# First name (string)
# Last name (string)
# Age (integer)
# Cohort number (integer)
# Full name (read-only string)
class Student():
    
    @property # The getter
    def first_name(self):
        try:
            return self.__first_name # Note there are 2 underscores here
        except AttributeError:
            return ''

    @first_name.setter # The setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError('Please provide a string value for the first_name')

    @property # The getter
    def last_name(self):
        try:
            return self.__last_name # Note there are 2 underscores here
        except AttributeError:
            return ''

    @last_name.setter # The setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError('Please provide a string value for the last_name')

    @property # The getter
    def age(self):
        try:
            return self.__age # Note there are 2 underscores here
        except AttributeError:
            return 0

    @age.setter # The setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('Please provide an integer value for the age')

    @property # The getter
    def cohort_number(self):
        try:
            return self.__cohort_number # Note there are 2 underscores here
        except AttributeError:
            return 0

    @cohort_number.setter # The setter
    def cohort_number(self, new_cohort_number):
        if type(new_cohort_number) is int:
            self.__cohort_number = new_cohort_number
        else:
            raise TypeError('Please provide an integer value for the cohort_number')
    
    @property # The getter
    def full_name(self):
        try:
            return (f'{self.__first_name} {self.__last_name}') # Note there are 2 underscores here
        except AttributeError:
            return ''
            
test = Student()
test.first_name = "Michelle"
test.last_name = "Johnson"
test.age = 27
test.cohort_number = 36
print(test.first_name,test.last_name,test.age, test.cohort_number, test.full_name)