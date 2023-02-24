from main import Student

my_student = Student.select()
for student in my_student:
    print(student.student_name, student.student_ID, student.student_class)
