# Kyla Purcell

# A01088856


class Student:
    """ This is the student class module, it includes all methods concerning the creation, format, and rules about
     the student class object. """

    def __init__(self, first_name: str, last_name: str, student_number: str, status: bool, grades=None):
        """Create a student object.

        Every student must have a first name, last name, student number and a status.
        Grades can be a full or empty list"""
        self.__grades = grades
        self.__status = status
        if ' ' in first_name or ' ' in last_name:
            raise ValueError('A student must have a complete first name, last name')
        elif '' == first_name or '' == last_name:
            raise ValueError('A student must have a complete first name, last name')
        else:
            self.__first_name = first_name
            self.__last_name = last_name
        if 'A' == student_number[0] and len(student_number) == 9 and ' ' not in student_number:
            self.__student_number = student_number
        else:
            raise ValueError('A student number must be in the correct format (A########)')

    def get_first_name(self)->str:
        """ Return the first name of a student"""
        return self.__first_name

    def get_last_name(self)->str:
        """ Return the last name of a student"""
        return self.__last_name

    def get_student_number(self)->str:
        """ Return the student number of a student"""
        return self.__student_number

    def get_status(self)->bool:
        """ Return the standing status of a student (good or bad standing)"""
        return self.__status

    def get_grades_list(self)-> list:
        """ Return the grades of a student as a list"""
        return self.__grades

    def print_student_info(self)-> None:
        """ Print the student's info in a pleasing way"""
        grade_string_list = []
        for i in self.__grades:
            grade_string_list.append(str(i))
        grade_string = ' '.join(grade_string_list)
        print('Name:', self.__first_name, self.__last_name, 'Student Number:', self.__student_number,
              'Status:', str(self.__status), 'Grades:', grade_string)

    def calculate_student_gpa(self)->float:
        """ Calculate a student's gpa"""
        number_of_courses = len(self.__grades)
        grades_sum = 0
        for i in self.__grades:
            grades_sum += i
        try:
            gpa = grades_sum/number_of_courses
        except ZeroDivisionError:
            print(self.__first_name, self.__last_name, 'has no final grades yet so their gpa is currently -1')
            gpa = -1
        return gpa

    def set_student_grades(self, grades: list)-> None:
        """ Set a student's grades.

        PARAM: grades, a list of integers
        PRE-CONDITION: grades must be a list of integers between 0 and 100
        POST-CONDITION: replaces a students current grades list with the parameter grades
        RETURN: None
        """
        for i in grades:
            if i < 0 or i > 100:
                raise ValueError('Grades must be between 0 and 100 in a percent form ')
        self.__grades = grades

    def set_student_first_name(self, name: str)->None:
        """ Set a student's first name.

        PARAM: name, a string
        PRE-CONDITION: name must be a non empty string with no whitespace
        POST-CONDITION: replaces a students current first name with the parameter name
        RETURN: None
        """
        self.__first_name = name

    def set_student_last_name(self, name: str)-> None:
        """ Set a student's last name.

        PARAM: name, a string
        PRE-CONDITION: name must be a non empty string with no whitespace
        POST-CONDITION: replaces a students current last name with the parameter name
        RETURN: None
        """
        self.__last_name = name

    def set_student_status(self, status: bool)-> None:
        """ Set a student's status.

        PARAM: status, a bool
        PRE-CONDITION: name must be a bool
        POST-CONDITION: replaces a students current status with the parameter status
        RETURN: None
        """

        self.__status = status

    def __repr__(self) -> str:
        """
        Return a string representation of a student object.

        """
        grade_string_list = []
        for i in self.__grades:
            grade_string_list.append(str(i))
        grade_string = ' '.join(grade_string_list)
        representation = ' '.join([self.__first_name, self.__last_name,
                                   self.__student_number, str(self.__status), grade_string])
        return representation

    def format_first_name(self)->None:
        """
        Format a student's first name (title case and strip leading/trailing whitespace).

        """
        self.__first_name = self.__first_name.title().strip()

    def format_last_name(self)->None:
        """
        Format a student's last name (title case and strip leading/trailing whitespace).

        """
        self.__last_name = self.__last_name.title().strip()




