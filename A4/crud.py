# Kyla Purcell

# A01088856

from A4 import student


def add_grades()->list:
    """
    Create list of inputted grades.

    POST-CONDITION: If valid grade, adds the inputted grades to a list and
    returns it or returns empty list if option selected
    RETURN: list of grades as a list of integers or an empty list.
    """
    grade_list = []
    while True:
        try:
            grade = int(input('Input a grade to add to the students grade list and when done adding type -2 or '
                              'if student has no grades yet type -1: ').strip())
            if grade == -1:
                return []
            elif grade == -2:
                    break
            elif grade > 100 or grade < 0:
                print('That grade is not valid')
            else:
                grade_list.append(grade)
        except ValueError:
            print('Grade must be an integer')
    return grade_list


def make_boolean(string_one: str) -> bool:
    """
     Convert a string into a boolean.

     PARAM: string_one, a string
     PRE-CONDITION: string_one must be a string
     POST-CONDITION: If string_one is True returns True else returns False
     RETURN: True or False as a Boolean

     >>> make_boolean('true')
     True
     >>> make_boolean('false')
     False
     """
    string_titled = string_one.title()
    if string_titled == 'True':
        return True
    else:
        return False


def add_student():
    """
     Create a student object.

     POST-CONDITION: If user input is valid returns a student object, otherwise returns None
     RETURN: a student as a Student object or None.
     """
    student1 = None
    try:
        first_name1 = input("What is the student's first name ")
        last_name1 = input("What is the student's last name ")
        student_number1 = input("What is the student's # ")
        status1 = make_boolean(input('Is this student in good standing, (True or False) '))
        grades = add_grades()
        student1 = student.Student(first_name1, last_name1, student_number1, status1, grades)
        student1.format_first_name()
        student1.format_last_name()
    except ValueError:
        print('A student must have correct a student number, a first/last name and a status to be added ')
    return student1


def file_write(student1, filename1: str)-> bool:
    """
     Write a student to a text file.

     PARAM: filename1, a string
     PARAM: student1 a student object
     PRE-CONDITION: filename1 must be a string
     PRE-CONDITION: student1 must be a student object or None
     POST-CONDITION: If student1 is student object writes their information to a text file as a string and returns True
     else returns False
     RETURN: True or False as a bool.

     >>> file_write(None, 'testfile2.txt')
     False
     """
    if student1 is None:
        return False
    else:
        filename = filename1
        with open(filename, 'a') as file_object:
            line = student1.__repr__()
            file_object.write('\n' + line)
        return True


def file_read(filename: str)-> list:
    """
     Read a student text file.

     PARAM: filename, a string
     PRE-CONDITION: filename must be a string ending in .txt
     POST-CONDITION: Converts students in the text file to student objects and adds them to a list
     RETURN: list of students as a list of student objects.
     """
    object_list = []
    with open(filename) as file_object:
        lines = file_object.readlines()
        student_list = [line.split() for line in lines]
        for i in student_list:
            if not i:
                continue
            else:
                object_list.append(student.Student(i[0], i[1], i[2], make_boolean(i[3]), list(map(int, i[4:]))))
        return object_list


def update_file(object_list: list, filename: str)-> None:
    """
     Update a student text file.

     PARAM: object_list, a list
     PARAM: filename, a string
     PRE-CONDITION: filename must be a string ending in .txt
     PRE-CONDITION: object_list must be a list of student objects
     POST-CONDITION: clears current information in the students text file and replaces it with
     the contents of object_list as a string
     RETURN: None
     """
    with open(filename, 'w') as file_object:
        file_object.write('')
    for student1 in object_list:
        file_write(student1, filename)


def file_delete_student(student_number: str, file_name: str) -> bool:
    """
    Delete a student from a text file.

    PARAM: student_number , a string
    PARAM: file_name, a string
    PRE-CONDITION: file_name must be a string ending in .txt
    PRE-CONDITION: student_number must be a string
    POST-CONDITION: if student_number matches the student number of a student in the file, deletes that
    student's information from the text file or prints a helpful message
    RETURN: True or False as a bool.

    >>> file_delete_student('A00000000','testfile14.txt')
    We could not remove that student because they do not exist in the database
    False
    """
    students_list = file_read(file_name)
    while True:
        for student1 in students_list:
            if student1.get_student_number() == student_number:
                print('We successfully deleted the student')
                students_list.remove(student1)
                update_file(students_list, file_name)
                return True
        print('We could not remove that student because they do not exist in the database')
        return False


def calculate_class_gpa(file_name: str)->float:
    """
    Calculate the class average.

    PARAM: file_name, a string
    PRE-CONDITION: file_name must be a string
    POST-CONDITION: calculates the gpa of students with final grades and then calculates the rounded average
    RETURN: the class grade point average as a float
    """
    print('Students with no final grades yet (GPA = -1) will not be counted in this calculation')
    student_list = file_read(file_name)
    grades_sum = 0
    new_list = []
    average = 0
    for student1 in student_list:
        if student1.calculate_student_gpa() == -1:
            continue
        new_list.append(student1)
    for student1 in new_list:
        grades_sum += student1.calculate_student_gpa()
    try:
        average = round(grades_sum/len(new_list), 2)
    except ZeroDivisionError:
        print('The students in the database do not have final grades yet')
    return average


def update_grades(student_number: str, file_name: str) -> bool:
    """
    Add a grade to a student's record.

    PARAM: student_number, a string
    PARAM: grade_to_add, an integer
    PARAM: file_name, a string
    PRE-CONDITION: student_number must be a string
    PRE-CONDITION: grade_to_add must be an integer in range 0-100
    PRE-CONDITION: file_name must be a string ending in .txt
    POST-CONDITION: If valid adds a grade to the grade list of a student and updates the text file
    RETURN: True or False as a bool

    >>> update_grades('A00000000','testfile14.txt')
    We could not find that student in our file or grade could not be added
    False
    """
    student_list = file_read(file_name)
    while True:
        for student1 in student_list:
            if student_number == student1.get_student_number():
                    grade_to_add = int(input('Please input a grade you would like to add (an integer from 0-100)'))
                    new_list = [grades for grades in student1.get_grades_list()]
                    new_list.append(grade_to_add)
                    try:
                        student1.set_student_grades(new_list)
                        update_file(student_list, file_name)
                        return True
                    except ValueError:
                        print('Grades cannot include numbers below zero or above 100')
        print('We could not find that student in our file or grade could not be added')
        return False


def print_class_list(file_name: str)-> None:
    """
    Print the information of all students in a text file.

    PARAM: file_name, a string
    PRE-CONDITION: file_name must be a string ending in .txt
    POST-CONDITION: Prints the information of students in the text file and prints how many students are currently
    enrolled in the class
    RETURN: None
    """
    student_list = file_read(file_name)
    for student1 in student_list:
        student1.print_student_info()
    print('There are', str(len(student_list)), 'students currently enrolled in this school')


def print_menu_options()-> int:
    """
    Print the menu options for the user.

    POST-CONDITION: Prints the menu options for the user and returns their selected option.
    RETURN: An option as an integer
    """
    print(' 1.Add Student', '\n', '2.Delete Student', '\n', '3.Calculate Class Average', '\n', '4.Print Class List',
          '\n', '5.Add Grade To Student Record', '\n', '6.Quit')
    try:
        option = int(input('Please select a menu option (1-6) '))
    except ValueError:
        print('You must select one of the given options')
        return print_menu_options()
    if 1 <= option <= 6:
        return option
    else:
        print('You must select one of the given options')
        return print_menu_options()


def crud_loop():
    """
    Manage a student record.
    """
    while True:
        option = print_menu_options()
        if option == 6:
            break
        elif option == 5:
            update_grades(input('Please input a student number in the format A###### '), 'students.txt')
        elif option == 4:
            print_class_list('students.txt')
        elif option == 3:
            print('The class average of this class is', str(calculate_class_gpa('students.txt')))
        elif option == 2:
            file_delete_student(input('Please input a student number in the format A###### to delete'), 'students.txt')
        elif option == 1:
            file_write(add_student(), 'students.txt')


def main():
    """
    Drive the program
    """
    crud_loop()
    import doctest
    doctest.testmod()


if __name__ == '__main__':
    main()










