"""
This is the main app file for running our app
"""
from user_interactions.user_functions import createStudent,studentsAboveEighty,viewStudents,studentAge,deleteStudentByID

while True:
    ch = None
    print("--------WELCOME To the studentFDB--------")
    print("1.view all students from the database.")
    print("2.create a student.")
    print("3.delete a student.")
    print("4.view all students having percentage above 80%.")
    print("5.calculate  age of a student.")
    ch = (input("Please Enter your choice --->"))
    if ch == '1':
        viewStudents()
    elif ch == '2':
        createStudent()
    elif ch == '3':
        deleteStudentByID()
    elif ch == '4':
        studentsAboveEighty()
    elif ch == '5':
        studentAge()
    else:
         ch  = input("You have entered a wrong choice? Do you want to continue?\nPress 'y' to CONTINUE or anything else to EXIT --->")  
         if ch != "y":
             break  

