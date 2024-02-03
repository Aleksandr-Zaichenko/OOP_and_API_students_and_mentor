class Student:
    
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

# Метод для выставления оценок лекторам           

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

# Получение средней оценки за домашние задания    

    def __average_grade(self):
        grades_list = []
        for course, grades in self.grades.items():
            for item in grades:
                grades_list.append(item)
        average = sum(grades_list) / len(grades_list)
        return average        

# Перегрузка вывода информации у магического метода __str__            

    def __str__(self):
        nm = f"Имя: {self.name}"
        snm = f"Фамилия: {self.surname}"
        av_gr = f"Средняя оценка за домашние задания: {self.__average_grade()}"
        co_in_pr = f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}"
        fin_co = f"Завершенные курсы: {', '.join(self.finished_courses)}"
        return f"{nm}\n{snm}\n{av_gr}\n{co_in_pr}\n{fin_co}"

# Реализация возможности сравнивать между собой студентов по средней оценке за домашние задания    

    def __eq__(self, other):
        return self.__average_grade() == other.__average_grade()
    
    def __lt__(self, other):
        return self.__average_grade() < other.__average_grade()
    
    def __le__(self, other):
        return self.__average_grade() <= other.__average_grade()
     

class Mentor:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
            

class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

# Получение средней оценки за лекции    

    def __average_grade(self):
        grades_list = []
        for course, grades in self.grades.items():
            for item in grades:
                grades_list.append(item)
        average = sum(grades_list) / len(grades_list)
        return average

# Перегрузка вывода информации у магического метода __str__    

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__average_grade()}"

# Реализация возможности сравнивать между собой лекторов по средней оценке за лекции    

    def __eq__(self, other):
        return self.__average_grade() == other.__average_grade()
    
    def __lt__(self, other):
        return self.__average_grade() < other.__average_grade()
    
    def __le__(self, other):
        return self.__average_grade() <= other.__average_grade()    


class Reviewer(Mentor):

# Метод для выставления оценок студентам    

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Перегрузка вывода информации у магического метода __str__    

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"        


# Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса

def av_grade_all_std(stud_list, course):
    grades_list = []
    for student in stud_list:                
        if student.grades.get(course) == None:
            continue
        for item in student.grades.get(course):
            grades_list.append(item)
    average = sum(grades_list) / len(grades_list)
    print(average)


# Подсчет средней оценки за лекции всех лекторов в рамках курса

def av_grade_all_lct(lct_list, course):
    grades_list = []
    for lecturer in lct_list:
        if lecturer.grades.get(course) == None:
            continue
        for item in lecturer.grades.get(course):
            grades_list.append(item)
    average = sum(grades_list) / len(grades_list)
    print(average)    


student_1 = Student('Vasya', 'Pupkin', 'Male')
student_2 = Student('Maria', 'Ivanova', 'Female')
lecturer_1 = Lecturer('Ivan', 'Ivanov')
lecturer_2 = Lecturer('Stepan', 'Stepanov')
reviewer_1 = Reviewer('Jeff', 'Bezos')
reviewer_2 = Reviewer('Elon', 'Mask')
student_1.finished_courses += ['Введение в программирование']
student_2.finished_courses += ['Введение в программирование']
student_1.courses_in_progress += ['Python', 'Git']
student_2.courses_in_progress += ['Python', 'Git']
lecturer_1.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']
reviewer_1.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git'] 


reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 7)


student_1.rate_lecturer(lecturer_1, 'Python', 8)
student_2.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_2, 'Git', 9)
student_2.rate_lecturer(lecturer_2, 'Git', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_2.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Git', 7)
student_2.rate_lecturer(lecturer_2, 'Git', 8)

 
students_list = [student_1, student_2]
lecturers_list = [lecturer_1, lecturer_2]


print(student_1)
print(student_1 < student_2)
print(lecturer_1)
print(lecturer_1 > lecturer_2)
print(reviewer_1) 
av_grade_all_std(students_list, 'Python')
av_grade_all_lct(lecturers_list, 'Python')

