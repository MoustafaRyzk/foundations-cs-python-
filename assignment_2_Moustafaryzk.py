# assignmentt num 2


def Menu():
    print("1. Count Digits")
    print("2. Find Max    ")
    print("3.1. Count Tags")
    print("3.2. Count Normalized Columns")
    print("4. Exit")
    print("---------------------------")
    print("Enter a Choice:")

def count_Digits(number):
    if number == 0:
        return 0
    elif number < 0:
        number = -number
    return 1 + count_Digits(number // 10)
    
