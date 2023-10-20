

###############
# Factorial(1)#
###############
def Factorial():
    num = input("Please Enter a Number:")
    while not (num.isnumeric()):
        num = input("Please Enter a Number:")
    num = int(num)

    factorial=""
    ruslt=1
    for x in range(1, num+1):
        ruslt = ruslt * x
        factorial= factorial + str(x) + " * "
    print(ruslt, "(", factorial[:-3], ")")

Factorial()

####################
# Divisors&lists(2)#
####################

number = input("Please Enter a Number: ")
while not number.isnumeric():
    number = input("Please Enter a Number: ")
number = int(number)

def divisors_List(number):
    divisors_List = []
    for x in range(number):
        if (number%(x+1)==0):
            divisors_List.append(x+1)
    print(divisors_List)

divisors_List(number)

###################
# reverseString(3)#
###################

def reserve_Text(text):
    reserveText=""
    for x in range(len(text)):
        reserveText+=text[(len(text)-1)-x]

    print(reserveText)

text=input("PLease Enter a text: ")
reserve_Text(text)

###############
# Even.List(4)#
###############

def is_Even(item):
    if item % 2 == 0:
        return True
    else:
        return False
def getList():
    list_1 = []
    n=input("Enter number of items:")
    while not (n.isnumeric()):
        n = input("Enter number of items")
    n=int(n)
    for i in range(0, n):
        item = input("Please Enter item: ")
        while not (item.isnumeric()):
            item = input("Please Enter item: ")
        item=int(item)

        list_1.append(item)


    return list_1
def getEvenList(list):
    even_List = []
    for x in list:
        if is_Even(x):
            even_List.append(x)
    print(even_List)

getEvenList(getList())

#####################
# strongePassword(5)#
#####################


def more_Then_8_Charachters(Password):
    if len(Password) >= 8:
        return True
    else:
        return False

def have_Upper_Letter(Password):
    for x in Password:
        if x.isupper():
            return True
    else:
        return False

def have_Lower_Letter(Password):
    for x in Password:
        if x.lower():
            return True
    else:
        return False

def have_Digit(Password):
    for x in Password:
        if x.isdigit():
            return True
    else:
        return False

def have_Special_Char(Password):
    for x in Password:
        if (x == ("#")) or (x == ("!")) or (x == ("$")) or (x == ("?")):
            return True
    else:
        return False

def is_Stronge_PassWord():
    Password = input("PLease Enter a Password:  ")
    if (more_Then_8_Charachters(Password) and have_Upper_Letter(Password) and have_Lower_Letter(Password) and have_Digit(Password) and have_Special_Char(Password)):
        print("Stronge Password")
    else:
        print("Weak Password")

is_Stronge_PassWord()

########################
# valid.IPv4.address(6)#
########################

def is_valid_ipv4_address(ip_address):
    octets = ip_address.split('.')
    if len(octets) != 4:
        return False

    for octet in octets:
        if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
            return False
        if octet[0] == '0' or len(octet) < 1:
            return False

    return True

ip_address = input("Please Enter ip-address:")
if is_valid_ipv4_address(ip_address):
    print("Valid ip-adress")
else:
    print ("invalid ip-address!!")
