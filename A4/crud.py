from A4 import student


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
        first_name1 = input("What is the student's first name")
        last_name1 = input("What is the student's last name")
        student_number1 = input("What is the student's #")
        status1 = status_input()
        grades = add_grades()
        student1 = student.Student(first_name1, last_name1, student_number1, status1, grades)
    except ValueError:
        print('A student must have a student number, a first/last name and a status to be added ')
        return add_student()
    except TypeError:
        print('A new students with no grades yet was created')
    return student1

student3 = add_student()

student3.print_student_info()
