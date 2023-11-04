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
    student_Lst = []
    number_Of_Students = input("Please Enter Number Of Students:")
    while not number_Of_Students.isnumeric() or number_Of_Students == "0":
        number_Of_Students = input("Please Enter Number Of Students:")
    number_Of_Students = int(number_Of_Students)
    for i in range(number_Of_Students):
        student_Dictionary = {}

        print("Please Enter ID of student", i + 1, ":", end=" ")
        ID = input()
        while not ID.isnumeric():
            ID = input("Please Enter ID of student:")
        ID = int(ID)
        student_Dictionary["ID"] = ID

        print("Please Enter Name of student", i + 1, ":", end=" ")
        name = input()
        student_Dictionary["Name"] = name

        print("Please Enter student", i + 1, "age:", end=" ")
        age = input()
        while not age.isnumeric():
            age = input()
        age = int(age)
        student_Dictionary["Age"] = age

        print("Please Enter student", i + 1, "major: ", end="")
        major = input()
        student_Dictionary["Major"] = major

        print("Please Enter student", i + 1, "GPA: ", end="")
        GPA = input()
        while not GPA.isnumeric():
            GPA = input("Please Enter student GPA")
        GPA = float(GPA)
        student_Dictionary["GPA"] = GPA
        student_Lst.append(student_Dictionary)
    return student_Lst


def getStudentByID(student_Lst):
    ID = input("Please Enter ID of student: ")
    while not ID.isnumeric():
        ID = input("Please Enter ID of student:")
    ID = int(ID)
    for x in range(len(student_Lst)):
        if student_Lst[x]["ID"] == ID:
            return student_Lst[x]

    return -1


def getStudentsByMajor(student_Lst):
    studentsNames = []
    Major = input("Please enter the major of the students you want information about:")
    for x in range(len(student_Lst)):
        if student_Lst[x]["Major"] == Major:
            studentsNames.append(student_Lst[x]["Name"])
    if len(studentsNames) == 0:
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


def findCommonMajors(student_List1, student_List2):
    majors_student1 = set()
    majors_student2 = set()

    for student in student_List1:
        majors_student1.add(student['Major'])

    for student in student_List2:
        majors_student2.add(student['Major'])

    common_majors = set()
    for major in majors_student1:
        if major in majors_student2:
            common_majors.add(major)

    return common_majors


def deleteStudent(student_List):
    student_lst = student_List
    student_By_ID = getStudentByID(student_List)
    if student_By_ID == -1:
        print("Student not found!!!")
        return student_lst
    else:
        student_lst.remove(student_By_ID)
    return student_lst


def calculateAverageGPA(student_List):
    if len(student_List) <= 0:
        print("sry no student found to calculate GPA average!!!")
        return 0
    total_Average = 0
    for student in student_List:
        total_Average += student["GPA"]
    return total_Average / len(student_List)


def getTopPerformance(student_list):
    students_Highest_GPAs = input("Please enter number of student you want of highest GPAs:")
    while not students_Highest_GPAs.isnumeric():
        students_Highest_GPAs = input("Please enter number of student you want of highest GPAs:")
    students_Highest_GPAs = int(students_Highest_GPAs)

    #if len(student_list) <= 0:
     #   return 0

    lst_GPAs = []
    for x in range(len(student_list)):
        lst_GPAs.append(student_list[x]["GPA"])

    lst_GPAs.sort(reverse=True)
    students = []
    for i in range(students_Highest_GPAs):
        sub_Student = []
        for j in range(len(student_list)):
            if student_list[j]["GPA"] == lst_GPAs[i]:
                sub_Student.append(student_list[j]["Name"])
                sub_Student.append(student_list[j]["GPA"])
        students.append(sub_Student)
    students = tuple(students)
    return students


def startApplication(student_List):
    user_Choice = 1
    while user_Choice != 9:
        student_lst = student_List
        menu()
        user_Choice = input("Please enter your choice:")
        while not user_Choice.isnumeric or not (
                (user_Choice == "1") or (user_Choice == "2") or (user_Choice == "3") or (user_Choice == "4") or (
                user_Choice == "5") or (user_Choice == "6") or (user_Choice == "7") or (user_Choice == "8") or (
                        user_Choice == "9")):
            user_Choice = input("Please enter your choice between 1 and 9:")
        user_Choice = int(user_Choice)

        if user_Choice == 1:
            user_Information = getStudentByID(student_lst)
            if user_Information == -1:
                print("User not found")
            else:
                for x, y in user_Information.items():
                    print(x, ":", y)

        elif user_Choice == 2:
            for student in student_lst:
                for x, y in student.items():
                    print(x, ":", y)
                print("************")

        elif user_Choice == 3:
            students_info = getStudentsByMajor(student_lst)
            if students_info == 0:
                print("User not found")
            else:
                print(students_info)

        elif user_Choice == 4:
            student_lst.append(addNewStudent())

        elif user_Choice == 5:
            print("common majors of the 2 lists of students are", find_Common_Majors(student_List, student_List))

        elif user_Choice == 6:
            student_lst = deleteStudent(student_lst)

        elif user_Choice == 7:
            total_GPA_Average = calculateAverageGPA(student_List)
            print("Total GPA average of all student =", total_GPA_Average)

        elif user_Choice == 8:
            print(getTopPerformance(student_lst))

        elif user_Choice == 9:
            quit()

        else:
            print("Inavild Number !!!")


def main():
    startApplication(getStudentList())


main()
