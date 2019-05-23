#ATM
#Deposit
#withdraw
#check balance
#change pin
print("****welcome****")
pin=int(input("Enter your pin:\n"))
act_amt=1000
print("you have"+" ",act_amt," "+"in your account")
print("1. Deposit\n2. Withdraw\n3. Check balance\n4. Change pin\n5. Exit")
def deposite(amt):
    global act_amt 
    act_amt=act_amt+amt
    return act_amt
def withdraw(amt):
    global act_amt
    if(amt=<act_amt):
        act_amt=act_amt-amt
        return act_amt
    else:
        print("Insufficient balance!")
def checkbal():
    print("you amount is:",act_amt)
def changepin():
    pin=int(input("Enter the new pin:"))
    print("you have successfully changed the pin ")
while(1):    
    var=int(input("Enter your choice:\n"))
    if(var==1):
        amt=int(input("Enter the amount to be deposited:\n"))
        deposite(amt)
        print("your current balance is:",act_amt)
    elif(var==2):
        amt=int(input("Enter the withdraw amount:\n"))
        withdraw(amt)
        print("your current balance is:",act_amt)
    elif(var==3):
        checkbal()
    elif(var==4):
        changepin()        
    elif(var==5):
        print("your current balance is:",act_amt)
        print("^^^^Thank You!^^^^")
        break
    
