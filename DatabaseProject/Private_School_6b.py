

import sys

import config
import datetime
#make the connection with the database
conn, myCursor=config.make_connection()
myCursor.execute('use Private_School;')

# a function that the user gives an input 
# and the query that inserts data in the database to students table
def insert_Student():
    print("Insert information in Students")
    # a try/except statement for not giving an integer
    try:
        
        StID=(int(input("Give me a student id number:")))
    except ValueError:
           print("Oops! Thats not an integer. Try again..." )
    
   
                  
    firstname=input("Give me first name: ")
    if  any(char.isdigit() for char in firstname):
        print("Please do not include number in firstname")   
        
        
       
   
                   
    lastname=input("Give me last name: ")
    try:
        if  any(char.isdigit() for char in lastname):
            raise ValueError
    except ValueError:
        print("Please do not include number in lastname")
            
            
        
        
                  
           
    
    try:
        print("Give me a birthdate: ")
        year=int(input("Year: "))
        month=int(input("Month: "))
        day=int(input("Day: "))
        birthdate=(datetime.date(year,month,day))
        fees=int(input("Give me your tuition fees amount: "))
    except ValueError:
            print("Oops!You have to write numbers not words.Try again...!")
    students_query=('INSERT INTO Students (studentid,firstname,lastname,dateOfBirth,tuitionFees) \
                                VALUES(%s,%s,%s,%s,%s);')
                            
    myCursor.execute(students_query, (StID,firstname,lastname,birthdate,fees))
    
    conn.commit()
    
 # a function that the user gives an input 
# and the query that inserts data in the database to courses table    
def insert_Courses():
    print("Insert information in Courses")
    try:
        
        cID=(int(input("Give me a course id number:")))
    except ValueError:
           print("Oops! Thats not an integer. Try again..." )
           
    
                   
    title=input("Give me the title of the course")
    if  any(char.isdigit() for char in title):
        print("Please do not include number in title") 
        
        
    
    
    
                   
    stream=input("Give me the programming language name that interests you")
    try:
        if  any(char.isdigit() for char in stream):
            raise ValueError
    except ValueError:
        print("Please do not include number in stream")
        
        
        
   
                   
    type=input("Tell me if you want the part/time or the full/time type: ")
    try:
        if  any(char.isdigit() for char in type):
            raise ValueError
    except ValueError:
        print("Please do not include number in type")
        
        
    
         
        
    try:
        print("Write when you do want to start the course")
        start_year=int(input("Year: "))
        start_month=int(input("Month: "))
        start_day=int(input("Day: "))
        startDate=(datetime.date(start_year,start_month,start_day))
        print("Write when do you want to end the course")
        end_year=int(input("Year: "))
        end_month=int(input("Month: "))
        end_day=int(input("Day: "))
        endDate=(datetime.date(end_year,end_month,end_day))
    
    except ValueError:
           print("Oops! Thats not an integer. Try again..." )  
    course_query=('INSERT INTO Courses (courseid,title,stream,type,startDate,endDate)\
                            VALUES(%s,%s,%s,%s,%s,%s);')

    myCursor.execute(course_query,(cID,title,stream,type,startDate,endDate))
    conn.commit()
    
# a function that the user gives an input 
# and the query that inserts data in the database to trainers table
def insert_Trainers():
    print("Insert information in Trainers")
    
    try:
        
        trID=(int(input("Give me a trainer id number: ")))
    except ValueError:
           print("Oops! Thats not an integer. Try again..." )
            
    
    
                   
    firstname=input("Give me a first name: ")
    if  any(char.isdigit() for char in firstname):
        print("Please do not include number in firstname")
        
        
    
   
                   
    lastname=input("Give me a lastname: ")
    if  any(char.isdigit() for char in lastname):
        print("Please do not include number in lastname")
        
       
    
    
                   
    subject=input("Give me a programming language: ")
    try:
        if  any(char.isdigit() for char in subject):
            raise ValueError
    except ValueError:
        print("Please do not include number in subject")
        
        
        
          
            
    trainer_query=('INSERT INTO Trainers (trainerid,firstname,lastname,subject)\
                            VALUES(%s,%s,%s,%s);')

    myCursor.execute(trainer_query,(trID,firstname,lastname,subject))
    conn.commit()

# a function that the user gives an input 
# and the query that inserts data in the database to assignments table
def insert_Assignments():
    print("Insert information in Assignments")
    try:
        
        AssID=(int(input("Give me an assignment id number: ")))
    except ValueError:
           print("Oops! Thats not an integer. Try again..." )
           
    
                   
    title=input("Give me the title of the assignment: ")
    try:
        if  any(char.isdigit() for char in title):
            raise ValueError
    except ValueError:
        print("Please do not include number in title")
        
        
    
   
                   
    description=input("Give me the description of the assignment: ")
    try:
        if  any(char.isdigit() for char in description):
            raise ValueError
    except ValueError:
        print("Please do not include number in description")
        
        
        
        
    try:
        
        print("Give me a submission date")
        sub_year=int(input("Year: "))
        sub_month=int(input("Month: "))
        sub_day=int(input("Day: "))
        subDateTime=(datetime.date(sub_year,sub_month,sub_day))
        oralMark=(int(input("Give me the oral mark:")))
        totalMark=(int(input("Give me the total mark: ")))
    except ValueError:
           print("Oops! That's not an integer. Try again..." )            
    
    
            
    assignment_query=('INSERT INTO Assignments(assignmentid,title,description,subDateTime,oralMark,totalMark)\
                            VALUES(%s,%s,%s,%s,%s,%s);')

    myCursor.execute(assignment_query, (AssID,title,description,subDateTime,oralMark,totalMark))
    conn.commit()
    
# a function that the user gives an input 
# and the query that inserts data in the database to the students per course table
def insert_StudentsPerCourse():
    print("Insert information in Students per Course")
    try:
        
         Stu_per_CID=(int(input("Give me a student per course id number: ")))
    except ValueError:
           print("Oops! Thats not an integer. Try again..." )
            
            
    student_per_course_query=('INSERT INTO Students_per_course(spcid)\
                                        VALUES (%s);')

    myCursor.execute(student_per_course_query, (Stu_per_CID,)) 
    conn.commit()
    
# a function that the user gives an input 
# and the query that inserts data in the database to the trainers per course table    
def insert_TrainersPerCourse():
    print("Insert information in Trainers per course")
    try:
        
         Tr_per_CID=(int(input("Give me a trainer per course id number: ")))
    except ValueError:
           print("Oops! Thats not an integer. Try again..." )
    
    
    trainer_per_course_query=('INSERT INTO Trainers_per_course(tpcid)\
                                        VALUES (%s);')

    myCursor.execute(trainer_per_course_query, (Tr_per_CID))
    conn.commit()
    
# a function that the user gives an input 
# and the query that inserts data in the database to assignments per student per course table
def insert_AssignmentsPerStudentPerCourse():
    print("Insert information in assignments per student per course")
    try:
        
        ass_per_stu_cID=(int(input("Give an assignment per student per course id number: ")))
    except ValueError:
           print("Oops! Thats not an integer. Try again..." )
    
    
    assign_per_student_course_query=('INSERT INTO Assignments_per_student_per_course (apspcid)\
                                            VALUES(%s);')

    myCursor.execute(assign_per_student_course_query,(ass_per_stu_cID))                                        
    conn.commit()
    
    

    
    
 
# a function that give us an option to exit from the menu/system   
def quit():
    print("The system will exit now...")
    sys.exit()                                   
    
    
# a function that includes the menu components    
def menu():
    
    print("              ****** Private School Menu******            ")
    choice=input ("""
                    
                    A: Students
                    B: Trainers
                    C: Assignments
                    D: Courses
                    E: Students per Course
                    F: Trainers per Course
                    G: Assignments per Student per Course
                    H: Quit
                    
                    Please make a selection from A, B, C, D, E, F, G or H:
                    """)
    
    # an if/elif/else condition for assign the proper letter in a certain function
    if choice == "A" or choice == "a":
        insert_Student()
       

        
    elif choice == "B" or  choice == "b" :
        insert_Trainers()
        
    elif choice == "C" or choice == "c" :  
        insert_Assignments()
        
    elif choice == "D" or choice == "d" :
        insert_Courses()
        
    elif choice == "E" or choice == "e":
        insert_StudentsPerCourse()
        
    elif choice == "F" or choice == "f" :
        insert_TrainersPerCourse()
        
    elif choice == "G" or choice == "g":
        insert_AssignmentsPerStudentPerCourse()
        
    elif choice =="H" or choice == "h" :
        quit()
    else:
        print("Oops!You must enter a valid option")
        menu()
    
    
menu()    #call the menu function and display the menu in the terminal enviroment 




    

