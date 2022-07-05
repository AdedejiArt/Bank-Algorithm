#The author is Adio Adedeji
#Importing Created class(Clients)
from Bank_class import Clients
ClientList=[]
Client1=Clients("Adio","01344","Farmer","0")
Client2=Clients("Sharon","0245","Hustler","0")
ClientList.append(Client1)
ClientList.append(Client2)
#Choice of operation asked
def menulist():
    int(input(" To Withdraw money. Press 1. \n "
          "To View account balance. Press 2. \n "
          "To deposit money. Press 3. \n "
          "To Transfer Money. Press 4 \n "))
#Function for deposit
def deposit():
    print("Hello Customer")
    amount=str(input("Enter the amount you want to deposit"))
    print("You have successfully deposited"+" "+amount)
    print("Your new balance is" + amount)
#Function For Withdrawal
def Withdrawal():
    A=int(input("How much are you willing to withdraw"))
    print("You have Successfully withdrawn"+A)


#Function for viewing account balance
def View():
    for items in ClientList:
        print ("Your account Balance is"+" "+str(0))
#Function for Transfer
def Transfer():
    print("How much are you willing to transfer")
    Number= int(input("Enter the Person's account number"))
    Much=int(input("How much would be transferred"))
    print(str(Much)+" "+"has been transferred to account owner"+" "+str(Number))
