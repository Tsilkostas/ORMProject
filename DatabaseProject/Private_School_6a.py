import sys
import mysql.connector

import config
conn, myQueries=config.make_connection()    #make the connection with the database
myQueries.execute('use Private_School;')

#function that gives a query -that shows all the students- 
# to the database an returns the result in a list
def all_students():
    try:
        all_students_list=[]
        show_students='SELECT * FROM students'
        myQueries.execute(show_students)
    
        for i in myQueries:
            all_students_list.append(i)
        print(all_students_list)
    except mysql.connector.IntegrityError as er:
        conn.rollback()
        print("Oops!Something went wrong!Try again", er)
        
#function that gives a query -that shows all the trainers- 
# to the database an returns the result in a list      
def all_trainers():
    try:
        all_trainers_list=[]
        show_trainers='SELECT * FROM trainers'
        myQueries.execute(show_trainers)
        for (i) in myQueries:
            all_trainers_list.append(i)
        print(all_trainers_list)
    except mysql.connector.IntegrityError as er:
        conn.rollback()
        print("Oops!Something went wrong!Try again", er)
            
#function that gives a query -that shows all the assignments- 
# to the database an returns the result in a list      
def all_assignments():
    try:
        all_assignments_list=[]
        show_assignments='SELECT * FROM assignments'
        myQueries.execute(show_assignments)
        for (i) in myQueries:
            all_assignments_list.append(i)
        print(all_assignments_list)
    except mysql.connector.Error as er:
        conn.rollback()
        print("Oops!Something went wrong!Try again", er)
        
#function that gives a query -that shows all the courses- 
# to the database an returns the result in a list       
def all_courses():
    try:
        all_courses_list=[]
        show_courses='SELECT * FROM courses'
        myQueries.execute(show_courses)
        for(i) in myQueries:
            all_courses_list.append(i)
        print(all_courses_list)
    except mysql.connector.Error as er:
        conn.rollback()
        print("Oops!Something went wrong!Try again", er)
#function that gives a query -that shows all the students per course- 
# to the database an returns the result in a list       
def students_per_course():
    try:
        students_per_course_list=[]
        show_students_per_course='SELECT s.studentid,courseid,s.firstname,s.lastname,s.dateOfBirth,s.tuitionFees \
        FROM Students as s \
        INNER JOIN Students_per_course on s.studentid=Students_per_course.courseid; '
        myQueries.execute(show_students_per_course)
        for (i) in myQueries:
            students_per_course_list.append(i)
        print(students_per_course_list)
    except  mysql.connector.Error as er:
        conn.rollback()
        print("Oops!Something went wrong!Try again", er)
        
    
#function that gives a query -that shows all the trainers per course- 
# to the database an returns the result in a list    
def trainers_per_course():
    try:
        trainers_per_course_list=[]
        show_trainers_per_course='SELECT t.trainerid,courseid ,t.firstname,t.lastname,t.subject \
        FROM Trainers as t \
        INNER JOIN Trainers_per_course on t.trainerid=Trainers_per_course.courseid;'
        myQueries.execute(show_trainers_per_course)
        for (i) in myQueries:
            trainers_per_course_list.append(i)
        print(trainers_per_course_list)
    except mysql.connector.Error as er:
        conn.rollback()
        print("Oops!Something went wrong!Try again", er)
        
#function that gives a query -that shows all the assignments per student per course- 
# to the database an returns the result in a list    
def assignments_per_student_per_course():
    try:
        assignments_per_student_per_course_list=[]
        show_assignment_per_student_per_course='SELECT a.assignmentid,Assignments_per_student_per_course.studentid,Assignments_per_student_per_course.courseid,a.title,a.description,a.subDateTime,a.oralMark,a.totalMark \
        FROM Assignments as a \
        INNER JOIN  Assignments_per_student_per_course on Assignments_per_student_per_course.assignmentid=a.assignmentid \
        INNER JOIN Students on students.studentid=Assignments_per_student_per_course.studentid \
        INNER JOIN Courses on courses.courseid=Assignments_per_student_per_course.courseid;'
        myQueries.execute(show_assignment_per_student_per_course)
        for(i) in myQueries:
            assignments_per_student_per_course_list.append(i)
        print(assignments_per_student_per_course_list)
    except mysql.connector.Error as er:
        conn.rollback()
        print("Oops!Something went wrong!Try again", er)
        
  #function that gives a query -that shows all the students who attends in more than one courses- 
  # to the database an returns the result in a list  
def students_many_courses():
    try:
        students_many_courses=[]
        show_students_belong_to_more_than_one_courses='SELECT s.studentid,s.firstname,s.lastname,s.dateOfBirth,s.tuitionFees,count(s_per_c.studentid) from students as s \
        INNER JOIN students_per_course as s_per_c on s.studentid=s_per_c.studentid GROUP BY s_per_c.studentid HAVING count(s_per_c.studentid)>1;'
        myQueries.execute(show_students_belong_to_more_than_one_courses)
        for (i) in myQueries:
            students_many_courses.append(i)
        print(students_many_courses)
    except mysql.connector.Error as er:
        conn.rollback()
        print("Oops!Something went wrong!Try again", er)
        
        
        
   # a function that give us an option to exit from the menu/system   
def quit():
    print("The system will exit now...")
    sys.exit()                                   
    
    
# a function that includes the menu components    
def menu():
    
    print("              ****** Private School Menu******            ")
    choice=input ("""
                    
                    A: Show all Students
                    B: Show all Trainers
                    C: Show all Assignments
                    D: Show all Courses
                    E: Show all the Students per Course
                    F: Show all the Trainers per Course
                    G: Show all the Assignments per Student per Course
                    H: Show all Students that belong to more than one courses
                    I: Quit
                    
                    Please make a selection from A, B, C, D, E, F, G, H or I:
                    """)
    
    # an if/elif/else condition for assign the proper letter in a certain function
    if choice == "A" or choice == "a":
        all_students()
        

        
    elif choice == "B" or  choice == "b" :
        all_trainers()
        
    elif choice == "C" or choice == "c" :  
        all_assignments()
        
    elif choice == "D" or choice == "d" :
        all_courses()
        
    elif choice == "E" or choice == "e":
        students_per_course()
        
    elif choice == "F" or choice == "f" :
        trainers_per_course()
        
    elif choice == "G" or choice == "g":
        assignments_per_student_per_course()
    
    elif choice == "H" or choice == "h":
        students_many_courses()
        
    elif choice =="I" or choice == "i" :
        quit()
    else:
        print("Wrong!You must enter a valid option")
        menu()
    
    
menu()    #call the menu function and display the menu in the terminal enviroment 




    

     