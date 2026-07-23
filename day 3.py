####################tuple is a collection used to store multiple values & it is immutable##############################
student = ("ram","sam","bheem")
print(student)
####################
student = ("ram","sam","bheem")
print(student[1])
####################
numbers = (10,20,30,40)
print(numbers)
#####################
numbers = (10,20,30,40)
print(numbers [2])
#####################
numbers = (10,20,30,40)
print(numbers [-2])
#####################error###########
data = (1,2,3)
data[0] = 100
print(data)
########################
x = (1,2,3,2,1,1,1)
print(x.count(1))
print(x.count(2))
print(x.count(3))
###################
x = ("apple","banana","grapes","banana")
print(x.count("banana"))
#####################
num = (10,20,30,40,50)
print(num[1:4])
###############sets###############

x={1,2,3,2,1,1,1}
print(x)
data={1,2,3}
data.add(4)
print(data)

x={1,2,3,2,1,1,1}
print(x)
data={1,2,3}
data.remove(2)
print(data)

a={1,2,3}
b={3,4,5}
print(a|b)

a={1,2,3}
b={3,4,5}
print(a&b)

#############function#############
def greeting():
    print("hello world")
    greeting()


def sub():
    return 10-20
result=sub()
print(result)

def add():
    return 10+20
result=add()
print(result)

#########################

def add(a,b):
    print(a+b)
add(10,20)

def add(*numbers):
    print(numbers)
add(10,20,30,40,50,60)

def add (*num):
    total = 0
    for i in num:
        total +=i
    print(total)
add(10,20,30,40,50,60)

#############kwargs################

def student(**details):
    print("name:",details["name"])
    print("age:",details["age"])
    print("job:",details["job"])

student(
    name="hima",
    age=22,
    job="sales",
)

def square(x):
    return x * x
print(square(16))

a=2
print("square:",a*a)

square = lambda x:x*x
print(square(25))

add=lambda a,b:a+b
print(add(10,2))

even=lambda a:a%2==0
print(even(1))

odd=lambda a:a%2!=0
print(odd(3))

even=lambda a:"even" if a%2==0 else"odd"
print(even(0))
print(even(1))
print(even(16))

upper = lambda a:a.upper()
print(upper("himani"))

lower=lambda a:a.lower()
print(lower("HIMANI"))

length=lambda a:len(a)
print(length("himani"))

##########file handling##############
#write in a file
file=open("student.txt","w")
file.write("hello hima")
file.close()

print("data written successfully")


# #read in a file
file=open("student.txt","r")
data=file.read()
print(data)
file.close()


#append a file
file=open("student.txt","a")
file.write("hello")
file.close()

print("data appended successfully")

file=open("student.txt","r")
print(file.read())
file.close()

###handling exception error####
try:
    a=10
    b=0
    print(a/b)
except:
    print("something went wrong")

#######handling specific error#########

try:
    num=int(input("enter number"))
    print(num)
except ValueError:
    print("only number allowed")

try:
    a=int(input("enter A:"))
    b=int(input("enter B:"))
    print(a/b)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("enter only numbers")

####final block####

try:
    file=open("data.txt")
    print(file.read())
except:
    print("file error")

finally:
    print("program completed")

###else block###
try:
    print(10/2)
except:
    print("error")
else:
    print("success")

