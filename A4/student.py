
class Student:

    counter = 0

    def __init__(self, first_name: str, last_name: str, student_number: str, status: bool, grades: list):
        self.__grades = grades
        if first_name is None or last_name is None or student_number is None or status is None:
            raise ValueError('A student must have a first name, last name, student number')
        elif '' == first_name or '' == last_name or '' == student_number:
            raise ValueError('A student must have a complete first name, last name and student number')
        else:
            self.__first_name = first_name
            self.__last_name = last_name
            self.__student_number = student_number
            self.__status = status
        self.id = Student.counter
        Student.counter += 1

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_student_number(self):
        return self.__student_number

    def get_status(self):
        return self.__status

    def get_grades_list(self):
        return self.__grades

    def print_student_info(self):
        grade_string_list = []
        for i in self.__grades:
            grade_string_list.append(str(i))
        grade_string = ' '.join(grade_string_list)
        print(self.__first_name, self.__last_name, self.__student_number, str(self.__status), grade_string)

    def calculate_student_gpa(self):
        number_of_courses = len(self.__grades)
        grades_sum = 0
        for i in self.__grades:
            grades_sum += i
        try:
            gpa = grades_sum/number_of_courses
        except ZeroDivisionError:
            print(self.__first_name, self.__last_name, 'has no final grades yet so their gpa is currently 0')
            gpa = 0
        return gpa

    def set_student_grades(self, grades: list):
        for i in grades:
            if i < 0 or i > 100:
                raise ValueError('Grades must be between 0 and 100 in a percent form ')
        self.__grades = grades

    def set_student_first_name(self, name: str):
        self.__first_name = name

    def set_student_last_name(self, name: str):
        self.__last_name = name

    def set_student_status(self, status: bool):
        self.__status = status





