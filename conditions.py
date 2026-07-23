password = input("enter password:")
if password == "admin123":
    print("welcome")

else:
    print("wrong password")



####################

marks = int(input("enter the marks:"))
if marks >= 90:
    print("A grade")
elif marks >= 75:
    print("B grade")
elif marks >= 50:
    print("C grade")
else:
    print("fail")    

#################

age = 25
salary = 50000
if age > 18 and salary > 30000:
    print("loan approved")

##################

day = "sunday"
if day == "saturday" or day == "sunday":
print("Holiday")

###################

login = True
 
if not login:
    print("print login")

####################

def withdraw_money():
    pin = 1234
    balance = 100000
    Pin = int(input("enter pin:"))
    if pin == Pin:
        print("current balance:",balance)
        amount = int(input("enter amount:"))
        if amount <= balance:
            balance = balance - amount
            print("Transaction successful")
            print("balance=",balance)
        else:
            print("no balance")
    else:
        print("wrong pin")    
withdraw_money()


