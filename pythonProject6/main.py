#The author is ADIO ADEDEJI
#Importing Functions from Dangote 2
from Bank_function import *
#While loop  to continue operation
answer = "yes"
while answer == "yes":

    menulist()
    value = int(input("Enter your  number one more time: "))
    if value == 1:
        Withdrawal()

    if value == 2:
        View()

    if value == 3:
        deposit()

    if value == 4:
        Transfer()