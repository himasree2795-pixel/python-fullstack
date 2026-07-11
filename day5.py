######encapsulation means wrapping variables and methods together inside a class and controlling access of the data##########

class bank:
    def __init__(self):
        self.balance = 10000
account = bank()
account.balance = 1000000000
print(account.balance)
#############################
class bank:
    def __init__(self):
        self.__balance = 10000
    def deposit(self,amount):
        self.__balance += amount
    def show_balance(self):
        print(self.__balance)
account = bank()
account.deposit(5000)
account.show_balance()
#################################
#######getter##############
class employee:
    def __init__(self,salary):
        self.__salary = salary
    def get_salary(self):
        return self.__salary
emp = employee(52836)
print(emp.get_salary())
##############################
######## Setter ########
class employee:
    def __init__(self):
        self.__salary = 0
    def set_salary(self,amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("invalid salary")
    def get_salary(self):
        return self.__salary
emp = employee()
emp.set_salary(52836)
print(emp.get_salary())
##################################
############polymorphism##############
##polymorphism means the same method name can perform different action depending on the object#######
class dog:
    def sound(self):
        print("dog barks")
class cat:
    def sound(self):
        print("cat meows")
Dog = dog()
Cat = cat()

Dog.sound()
Cat.sound()
################################
class CreditCard:
    def pay(self):
        print("Payment with Credit Card")

class DebitCard:
    def pay(self):
        print("Payment with Debit Card")

class UPI:
    def pay(self):
        print("Payment with UPI")

credit = CreditCard()
debit = DebitCard()
upi = UPI()

credit.pay()
debit.pay()
upi.pay()
############################
#########abstraction##########
######abstraction means hiding internal implementation and showing only necessary feature to the user###########

from abc import ABC, abstractmethod
class vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class car(vehicle):
    def start(self):
        print("car started")

car =car()
car.start()
###############################
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog barks")

dog = Dog()
dog.sound()
#################################
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def sleep(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog barks")
    def eat(self):
        print("Dog eats bones")
    def sleep(self):
        print("Dog sleeps at night")
dog = Dog()
dog.sound()
dog.eat()
dog.sleep()
##########################################
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
    @abstractmethod
    def eat(self):
        pass
    @abstractmethod
    def move(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog barks")
    def eat(self):
        print("Dog eats bones")
    def move(self):
        print("Dog runs")
class Cat(Animal):
    def sound(self):
        print("Cat meows")

    def eat(self):
        print("Cat drinks milk")

    def move(self):
        print("Cat jumps")

class Cow(Animal):
    def sound(self):
        print("Cow moos")

    def eat(self):
        print("Cow eats grass")

    def move(self):
        print("Cow walks")

dog = Dog()
cat = Cat()
cow = Cow()

dog.sound()
dog.eat()
dog.move()

cat.sound()
cat.eat()
cat.move()

cow.sound()
cow.eat()
cow.move()

