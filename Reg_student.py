from main import Student

try:
    Student_name = input("Enter Your Name \n")
    Student_ID = input("Enter Your ID \n")
    Student_class = input("Enter Your Class \n")

    Student.create(student_name=Student_name, student_ID=Student_ID, student_class=Student_class)
    print("Student Created Successfully")
except:
    print("Failed to create a User,Retry")
