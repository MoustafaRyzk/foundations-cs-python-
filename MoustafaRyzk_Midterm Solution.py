import json
import requests
from bs4 import BeautifulSoup  # https://www.youtube.com/watch?v=taL3r_JpwBg


# ----------------
# for reusability:
# ----------------
def getPositiveIntegerNumber(text_Message, hint):
    number = input(text_Message)

    while not number.isnumeric():
        print(hint)
        number = input(text_Message)

    return int(number)


def getPostiveIntNumFrom_to(text_Message, hint, fr_om, to):
    while True:
        number = getPositiveIntegerNumber(text_Message, hint)
        if (number >= fr_om) and (number <= to):
            return number

        print(hint)


# ----------------------------------------------------------------#

def displayMenu():
    print("\n####################")
    print("#       Menu       #")
    print("####################")
    print("1 . Open Tab")
    print("2 . Close Tab")
    print("3 . Switch Tab BY Index")
    print("4 . Display All Tabs")
    print("5 . Open Nested Tab")
    print("6 . Clear All Tabs")
    print("7 . Save Tabs")
    print("8 . Import Tabs")
    print("9 . Switch Tab By Title")
    print("10. Exit")
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
        print("<< You don't have any tab opened!! >>")
        return

    index = input(
        "Please enter the index of tab you want to close , you can leave this field empty so we close last tab : ")
    if not index.isnumeric():
        if index == "":
            tabs.pop()
            print("<< Closing the last tab is completed >>")
            return
        else:
            print("<< Invalid tab index >> ")

    index = int(index)

    if index >= 0 and index < len(tabs):
        tabs.pop(index)
        print(f"Closing tab at index {index} completed")
    else:
        print(f"<< Index {index} is an Invalid tab index >>")


def switchTabBYIndex():
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

    index = int(index)

    if index >= 0 and index < len(tabs):
        switched_Tab=[]
        switched_Tab.append(tabs[index])
        displayAllTabs(switched_Tab)
    else:
        print("<< Invalid tab index! >>")


def switchTabByTitle():  # I try to improve program <<program will display all content of tabs have title the user enter>

    title = input("Please enter the title of tab you want to display its content : ")
    found = False
    for tab in tabs:

        if title == tab['title']:
            print(f"title: {title}")
            url = tab['url']
            url_Reader = requests.get(url).content
            content = BeautifulSoup(url_Reader, "lxml")
            print(f"URL: {url}")
            print(f"content: {content}")
            found = True

        if 'nestedTabs' in tab:
            for tab in tab['nestedTabs']:
                if title == tab['title']:
                    print(f"title: {title}")
                    url = tab['url']
                    url_Reader = requests.get(url).content
                    content = BeautifulSoup(url_Reader, "lxml")
                    print(f"URL: {url}")
                    print(f"content: {content}")
                    found = True

    if not found:
        print(f"Tab with title {title} not found !!!")


def openNestedTab():
    if len(tabs) == 0:
        print("You don't have any tab opened!!")
        return

    parent_Index = input("Please enter the index of the tab you want to insert additional tabs in it : ")
    while not parent_Index.isnumeric():
        parent_Index = input("Please enter the index of the tab you want to insert additional tabs in it : ")
    parent_Index = int(parent_Index)

    if parent_Index >= 0 and parent_Index < len(tabs):
        parent_Tab = tabs[parent_Index]

        title = input("Enter the title of the nested tab: ")
        url = input("Enter the URL of the nested tab: ")

        correct_Url = False
        try:
            url_Reader = requests.get(url)
            correct_Url = True
        except:
            print(" << Invalid URL , please check website URL and try again >> ")
            return

        nested_Tab = {"title": title, "url": url}
        if 'nestedTabs' not in parent_Tab:
            parent_Tab['nestedTabs'] = []
        parent_Tab['nestedTabs'].append(nested_Tab)

    else:
        print("Invalid tab index.")


def displayAllTabs(tabs):
    if len(tabs)==0:
        return

    for tab in tabs:

        if 'nestedTabs' in tab:
            displayAllTabs(tab['nestedTabs'])



        title = tab['title']
        url = tab['url']
        url_Reader = requests.get(url).content
        content = BeautifulSoup(url_Reader, "lxml")  # https://www.youtube.com/watch?v=taL3r_JpwBg

        print(f"title: {title}")
        print(f"URL: {url}")
        print(f"content: {content}")




def clearAllTabs():
    tabs.clear()
    print("<< All tabs cleared >>")

def saveTabs():
    file_Path = input("Please enter file path to save the tabs on it : ")
    if file_Path.endswith(".json"):
        try:
            with open(file_path,'w') as file:  # https://programmingadvices.com/courses/introduction-to-programming-using-c-level-2/lectures/42360420
                json.dump(tabs, file)  # https://www.youtube.com/watch?v=C1crQ2-SIHc
                print("<< Tabs saved on file >>")  # https://www.geeksforgeeks.org/json-dump-in-python/
        except:
            print(" << Invalid file path , please check your file path and try again >> ")

    else:
        print("<< Sry, You must enter a jason file path only >>")


def importTabs():
    file_Path = input("Please enter the file path to import the tabs in it : ")
    if file_Path.endswith(".json"):
        try:
            with open(file_Path, 'r') as file:
                tabs.extend(json.load(file))  # https://www.geeksforgeeks.org/append-to-json-file-using-python/
                print("<< Tabs imported from file >>")
        except:
            print(" << Invalid file path , please check your file path and try again >> ")

    else:
        print("<< Sry, You must enter a jason file path only >>")


tabs = []  # her i make tabs a global variable take scoop of all project because no need to enter it as a parameter


# to all function one by one execpt [displayAllTabs must enter parameter => (recursive]


def startApp():
    print('''----------------------------------------------------------------------------
    # HELLO USER :) , WELCOME TO OUR ADVANCED BROWSER TABS SIMULATION #
----------------------------------------------------------------------------''')

    while True:

        displayMenu()

        user_choice = getPostiveIntNumFrom_to("Please Enter Your Choice: ",
                                              "<<You must enter integer number between 1 and 10 ", 1, 10)

        if user_choice == 1:
            openTab()

        elif user_choice == 2:
            closeTab()

        elif user_choice == 3:
            switchTabBYIndex()

        elif user_choice == 4:
            displayAllTabs(tabs)

        elif user_choice == 5:
            openNestedTab()

        elif user_choice == 6:
            clearAllTabs()

        elif user_choice == 7:
            saveTabs()

        elif user_choice == 8:
            importTabs()

        elif user_choice == 9:
            switchTabByTitle()

        elif user_choice == 10:
            print("\nTHANK YOU FOR USING OUR ADVANCED BROWSER TABS SIMULATION :) G00D BYE ")
            quit()


def main():
    startApp()

main()