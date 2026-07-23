product_price = 5000
delivery_charge = 100

total = product_price + delivery_charge
print(total)

a=10
b=3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)

student = 10
groups = 2

print(student // groups)

##################

followers = 100
followers += 1
print(followers)

##################

saved_password = "1234"
enterd_password = "abcd"

print(saved_password == enterd_password)

balance = 500
pin_correct = True 
if balance >= 1000 and pin_correct:
    print("withdraw allowed")
else:
    print("failed")    

balance = 500
pin_correct = True 
if balance <= 1000 and pin_correct:
    print("withdraw allowed")
else:
    print("failed")   



item = input("Enter item name: ")
price = float(input("Enter price: "))
qty = int(input("Enter quantity: "))
discount = int(input("enter discount amount"))

total = price * qty
final_bill = total - discount

print(item)
print(price)
print(qty)
print(total)
print(final_bill)
