

# #~----------Encapsulation-------~#


# from abc import ABC,abstractmethod
# class parent(ABC):
    
#     @staticmethod
#     def wakeup():
#         print("I am from parent class")
#     @abstractmethod
#     def income():
#         pass

# class child(parent):
#     @staticmethod
#     def income():
#         print("I earn only 20k")

# # child.wakeup()
# # c1=child()
# child.income()

#? Create a class vehicle which is a abstract class and implemnts a abstract method that is type of vehicle inside itself also create 2 sub class car and truck which implemts the abstract method in their own way

# from abc import ABC, abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def type(self):
#         pass
# class car(vehicle):
#     def type(self):
#         print("I am a car")
# class truck(vehicle):
#     def type(self):
#         print("I am a truck")
# c1=car()
# t1=truck()
# c1.type()
# t1.type()

#~-----------------Example-3------------------~#

#?WAP to create an abstract class bankaccount with abstract method deposit and withdraw . create subclass : savingaccount and currentaccount that extend the bankaccount and implement the respective method to handle deposits and withdrawl for each account tyoe 

from abc import ABC,abstractmethod
class bankaccount(ABC):
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
    def __init__(self,name,balance,accoutnumber):
        self.NAME=name
        self.BALANCE=balance
        self.ACCOUNTNUMBER=accoutnumber
class savingaccount(bankaccount):
    def withdraw(self):
        n=int(input("enter the amount to withdrawl : "))
        if n<self.BALANCE:
            self.BALANCE-=n
            print("withdrawl successful")
        else:
            print("insufficient balance")
    def deposit(self):
        n=int(input("enter the amount to deposit : "))
        self.BALANCE+=n
        print("deposit successful",self.BALANCE)
class currentaccount(bankaccount):
    def withdraw(self):
        n=int(input("enter the amount to withdrawl : "))
        if n<self.BALANCE:
            self.BALANCE-=n
            print("withdrawl successful")
        else:
            print("insufficient balance")
    def deposit(self):
        n=int(input("enter the amount to deposit : "))
        self.BALANCE+=n
        print("deposit successful")

s1=savingaccount("Rahul",1000,123456)
c1=currentaccount("Preksha",1000,123456)
s1.deposit()
s1.withdraw()
c1.deposit()
c1.withdraw()
    
        
        
    
        