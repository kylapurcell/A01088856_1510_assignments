class Student:

    counter = 0

    def __init__(self, first_name: str, last_name: str, student_number: str, status: bool, grades:list):
        self.grades = grades
        if first_name is None or last_name is None or student_number is None or status is None:
            raise ValueError('A student must have a first name, last name, student number , and grades')
        else:
            self.first_name = first_name
            self.last_name = last_name
            self.student_number = student_number
            self.status = status
        self.id = Student.counter
        Student.counter += 1

    def 
