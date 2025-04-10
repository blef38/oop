class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def aver(self):
        average_length = sum(len(v) for v in self.grades[grade]) / len(self.grades)
        print(average_length)
        return average_length

    def __str__(self):
        return f'Имя: {self.name}, фамилия: {self.surname}, средняя оценка: {self.aver}'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


Dyatlov = Student('Семен', 'Дятлов', 'your_gender')
Dyatlov.courses_in_progress += ['Python']
Dyatlov.courses_in_progress += ['Math']

Antonov = Reviewer('Андрей','Антонов')
Antonov.courses_attached += ['Python', 'Math']

Dymov = Lecturer('Сергей','Дымов')
Dymov.courses_attached += ['Python', 'Math']

# Ivanov = Reviewer('Владимир','Иванов')
# Ivanov.courses_attached += ['Python']
#
# Ivanov.rate_hw(Dyatlov, 'Python', 7)
# Antonov.rate_hw(Dyatlov, 'Python', 8)
# Antonov.rate_hw(Dyatlov, 'Math', 10)
# Antonov.rate_hw(Dyatlov, 'Python', 3)
# Antonov.rate_hw(Dyatlov, 'Math', 5)
#
# print(Dyatlov.name, Dyatlov.surname, Dyatlov.grades)

Dyatlov.rate_lec(Dymov, 'Python', 8)
Dyatlov.rate_lec(Dymov, 'Python', 5)
Dyatlov.rate_lec(Dymov, 'Math', 9)
Dyatlov.rate_lec(Dymov, 'Math', 4)

print(Dymov.name, Dymov.surname, Dymov.grades)

