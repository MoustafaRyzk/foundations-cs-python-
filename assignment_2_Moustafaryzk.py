# assignmentt num 2


def Menu():
    print("1. Count Digits")
    print("2. Find Max    ")
    print("3.1. Count Tags")
    print("3.2. Count Normalized Columns")
    print("4. Exit")
    print("---------------------------")
    print("Enter a Choice:")

def count_Digits():
    text=input("Please enter a number:")
    while not((text[0]=="-" and text[1:].isdigit()) or text.isdigit()):
        text = input("Please enter a number:")
    number_Of_Digits=0

    if text[0]=="-":
        for i in range(1, len(text)):
            number_Of_Digits += 1
        return number_Of_Digits
    else:
        for i in range(len(text)):
            number_Of_Digits+=1
        return number_Of_Digits