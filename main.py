class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.courses_attached = []
        self.grades = {}

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


class Mentor:
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

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.courses_in_progress = []
        self.grades = {}

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

best_student = Student('Roy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

reviewer = Reviewer('Nina', 'Stepanova')
print(reviewer.name)
print(reviewer.surname)

reviewer.courses_attached += ['Python']
reviewer.rate_hw(best_student, reviewer, 'Python', 10)
reviewer.rate_hw(best_student, reviewer, 'Python', 10)
reviewer.rate_hw(best_student, reviewer, 'Java', 10)
print(best_student.grades)

teacher = Lecturer('Edward', 'Stepanov')
print(teacher.name)
print(teacher.surname)

current_teacher = Lecturer('Roy', 'Eman')
current_teacher.courses_in_progress += ['Java']

best_student.courses_attached += ['Java']
best_student.rate_hw_stud(current_teacher, 'Python', 10)
best_student.rate_hw_stud(current_teacher, 'Python', 10)
best_student.rate_hw_stud(current_teacher, 'Java', 10)
print(current_teacher.grades)
# lector.courses_attached += ['Python']
# lector.rate_hw(best_student, lector, 'Python', 10)
# lector.rate_hw(best_student, lector, 'Python', 10)
# lector.rate_hw(best_student, lector, 'Python', 10)
# print(best_student.grades)
