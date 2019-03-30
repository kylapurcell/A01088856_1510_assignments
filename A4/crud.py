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


def add_student():
    #try:
        #first_name1 = input('What is the students first name')
        #last_name1 = input('What is the students last name')
    pass

print(add_grades())