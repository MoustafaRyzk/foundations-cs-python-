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