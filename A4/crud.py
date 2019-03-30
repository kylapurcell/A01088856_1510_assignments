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


def file_write(student1):
    grade_string = ''
    for i in student1.grades:
        grade_string = grade_string + ' ' + str(i)
    filename = 'students.txt'
    with open(filename, 'a') as file_object:
        line = ' '.join([student1.first_name, student1.last_name,
                         student1.student_number, str(student1.status), grade_string])
        file_object.write('\n' + line)


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
            if i is []:
                continue
            else:
                object_list.append(student.Student(i[0], i[1], i[2], make_boolean(i[3]), list(map(int, i[4:]))))
        return object_list

file_write(add_student())

list1 = file_read()

for i in list1:
    i.print_student_info()
    print(i.counter)

