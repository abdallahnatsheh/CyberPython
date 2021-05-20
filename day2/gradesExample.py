success_grades=['A', 'B', 'C', 'D']
faild_grade='F'

student_grade = input("enter your grade please: ")
student_grade = student_grade.upper()
if student_grade in success_grades:
    print("congratulation")
elif student_grade == faild_grade:
    print("good luck next year")
else:
    print("not valid grade")