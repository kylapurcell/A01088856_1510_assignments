from A4 import student
import math


def add_grades():
    grade_list = []
    while True:
        try:
            grade = int(input('Input a grade to add to the students grade list, If no grades yet type 1 '
                           'when done adding type 2 ').strip())
            if grade == 1:
                return ''
            elif grade == 2:
                    break
            grade_list.append(grade)
        except TypeError:
            print('Grade must be an integer')
    return grade_list


def status_input():
    status = False
    status1 = input('Is this student in good standing, (True or False)').title().strip()
    if status1 == 'True':
        status = True
    return status


def add_student():
    student1 = None
    try:
        first_name1 = input("What is the student's first name").title()
        last_name1 = input("What is the student's last name").title()
        student_number1 = input("What is the student's #")
        status1 = status_input()
        grades = add_grades()
        student1 = student.Student(first_name1, last_name1, student_number1, status1, grades)
    except ValueError:
        print('A student must have correct a student number, a first/last name and a status to be added ')
    except TypeError:
        print('A new students with no grades yet was created')
    return student1


def file_write(student1):
    if student1 is None:
        return False
    else:
        grade_string_list = []
        for i in student1.get_grades_list():
            grade_string_list.append(str(i))
        grade_string = ' '.join(grade_string_list)
        filename = 'students.txt'
        with open(filename, 'a') as file_object:
            line = ' '.join([student1.get_first_name(), student1.get_last_name(),
                         student1.get_student_number(), str(student1.get_status()), grade_string])
        file_object.write('\n' + line)
        return True


def make_boolean(string):
    if string == 'True':
        return True
    else:
        return False


def file_read():
    object_list = []
    filename = 'students.txt'
    with open(filename) as file_object:
        lines = file_object.readlines()
        student_list = [line.split() for line in lines]
        for i in student_list:
            if i == []:
                continue
            else:
                object_list.append(student.Student(i[0], i[1], i[2], make_boolean(i[3]), list(map(int, i[4:]))))
        return object_list


def update_file(object_list: list):
    filename = 'students.txt'
    with open(filename, 'w') as file_object:
        file_object.write('')
    for student1 in object_list:
        file_write(student1)


def file_delete_student(student_number: str):
    students_list = file_read()
    while True:
        for student1 in students_list:
            if student1.get_student_number() == student_number:
                print('We successfully deleted the student')
                students_list.remove(student1)
                update_file(students_list)
                return True
        print('We could not remove that student because they do not exist in the database')
        return False


def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def calculate_class_gpa():
    print('Students with no final grades yet (GPA = 0) will not be counted in this calculation')
    student_list = file_read()
    grades_sum = 0
    new_list = []
    for student1 in student_list:
        if student1.calculate_student_gpa() == 0:
            continue
        new_list.append(student1)
    for student1 in new_list:
        grades_sum += student1.calculate_student_gpa()
    return truncate(grades_sum/len(new_list), 2)


def update_grades(student_number: str, grade_to_add: int):
    student_list = file_read()
    while True:
        for student1 in student_list:
            if student_number == student1.get_student_number():
                    new_list = [grades for grades in student1.get_grades_list()]
                    new_list.append(grade_to_add)
                    try:
                        student1.set_student_grades(new_list)
                        update_file(student_list)
                        return True
                    except ValueError:
                        print('Grades cannot include numbers below zero or above 100')
        print('We could not find that student in our file or grade could not be added')
        return False


def print_class_list():
    student_list = file_read()
    for student1 in student_list:
        student1.print_student_info()
    print('There are', str(len(student_list)), 'students currently enrolled in this school')


def print_menu_options():
    print(' 1.Add Student', '\n', '2.Delete Student', '\n', '3.Calculate Class Average', '\n', '4.Print Class List',
          '\n', '5.Add Grade To Student Record', '\n', '6.Quit')
    option = int(input('Please select a menu option (1-6) '))
    return option


def crud_loop():
    while True:
        option = print_menu_options()
        if option == 6:
            break
        elif option == 5:
            student_number = input('Please input a student number in the format A###### ')
            grade = int(input('Please input a grade you would like to add (an integer from 0-100)'))
            update_grades(student_number, grade)
        elif option == 4:
            print_class_list()
        elif option == 3:
            print(calculate_class_gpa())
        elif option == 2:
            student_number = input('Please input a student number in the format A###### to delete')
            file_delete_student(student_number)
        elif option == 1:
            file_write(add_student())

crud_loop()











