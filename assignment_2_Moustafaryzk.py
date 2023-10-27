# assignmentt num 2

def GetDigit(text):

    num = input(text)
    while not num.isdigit():
        num = input(text)
    num = int(num)
    return num
def Menu():
    print("1. Count Digits")
    print("2. Find Max    ")
    print("3.1. Count Tags")
    print("3.2. Count Normalized Columns")
    print("4. Exit")
    print("---------------------------")


def count_Digits(number):
    if number == 0:
        return 0
    elif number < 0:
        number = -number
    return 1 + count_Digits(number // 10)

def get_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        sub_max = get_max(lst[1:])
        if lst[0] > sub_max:
            return lst[0]
        else:
            return sub_max


def Start_assignment():

        Menu()

        user_Choice=input("Please Enter your choice:")
        while not ((user_Choice.isdigit()) and ((user_Choice =="1") or (user_Choice =="2") or (user_Choice =="3") or (user_Choice =="4"))):
            user_Choice = input("Please Enter your choice:")

        user_Choice=int(user_Choice)

        if user_Choice==1:
            num = input("Please enter a number:")
            while not ((num[0] == "-" and num[1:].isdigit()) or num.isdigit()):
                num = input("Please enter a number:")
            num=int(num)

            print(count_Digits(num))

        if user_Choice==2:
            lst = []
            num_Item=GetDigit("Please Enter Number of Items")
            for i in range(num_Item):
                item = input("Enter item:")
                while not item.isdigit():
                    item = input("Enter item:")
                item = int(item)
                lst.append(item)
            print("max item = ", get_max(lst))


      


        if user_Choice==4:
            quit()


