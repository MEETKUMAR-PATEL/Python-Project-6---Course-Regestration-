# This is where your code for Achievement Task 3: Course Registration will go.

# Name:                 CourseRegestration.py
# Author:               Meetkumar Patel
# Date Created:         February 20, 2022
# Date Last Modified:   February 27, 2022 

# Purpose:
#This program runs a course regestartion program where students are asked for input 
# regading their persona; information then asking them to select courses they would like to do.
import os
filename = "UserConfirmation.txt"
#Welcome screen
print()
print("{0:-^50}".format("Course Regestration"))
print()
#Students give their personal information
firstName = input("Please Enter your First Name: ").strip().capitalize()
secName = input("Please Enter your Last Name: ").strip().capitalize()
studentNum = int(input("Please Enter Your Student Number:").strip())

#The student information is stored in a list (infolst)
infoLst = []
infoLst.append(firstName)
infoLst.append(secName)
infoLst.append(studentNum)

decsion = "2"
while decsion == "2":
    #This dictionary holds all the courses and its name as value
    courseInfoDict = {
        "PROG1783" : "PROGRAMMING",
        "INFO8025" : "IT INFRASTRUCTURE",
        "BUS8530"  : "LEAN UX 3.0",
        "PROG1009" : "COMPUTER PROGRAMMING"
    }

    print()
    #Then the dictionary is printed out by using a loop
    for key, value in courseInfoDict.items():
        print("{0:}{1:->25}".format(key, value))

    #Here student is asked to select o=ne of the courses from above.
    print()
    userCourse = input("Please Select Your Courses by entering course code: \n").strip().upper()
    if len(userCourse) == 0:
        print("You havent selected any course!!")
        decsion = input("Please select: 1 - To exit the program 2 - To continue selecting the program: ")
        if decsion == 1:
            break
        else:
            continue
    else:
        pass
    userCourseSel = list(map(str, userCourse.split(",")))  # Then its strored in a list 

    #Prints the students personal information and then also displaying the courses selected
    separator = " "
    studentLst = []
    for x in infoLst:
        studentLst.append(str(x))
    # Here the information is going through a loop and being separated to different variables and then used for an output    
    lst1 = "".join(studentLst[0])
    lst2 = "".join(studentLst[1])
    lst3 = "".join(studentLst[2])

    print()
    # This will print the students information provided by the student
    print("{0:-^50}".format("Student Information"))
    print("{0:s}{1:^22}{2:}{3:}{4:}".format("Student Name: "," ",lst1, " " ,lst2))
    print("{0:s}{1:^20}{2:}".format("Student Number: "," ",lst3))
    print("Total number of registered courses: ", len(userCourseSel))
    print("{0:-^50}".format(""))
    print()
    print("Course registration has been confirmed for the following courses: \n")
    #Here the loop is used to check the course selected by the student and also printing it out by matching / Checking it with dictionary.
    sep = ''
    studentNotLst = []
    mycourse = []
    i = 1
    for course in userCourseSel:
        #Now match userlist with dict of course and giving its output
        if course in courseInfoDict:
            courseValue = courseInfoDict[course]#Here we get the course value of the course selected thus can be used for displaying.
            if i <= 5:
                x = "Course #: {0:} {1:s}-{2:s}".format(i,courseValue, course)
                print(x)
                mycourse.append(x)
                i += 1
            print()
        else:
            #print("You give the program codes which are not available.")
            studentNotLst.append(course)
    print()
    #print("All non-existing course codes\n")
    for noCourse in studentNotLst:
        if len(noCourse) == 0:
            pass
        else:
            print("All non-existing course codes")
        
        print(noCourse)

    if len(userCourseSel) > 0:
        print()
        print("Thank you")
        print("Your file has been saved on\n\t{}\n\n".format(os.path.join(os.getcwd(), filename)))

        outDisplay = ""
        outDisplay += "{0:s}{1:^22}{2:}{3:}{4:}\n".format("Student Name: "," ",lst1, " " ,lst2)
        outDisplay += "{0:s}{1:^20}{2:}\n".format("Student Number: "," ",lst3)
        outDisplay += "Total number of registered course:  {}\n".format(len(userCourseSel))
        outDisplay += "{0:-^50}\n".format("")
        for x in mycourse:
            outDisplay += "{}\n".format(str(x))
        
        with open(filename, "a") as outputFile:
            outputFile.write(outDisplay)
    break

