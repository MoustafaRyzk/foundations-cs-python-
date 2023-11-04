def menu():
    print("""1. Get Student by ID
2. Get All Students
3. Get Students by Major
4. Add Student
5. Find Common Majors
6. Delete Student
7. Calculate Average GPA
8. Get Top Performers
9. Exit
- - - - - - - - - - - - - - -""")
    
def getStudentList():
    student_Lst=[]
    number_Of_Students=input("Please Enter Number Of Students:")
    while not number_Of_Students.isnumeric() or number_Of_Students=="0":
        number_Of_Students = input("Please Enter Number Of Students:")
    number_Of_Students=int(number_Of_Students)
    for i in range(number_Of_Students):
        student_Dictionary=dict()


        print("Please Enter ID of student", i + 1, ":", end=" ")
        ID = input()
        while not ID.isnumeric():
            ID = input("Please Enter ID of student:")
        ID=int(ID)
        student_Dictionary["ID"] = ID

        print("Please Enter Name of student", i+1, ":", end=" ")
        name=input()
        student_Dictionary["Name"]=name

        print("Please Enter student", i+1, "age:", end=" ")
        age = input()
        while not age.isnumeric():
            age = input()
        age=int(age)
        student_Dictionary["Age"] = age

        print("Please Enter student", i+1, "major: ", end="")
        major = input()
        student_Dictionary["Major"] = major

        print("Please Enter student", i+1, "GPA: ", end="")
        GPA = input()
        while not GPA.isnumeric():
            GPA = input("Please Enter student GPA")
        GPA=float(GPA)
        student_Dictionary["GPA"] = GPA
        student_Lst.append(student_Dictionary)
    return student_Lst

def getStudentByID(student_Lst):
    ID = input("Please Enter ID of student: ")
    while not ID.isnumeric():
        ID = input("Please Enter ID of student:")
    ID = int(ID)
    for x in range(len(student_Lst)):
        if student_Lst[x]["ID"]==ID:
            return student_Lst[x]

    return -1

def getStudentsByMajor(student_Lst):
    studentsNames=[]
    Major = input("Please enter the major of the students you want information about:")
    for x in range(len(student_Lst)):
        if student_Lst[x]["Major"] == Major:
            studentsNames.append(student_Lst[x]["Name"])
    if len(studentsNames)==0:
        return 0
    else:
        return studentsNames
    
def addNewStudent():
    new_Student = {}

    print("Please Enter ID of new student :", end=" ")
    ID = input()
    while not ID.isnumeric():
        ID = input("Please Enter ID of new student: ")
    ID = int(ID)
    new_Student["ID"] = ID

    print("Please Enter Name of new student:", end=" ")
    name = input()
    new_Student["Name"] = name

    print("Please Enter new student age :", end=" ")
    age = input()
    while not age.isnumeric():
        age = input("Please Enter new student age:")
    age = int(age)
    new_Student["Age"] = age

    print("Please Enter new student major: ", end="")
    major = input()
    new_Student["Major"] = major

    print("Please Enter new student GPA: ", end="")
    GPA = input()
    while not GPA.isnumeric():
        GPA = input("Please Enter student GPA")
    GPA = float(GPA)
    new_Student["GPA"] = GPA
    return new_Student    
    
    