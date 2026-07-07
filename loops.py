for i in range(5):
    print("hima")


###################

users=["hima","thanu","siri","sak","venu"]
for users in users:
    print("message sent to",users)

###################

for i in range(2,6):
    print(i)

#####################

name = ["dhoni"]

for ch in name:
    print(ch)

name = "dhoni"

for ch in name:
    print(ch)

######################

count = 1
while count <=5:
    print(count)
    count += 1

####################

for i in range(10):
    if i == 5:
        break
    print(i)

####################

for i in range(10):
    if i == 5:
        continue
    print(i)

#########################

password = ""
while password != "1234":
    password = input("enter password")
    print("login success")

########################

student = [
    "ram",
    "sam",
    "rana"
]
student.remove("sam")
student.append("Alex")
print(student)



