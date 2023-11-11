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
    correct_Url = False
    try:
        url_Reader = requests.get(url)
        correct_Url = True
    except:
        print(" << Invalid URL , please check website URL and try again >> ")

    if correct_Url:
        tab = {"title": title, "url": url}
        tabs.append(tab)

def closeTab():

    if len(tabs) == 0:
        print("You don't have any tab opened!!")
        return

    index = input("Please enter the index of tab you want to close , you can leave this field empty so we close last tab : ")
    if not index.isnumeric():
        if index == "":
            tabs.pop()
            print("Closing the last tab is completed")
            return
        else:
             print("Invalid tab index ")

    index = int(index)

    if index >= 0 and index < len(tabs):
        tabs.pop(index)
        print(f"Closing tab at index {index} completed")
    else:
        print(f"<< Index {index} is an Invalid tab index >>")


def switchTab():
    if len(tabs) == 0:
        print("<< You don't have any tab disply its content !! >>")
        return
    index = input("Please enter the index of tab you want to display its content : ")
    while not index.isnumeric():
        if index == "":
            index = len(tabs) - 1
            break
        else:
            index = input("Please enter the index of tab you want to display its content : ")
    index=int(index)

    if index >= 0 and index < len(tabs):
        tab = tabs[index]

        title = tab['title']
        url = tab['url']
        url_Reader = requests.get(url).content
        content = BeautifulSoup(url_Reader, "lxml")  # https://www.youtube.com/watch?v=taL3r_JpwBg

        print(f"title: {title}")
        print(f"URL: {url}")
        print(f"{content}")

    else:
        print(f"<< Index {index} is an Invalid tab index >>")