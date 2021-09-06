#
# Задание № 3. Полиморфизм и магические методы
#
# Перегрузите магический метод __str__ у всех классов.
'''
У проверяющих он должен выводить информацию в следующем виде:
print(some_reviewer)
Имя: Some
Фамилия: Buddy
'''
from functools import reduce

'''
У лекторов:
print(some_lecturer)
Имя: Some
Фамилия: Buddy
Средняя оценка за лекции: 9.9
'''

'''
А у студентов так:
print(some_student)
Имя: Ruoy
Фамилия: Eman
Средняя оценка за домашние задания: 9.9
Курсы в процессе изучения: Python, Git
Завершенные курсы: Введение в программирование
'''
# Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов
# по средней оценке за лекции и студентов по средней оценке за домашние задания.


# Задание № 4. Полевые испытания
#
# Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:
#
# для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
# (в качестве аргументов принимаем список студентов и название курса);
# для подсчета средней оценки за лекции всех лекторов в рамках курса
# (в качестве аргумента принимаем список лекторов и название курса).
#
#



from random import randint

from termcolor import cprint







class Student:
    def __init__(self, name, surname, gender, *course):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.person = {}
        self.course = course
        self.jik = {}



    def __str__(self):
        return f'Имя - {self.name}, Фамилия - {self.surname}, {self.finished_courses}, "\n"' \
               f'Pytson - {self.grades["Python"]}, "\n" Git - {self.grades["Git"]}"\n"' \
               f' средний бал {self.person[self.name]}'

    def rate_hw(self, lekt, course, grade):
        if isinstance(lekt, Lecturer) and course in lecturer.courses_attached \
                and course in lekt.courses_in_progress:
            if course in lekt.lector_grades:
                lekt.lector_grades[course] += [grade]

            else:
                lekt.lector_grades[course] = [grade]

        else:
            return 'Ошибка'
        return f"{lekt.lector_grades[course]}"

    def peson_grade(self, grade,):
        if self.course in self.grades:
            self.person[self.name] += grade
        else:
                self.pers = self.grades['Python'] + self.grades['Git']
                self.jik[self.name] = float(sum(self.grades['Python'] + self.grades['Git']) / len(self.pers))
                self.person[self.name] = self.jik

    # def peson_grade(self, grade):
    #     if self.course in self.grades:
    #         self.person[self.name] += [self.grades]
    #     else:
    #         self.person[self.name] = [self.grades]
    #         return grade
        # else:
        #     return 'Ошибка'
        # return f"{student.grades[course]}"
        # self.person[self.name] += [self.grades]

    def student_act(self):

            dese = randint(1, 6)
            if dese == 1:
                students.rate_hw(lekt, 'Python', 10) and \
                students.rate_hw(lekt, 'Git', 8)
                lekt.peson_grade(lekt, 'Elizar')
                lekt.peson_grade(lekt, 'Some')


            elif dese == 4:
                students.rate_hw(lekt, 'Python', 9) and \
                students.rate_hw(lekt, 'Git', 10)
                lekt.peson_grade(lekt, 'Elizar')
                lekt.peson_grade(lekt, 'Some')



            elif dese == 5:
                students.rate_hw(lekt, 'Python', 8) and \
                students.rate_hw(lekt, 'Git', 9)
                lekt.peson_grade(lekt, 'Elizar')
                lekt.peson_grade(lekt, 'Some')


            else:
                students.rate_hw(lekt, 'Python', 10) and \
                students.rate_hw(lekt, 'Git', 10)




class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


    def __str__(self):
        pass




class Lecturer(Mentor):
    def __init__(self, name, surname, *course):
        super().__init__(name=name, surname=surname)
        self.name = name
        self.courses_attached = []
        self.lector_grades = {}
        self.courses_in_progress = []
        self.person = {}
        self.course = course
        self.jik = {}



    def __str__(self):
        return f'Имя - {self.name}, Фамилия - {self.surname}, "\n"' \
               f'Pytson - {self.lector_grades["Python"]}, "\n" Git - {self.lector_grades["Git"]}"\n"' \
               f'средний бал за лекции {self.person[self.name]}'

    def reed_lection(self, cours,):
        print(f'ghjxbnfk ntrwb - {cours}')

    def peson_grade(self, grade, name):
        if self.course in self.lector_grades:
            self.person[name] += grade
        else:
                self.pers = self.lector_grades['Python'] + self.lector_grades['Git']
                self.jik[name] = float(sum(self.lector_grades['Python'] + self.lector_grades['Git']) / len(self.pers))
                self.person[name] = self.jik

        # return grade
            # return self.person
            # lecturer.person.setdefault('Some')
            # lecturer.person.setdefault('Elizar')
            # if lecturer.person['Elizar'] < lecturer.person['Elizar']:
            #     += 1
            #     print()


            # print('лучший преподователь Some')

    def __lt__(self, ):
        return self.person < other.person

    def ickvel(self):
        lecturer.person.setdefault('Some'), lecturer.person.setdefault('Elizar')
        if lecturer.person['Elizar'] > lecturer.person['Some']:
            print('лучший преподователь Some')
        else:
            print('лучший преподователь Elizar')


    def act(self):
        dises = randint(1, 2)
        if dises == 1:
            self.reed_lection('Paython') and self.reed_lection('Git')
        else:
            self.reed_lection('Paython') and self.reed_lection('Git')

# TODO реализовать случайные оценки

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name=name, surname=surname)
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        return f"{student.grades[course]}"

    def rvw_act(self):

        dese = randint(1, 6)
        if dese == 1:
            reviewer.rate_hw(students, 'Python', 10) and \
            reviewer.rate_hw(students, 'Git', 8)
            students.peson_grade(students)
        elif dese == 4:
            reviewer.rate_hw(students, 'Python', 9) and \
            reviewer.rate_hw(students, 'Git', 10)
            students.peson_grade(students)

        elif dese == 5:
            reviewer.rate_hw(students, 'Python', 8) and \
            reviewer.rate_hw(students, 'Git', 9)
            students.peson_grade(students)

        else:
            reviewer.rate_hw(students, 'Python', 10) and \
            reviewer.rate_hw(students, 'Git', 10)
            students.peson_grade(students)


# реализовать случайные оценки

student = [Student(name="Александр", surname="Фролов", gender='Mail'),
            Student(name="Валерия", surname="Христофорова", gender='Famail',),
            Student(name="Дмитрий", surname="Михеев", gender='Mail',)
            ]

for students in student:
    students.courses_in_progress += ['Python']
    students.courses_in_progress += ['Git']
    students.finished_courses = ['введение в програмирование']


lectur = [Lecturer(name='Some', surname='Odoc'),
            Lecturer(name='Elizar', surname='Fishman')]



elik = Lecturer(name='Elizar', surname='Fishman')
som = Lecturer(name='Elizar', surname='Fishman')

som.courses_attached += ['Python']
som.courses_attached += ['Git']
som.courses_in_progress += ['Python']
som.courses_in_progress += ['Git']

elik.courses_attached += ['Python']
elik.courses_attached += ['Git']
elik.courses_in_progress += ['Python']
elik.courses_in_progress += ['Git']

lektur = [elik, som

]

for lekt in lektur:



    print()
for lecturer in lectur:
    lecturer.courses_attached += ['Python']
    lecturer.courses_attached += ['Git']
    lecturer.courses_in_progress += ['Python']
    lecturer.courses_in_progress += ['Git']



reviewer = Reviewer('Some', 'Buddy')
reviewer.courses_attached += ['Python']
reviewer.courses_attached += ['Git']



for week in range(1, 62, 5):
    cprint(f'========================== {week} ===========================', 'cyan')
    for students in student:
        reviewer.rvw_act()
        # print(students.person)



    cprint(f'========================== игтоги {week} недели ===========================', 'cyan')
    cprint(f'========================== студенты ===========================', 'cyan')

    for students in student:
        cprint(f'{students}', color="yellow")



        # print(students.person)
    cprint(f'========================== преподы ===========================', 'cyan')
    for lekt in lektur:
        students.student_act()
        cprint(lekt.jik, color='blue')
        lekt.peson_grade(lekt, 'Elizar')
        lekt.peson_grade(lekt, 'Some')
        print(lekt.jik['Elizar'])
        print(lekt.jik['Some'])
        print(lekt.jik['Elizar'] == lekt.jik['Some'])
        break



        # lecturer.person.setdefault(lecturer.name), lecturer.person.setdefault(lecturer.name)
        # print(lecturer.person['Elizar'])

















