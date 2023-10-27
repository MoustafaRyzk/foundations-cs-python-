###################
# assignmentt 2   #
###################

def GetDigit(text):

    num = input(text)
    while not num.isdigit():
        num = input(text)
    num = int(num)
    return num

def Menu():
    print("1. Count Digits")
    print("2. Find Max    ")
    print("3. Count Tags")
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

def count_tag(html, tag):
    if len(html) == 0:
        return 0

    opening_tag = "<" + tag + ">"
    closing_tag = "</" + tag + ">"

    opening_index = html.find(opening_tag)
    if opening_index == -1:
        return 0

    closing_index = html.find(closing_tag, opening_index)
    if closing_index == -1:
        return 0

    count = 1
    updated_html = html[closing_index + len(closing_tag):]
    count += count_tag(updated_html, tag)

    return count

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


        if user_Choice==3:
            html_code = input("Enter the HTML code: ")
            html_tag=input("Enter tag")
            print("number of tag", html_tag, "=", count_tag(html_code,html_code))


        if user_Choice==4:
            quit()


def main():

    Start_assignment()

main()