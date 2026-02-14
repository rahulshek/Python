
#& WAP to change the timing of Qspider class
# class Qspider:
#     BRANCH="Ahmedabad"
#     NO_OF_CLASSES=6
#     TIMING="10 to 8"

#     def __init__(self,name,course,degree):
#         self.NAME=name
#         self.COURSE=course
#         self.DEGREE=degree

#     @classmethod
#     def change_timing(cls,timing):
#         cls.TIMING=timing

#     @classmethod
#     def display(cls):
#         print(cls.BRANCH,cls.NO_OF_CLASSES,cls.TIMING)

# Qspider.display()    
# Qspider.change_timing("10 to 10")  
# Qspider.display()  


#~-----------------------------------------------------------------------------------------------------

#&WAP to change the course of student using class method

# class Qspider:
#     BRANCH="Ahmedabad"
#     NO_OF_CLASSES=6
#     TIMING="10 to 8"

#     def __init__(self,name,course,degree):
#         self.NAME=name
#         self.COURSE=course
#         self.DEGREE=degree
#     def display(self):
#         print(self.NAME,self.COURSE,self.DEGREE)
#     def change_course(self,course):
#         self.COURSE=course

#     @classmethod
#     def change_timing(cls,timing):
#         cls.TIMING=timing

#     @classmethod
#     def displaycls(cls):
#         print(cls.BRANCH,cls.NO_OF_CLASSES,cls.TIMING)


# s1=Qspider("Preksha","Python","B.Tech")
# s2=Qspider("Rahul","Java","B.Tech")
# s1.display()
# s1.change_course("C++")
# s1.display()
# s2.display()
# s2.change_course("C")
# s2.display()
# Qspider.displaycls()    
# Qspider.change_timing("10 to 10")  
# Qspider.displaycls()  

#~-----------------------------------------------------------------------------------------------------

#Create a class bank which consisit of bank name , branch name , barnch manager name and create 3 objects which consists of customer name , mail- id , contact number  and balance as object members also implement 2 class methods and 3 object methods for the example

class bank:
    BANK_NAME="Axis"
    BRANCH_NAME="Ahmedabad"
    BRANCH_MANAGER_NAME="Rahul"
    
    def __init__(self,customer_name,mail_id,contact_number,balance):
        self.CUSTOMER_NAME=customer_name
        self.MAIL_ID=mail_id
        self.CONTACT_NUMBER=contact_number
        self.BALANCE=balance

    def display(self):
        print(self.CUSTOMER_NAME,self.MAIL_ID,self.CONTACT_NUMBER,self.BALANCE)

    def deposit(self,amount):
        self.BALANCE+=amount
        print("Amount deposited successfully")

    def withdraw(self,amount):
        if amount>self.BALANCE:
            print("Insufficient balance")
        else:
            self.BALANCE-=amount
            print("Amount withdrawn successfully")

    @classmethod
    def display_bank(cls):
        print(cls.BANK_NAME,cls.BRANCH_NAME,cls.BRANCH_MANAGER_NAME)

    @classmethod
    def change_branch_manager(cls,branch_manager_name):
        cls.BRANCH_MANAGER_NAME=branch_manager_name
    
    @classmethod
    def change_bname(cls,bname):
        cls.BANK_NAME=bname

s1=bank("Preksha","preksha@gmail.com",1234567890,10000)
s2=bank("Rahul","rahul@gmail.com",1234567890,20000)
s3=bank("Rohan","rohan@gmail.com",1234567890,30000)

s1.display()
s2.display()
s3.display()
s1.deposit(5000)
s1.display()
s1.withdraw(10000)
s1.display()
bank.change_branch_manager("Rohan")
bank.display_bank()
bank.change_bname("HDFC")
bank.display_bank()


#~-----------------------------------------------------------------------------------------------------