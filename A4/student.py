
class Student:

    counter = 0

    def __init__(self, first_name: str, last_name: str, student_number: str, status: bool, grades: list):
        self.grades = grades
        if first_name is None or last_name is None or student_number is None or status is None:
            raise ValueError('A student must have a first name, last name, student number')
        elif '' == first_name or '' == last_name or '' == student_number:
            raise ValueError('A student must have a complete first name, last name and student number')
        else:
            self.first_name = first_name
            self.last_name = last_name
            self.student_number = student_number
            self.status = status
        self.id = Student.counter
        Student.counter += 1

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_student_number(self):
        return self.student_number

    def get_status(self):
        return self.status

    def get_grades_list(self):
        return self.grades

    def print_student_info(self):
        grades_print = ""
        for i in self.grades:
            grades_print.join(str(i))
        print(grades_print)
        print(self.first_name, self.last_name, self.student_number, str(self.status), str(self.grades))



