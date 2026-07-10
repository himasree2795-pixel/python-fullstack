class student: #class name
    name = "hima" #attribute
    def study(self): #represent current object
        print("hima is studying")
s1 = student() #s1 is an object
print(s1.name)
s1.study() #study is a method

class student:
    def details(self):
        print("had breakfast")
s1 = student()
s1.details()

student.details(s1)

class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
s1 = student("hima",20)
s2 = student("thanu",21)
s3 = student("siri",21)
print(s1.name ,s2.name ,s3.name)
print(s1.age,s2.age,s3.age)

class bank:
    def __init__(self,balance):
        self.balance = balance

    def check_balance(self):
        print(self.balance)
account = bank(5000)
account.check_balance()

class user:
    def __init__(self,name):
        self.name=name
    def login(self):
        print(self.name,"logged in")

u1=user("hima")
u2=user("venu")
u1.login()
u2.login()

class father:
    def house(self):
        print("Father has a house")

class son(father):
    def bike(self):
        print("son has a bike")

s=son()
s.house()
s.bike()

class grandfather:
    def land(self):
        print("Grandfather has land")

class father(grandfather):
    def house(self):
        print("Father has a house")

class son(father):
    def bike(self):
        print("Son has a bike")

s = son()
s.land()
s.house()
s.bike()

class father:
    def house(self):
        print("Father has a house")

class mother:
    def jewelry(self):
        print("Mother has jewelry")

class son(father, mother):
    def bike(self):
        print("Son has a bike")

s = son()
s.house()
s.jewelry()
s.bike()

class father:
    def house(self):
        print("Father has a house")

class son(father):
    def bike(self):
        print("Son has a bike")

class daughter(father):
    def car(self):
        print("Daughter has a car")

s = son()
s.house()
s.bike()

d = daughter()
d.house()
d.car()

class student:
    def __init__(self,name):
        self.name=name
    
    def __str__(self):
        return self.name

s = student("king")
print(s)

def login(func):
    def wrapper():
        print("checking login")
        func()
    return wrapper
@login
def dashboard():
    print("dashboard page")
dashboard()

def message(func):
    def wrapper():
        print("function started")
        func()
        print("function ended")
    return wrapper
@message
def hello():
    print("hello python")
hello()
def hima():
    print("hello hima")
hima()

import json

student = {
    "name":"hima",
    "age":21
}
data=json.dumps(student)
print(data)

import json

data = '{"name":"hima","age":21}'

student = json.loads(data)
print(student["name"])
print(student["age"])

import requests

response = requests.get(
    "https://api.github.com/users/python"
)
data=response.json()
print(data)

