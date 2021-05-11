class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}
        self.av_grade_stud = 0
        self.av_grade = 0
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
    def rate_hw_stud(self, teacher, course, grade):
        if isinstance(teacher, Lecturer) and course in self.courses_attached and course in teacher.courses_in_progress:
            if course in teacher.grades:
                teacher.grades[course] += [grade]
            else:
                teacher.grades[course] = [grade]
        else:
            return 'Ошибка'
    def average_rating(self):
        rating_list = []
        for lang, grade in self.grades.items():
            for val in grade:
                rating_list.append(val)
        self.av_grade = sum(rating_list) / len(rating_list)
    def __str__(self):
        self.average_rating()
        stud_list = []
        for lang, grade in self.grades.items():
            for val in grade:
                stud_list.append(val)
        av_grade_stud = sum(stud_list) / len(stud_list)
        return 'Имя: '+self.name+'\nФамилия: '+self.surname+'\nСредняя оценка за домашние задания: '+str('%.2f' % av_grade_stud)+'\nКурсы в процессе обучения: '+str(', '.join(self.courses_in_progress))+'\nЗавершенные курсы: '+'Введение в программирование'
    def out_avgr(self):
        print(self.av_grade)
    def __lt__(self, other):
        print('Сравниваем среднюю оценку студента и лектора')
        return self.av_grade < other.av_grade

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades = {}
        self.av_grade_lect = 0
        self.av_grade = 0
    def average_rating(self):
        rating_list = []
        for lang, grade in self.grades.items():
            for val in grade:
                rating_list.append(val)
        self.av_grade = sum(rating_list) / len(rating_list)
    def __str__(self):
        self.average_rating()
        lect_list = []
        for lang, grade in self.grades.items():
            for val in grade:
                lect_list.append(val)
        av_grade_lect = sum(lect_list) / len(lect_list)
        return 'Имя: '+self.name+'\nФамилия: '+self.surname+'\nСредняя оценка за лекции: '+str('%.2f' % av_grade_lect)
    def __lt__(self, other):
        print('Сравниваем среднюю оценку лектора и студента')
        return self.av_grade < other.av_grade

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def rate_hw(self, student, reviewe,  course, grade):
        if isinstance(student, Student) and isinstance(reviewe, Reviewer) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return 'Имя: '+self.name+'\nФамилия: '+self.surname

def aver_stud_or_lect(dict1, dict2):
    all_dict = {}
    our_list = []
    all_dict = dict1.copy()
    for lang, grade in dict1.items():
        for lang1, grade1 in dict2.items():
            if lang != lang1:
                all_dict.setdefault(lang1, grade1)
            else:
                for val in grade1:
                    grade.append(val)
    course = input('Введите название курса: ')
    for lang, grade in all_dict.items():
        if lang == course:
            for val in grade:
                our_list.append(val)
    av_grade_stud = sum(our_list) / len(our_list)
    print(f" '\nСредняя оценка курса '{course}' : {av_grade_stud}")

one_student = Student('Roy', 'Eman', 'your_gender')
one_student.courses_in_progress += ['Python', 'Git', 'Java']
two_student = Student('Ben', 'Afleck', 'your_gender')
two_student.courses_in_progress += ['Python', 'Git', 'Java']

one_reviewer = Reviewer('Kurt', 'Russell')
two_reviewer = Reviewer('Milla', 'Jovovich')

one_teacher = Lecturer('Jeckie', 'Chan')
one_teacher.courses_in_progress += ['Python', 'Git']
two_teacher = Lecturer('Jet', 'Li')
two_teacher.courses_in_progress += ['Java', 'Git']

one_reviewer.courses_attached += ['Python', 'Git']
one_reviewer.rate_hw(one_student, one_reviewer, 'Python', 10)
one_reviewer.rate_hw(one_student, one_reviewer, 'Python', 8)
one_reviewer.rate_hw(one_student, one_reviewer, 'Git', 6)
one_reviewer.rate_hw(one_student, one_reviewer, 'Git', 9)
one_reviewer.rate_hw(one_student, one_reviewer, 'Java', 8)
one_reviewer.rate_hw(one_student, one_reviewer, 'Java', 9)
two_reviewer.courses_attached += ['Java', 'Python', 'Git']
two_reviewer.rate_hw(two_student, two_reviewer, 'Python', 6)
two_reviewer.rate_hw(two_student, two_reviewer, 'Java', 4)
two_reviewer.rate_hw(two_student, two_reviewer, 'Git', 6)
two_reviewer.rate_hw(two_student, two_reviewer, 'Python', 3)
two_reviewer.rate_hw(two_student, two_reviewer, 'Java', 5)
two_reviewer.rate_hw(two_student, two_reviewer, 'Git', 2)

one_student.courses_attached += ['Python', 'Git']
one_student.rate_hw_stud(one_teacher, 'Python', 10)
one_student.rate_hw_stud(one_teacher, 'Java', 8)
one_student.rate_hw_stud(one_teacher, 'Git', 10)
one_student.rate_hw_stud(one_teacher, 'Python', 1)
one_student.rate_hw_stud(one_teacher, 'Java', 2)
one_student.rate_hw_stud(one_teacher, 'Git', 3)
two_student.courses_attached += ['Java', 'Git']
two_student.rate_hw_stud(two_teacher, 'Java', 9)
two_student.rate_hw_stud(two_teacher, 'Python', 5)
two_student.rate_hw_stud(two_teacher, 'Git', 8)
two_student.rate_hw_stud(two_teacher, 'Java', 4)
two_student.rate_hw_stud(two_teacher, 'Python', 5)
two_student.rate_hw_stud(two_teacher, 'Git', 6)

print()
print('Reviewer')
print(one_reviewer)
print(two_reviewer)
print()
print('Lecturer')
print(one_teacher)
print(two_teacher)
print()
print('Student')
print(one_student)
print(two_student)
print()
# print('one_student.grades', one_student.grades)
# print('two_student.grades', two_student.grades)
# print('one_teacher.grades', one_teacher.grades)
# print('two_teacher.grades', two_teacher.grades)
print(one_student < one_teacher)
print()
aver_stud_or_lect(one_student.grades, two_student.grades)

