from model.student import Student

def createStudent():
    print("Creating a student .....")
    s_name = input("Enter name of the student.------>")
    s_email = input("Enter email of the student.------>")
    s_english_marks = input("Enter marks scored in english.------>")
    s_maths_marks = input("Enter marks scored in maths.------>")
    s_science_marks = input("Enter marks scored in science.------>")
    s_d_o_b = input("Enter Date of Birth of the student.------>")
    student = Student(s_name , s_email,s_english_marks,s_maths_marks,s_science_marks,s_d_o_b)
    if student:
        print(f"You have created a student \n{student}")
        student.save()
    else:
        print("Failed to create a user.")

def viewStudents():
    print("*"*20,' students ',"*"*20)
    students = Student.view_students()   
    for student in students:
        print(student)

def findStudentByName():
    print("*"*20,'find students ',"*"*20)
    print("Searching students by name..")
    search_name = input("Enter the name of a student ==>")
    students = Student.find_student_by_name(search_name)
    if students:
        for student in students:
            print(student)
    else:
        print("No Student found.")


def studentsAboveEighty():
    print("*"*20,' students abov 80 %',"*"*20)
    students = Student.view_students() 
    students_above_eighty = list(filter(lambda x :(int(x.s_english_marks) + int(x.s_maths_marks) + int(x.s_science_marks))/300 > 0.8 , students))
    if students_above_eighty:
        for student in students_above_eighty:
            print(student)
def deleteStudentByID():
    print("*"*20,'delete student ',"*"*20)
    print("Deleting students by ID..")
    id = input("Enter the ID of a student you want to remove ==>")
    Student.delete_student_by_id(id)
    


def studentAge():
    print("*"*20,'age of student ',"*"*20)
    id = input("Enter the ID of a student you want age ==>")
    students = Student.view_students()
    print(students)

