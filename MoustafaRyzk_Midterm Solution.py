import json
import requests
from bs4 import BeautifulSoup #https://www.youtube.com/watch?v=taL3r_JpwBg

#----------------
#for reusability:
#----------------
def getPositiveIntegerNumber(text_Message, hint):
    number=input(text_Message)

    while not number.isnumeric():
        print(hint)
        number = input(text_Message)

    return int(number)

def getPostiveIntNumFrom_to(text_Message, hint, fr_om, to):
    while True:
        number = getPositiveIntegerNumber(text_Message, hint)
        if (number>=fr_om) and (number<=to):
           return number

        print(hint)
#----------------------------------------------------------------#

def displayMenu():
    print("\n####################")
    print("#       Menu       #")
    print("####################")
    print("1. Open Tab")
    print("2. Close Tab")
    print("3. Switch Tab")
    print("4. Display All Tabs")
    print("5. Open Nested Tab")
    print("6. Clear All Tabs")
    print("7. Save Tabs")
    print("8. Import Tabs")
    print("9. Exit")
    print("####################")
    print()

def openTab():
    title = input("PLease enter the title of the website: ")

    url = input("Please enter the URL of the website: ")
    tabs.append(tab)