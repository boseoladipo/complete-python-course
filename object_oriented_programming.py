my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 88, 90, 99]
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])

print(average_grade(my_student))

class Student:
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grades = new_grade

    def average(self):
        return sum(self.grades)/len(self.grades)

student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose', [50, 60, 99, 100])

print(student_one.name)
print(student_two.name)

print(student_one.average())

class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year

print(Movie('The Matrix', 1994).name)

movies = ['Matrix', 'Finding Nemo']
print(movies.__class__)

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self):
        return f'<Garage {self.cars}>'

    # def __str__(self):
    #     return f'Garage with {len(self)} cars.'

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(ford)

#%%
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent:
    def __init__(self, name, school, salary):
        self.name = name
        self.school = school
        self.marks = []
        self.salary = salary

    def average(self):
        return sum(self.marks)/ len(self.marks)

rolf = WorkingStudent('Rolf', "MIT", 15.50)
print(rolf.salary)


# %%
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 37.5

rolf = WorkingStudent('Rolf', "MIT", 15.50)
print(rolf.weekly_salary)

# %%
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)

my_object = Foo()
my_object.hi()

class Bar:
    @staticmethod
    def hi():
        print('Hello, I don\'t take parameters')

another_object = Bar()
another_object.hi()


# %%
class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)

number = FixedFloat(18.5746)
new_number  = FixedFloat.from_sum(19.575, 0.789)
# print(new_number)

class Euro(FixedFloat):
    """
    Class that defines currency of the European people
    """
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}'

money = Euro.from_sum(18.588, 84.32)
print(money)

# %%
