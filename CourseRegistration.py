# This is where your code for Achievement Task 3: Course Registration will go.

# Name:                 CourseRegestration.py
# Author:               Meetkumar Patel
# Date Created:         February 20, 2022
# Date Last Modified:   February 27, 2022 

# Purpose:
#This program runs a course regestartion program where students are asked for input 
# regading their persona; information then asking them to select courses they would like to do.

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

#This dictionary holds all the courses and its name as value
courseInfoDict = {
    "PROG 1783" : "PROGRAMMING",
    "INFO 8025" : "IT INFRASTRUCTURE",
    "BUS 8530"  : "LEAN UX 3.0",
    "PROG 1009" : "COMPUTER PROGRAMMING"
}

print()
#Then the dictionary is printed out by using a loop
for key, value in courseInfoDict.items():
    print("{0:}{1:->25}".format(key, value))

#Here student is asked to select o=ne of the courses from above.
print()
userCourse = input("Please Select Your Courses by entering course code: \n").strip().upper()
userCourseSel = list(map(str, userCourse.split(", ")))  # Then its strored in a list 

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
print("{0:s}{1:}{2:}{3:}".format("Student Full Name : ", lst1, " " ,lst2))
print("{}{}{}".format("Student ID Number :"," ",lst3))
print()

print("The course selected by the students are as follows: \n")
#Here the loop is used to check the course selected by the student and also printing it out by matching / Checking it with dictionary.
for course in userCourseSel:
    #Now match userlist with dict of course and giving its output
    if course in courseInfoDict:
        courseValue = courseInfoDict[course]#Here we get the course value of the course selected thus can be used for displaying.
        print("{0:s}{1:->28s}".format(course, courseValue))
        print()
        continue
    else:
        print("The course selected is not in the current section!!!Please Try Again Later.")
        print()