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
    # def aver(self):
    #     average_length = sum(len(v) for v in self.grades[grade]) / len(self.grades)
    #     print(average_length)
    #     return average_length
    def avg_rate(self):
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        return round(sum(all_grades) / len(all_grades), 2) if all_grades else 0

    def __str__(self):
        return (f'Имя: {self.name}, \nФамилия: {self.surname}, '
                f'\nСредняя оценка за домашние задания: {self.avg_rate()},'
                f'\nКурсы в процессе изучения: {self.courses_in_progress},'
                f'\nЗавершенные курсы: {self.finished_courses}')

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.avg_rate() == other.avg_rate()
        return False

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.avg_rate() < other.avg_rate()
        return False

    def __gt__(self, other):
        if isinstance(other, Student):
            return self.avg_rate() > other.avg_rate()
        return False

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
    def avg_rate(self):
        all_grades = [grade for course_grades in self.grades.values() for grade in course_grades]
        return round(sum(all_grades) / len(all_grades), 2) if all_grades else 0
    def __str__(self):
        return f'Имя: {self.name}, \nФамилия: {self.surname}, \nСредняя оценка за лекции: {self.avg_rate()}'
    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_rate() == other.avg_rate()
        return False

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_rate() < other.avg_rate()
        return False

    def __gt__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_rate() > other.avg_rate()
        return False

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
    def __str__(self):
        return f'Имя: {self.name}, Фамилия: {self.surname}'

def rate_st_avg_for_all_courses(stud_list, course):
        all_grades = []
        for stud in stud_list:
            all_grades += stud.grades[course]
        print(all_grades)
        return round(sum(all_grades) / len(all_grades), 2) if all_grades else 0


def rate_lec_avg_for_all_courses(lec_list, course):
    all_grades = []
    for lec in lec_list:
        all_grades += lec.grades[course]
    print(all_grades)
    return round(sum(all_grades) / len(all_grades), 2) if all_grades else 0

Dyatlov = Student('Семен', 'Дятлов', 'your_gender')
Dyatlov.courses_in_progress += ['Python']
Dyatlov.courses_in_progress += ['Math']

Petrov = Student('Иван', 'Петров', 'your_gender')
Petrov.courses_in_progress += ['Python']

Antonov = Reviewer('Андрей','Антонов')
Antonov.courses_attached += ['Python', 'Math']

Dymov = Lecturer('Сергей','Дымов')
Dymov.courses_attached += ['Python', 'Math']

Dmitriev = Lecturer('Андрей','Дмитриев')
Dmitriev.courses_attached += ['Python', 'Math']

Ivanov = Reviewer('Владимир','Иванов')
Ivanov.courses_attached += ['Python']

Ivanov.rate_hw(Dyatlov, 'Python', 7)
Antonov.rate_hw(Dyatlov, 'Python', 8)
Antonov.rate_hw(Dyatlov, 'Math', 10)
Antonov.rate_hw(Dyatlov, 'Python', 3)
Antonov.rate_hw(Dyatlov, 'Math', 5)

Antonov.rate_hw(Petrov, 'Math', 2)
Antonov.rate_hw(Petrov, 'Python', 1)
Antonov.rate_hw(Petrov, 'Python', 5)

# print(Dyatlov.name, Dyatlov.surname, Dyatlov.grades)

Dyatlov.rate_lec(Dymov, 'Python', 8)
Dyatlov.rate_lec(Dymov, 'Python', 5)
Dyatlov.rate_lec(Dymov, 'Math', 1)
Dyatlov.rate_lec(Dymov, 'Math', 4)

Dyatlov.rate_lec(Dmitriev, 'Python', 3)
Petrov.rate_lec(Dmitriev, 'Python', 2)
Dyatlov.rate_lec(Dmitriev, 'Math', 1)
Petrov.rate_lec(Dmitriev, 'Math', 4)

# print(Dymov.name, Dymov.surname, Dymov.grades)
# print(Dymov)
# print(Dyatlov)
# print(Petrov)
# print(Dyatlov > Petrov)
# print(Dmitriev)
# print(Dymov > Dmitriev)

print(rate_st_avg_for_all_courses([Dyatlov,Petrov],'Python'))
print(rate_lec_avg_for_all_courses([Dymov,Dmitriev],'Python'))
