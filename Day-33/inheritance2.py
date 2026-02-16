
#& Create a class bank which consist of 3 class  members 4 object (name,monumber,email, accountno) members 3 class member 4 object member and also create 2 class method and object method 

class Bank:
    BNAME="Axis"
    MANAGERNAME="Rahul"
    BRANCHCODE="IC001"

    def __init__(self,name,monumber,email,accountno):
        self.NAME=name
        self.MONUMBER=monumber
        self.EMAIL=email
        self.ACCOUNTNO=accountno

    def display(self):
        print("Name:",self.NAME)
        print("Mobile Number:",self.MONUMBER)
        print("Email:",self.EMAIL)
        print("Account Number:",self.ACCOUNTNO)

    def displaycls(cls):
        print("Bank Name:",cls.BNAME)
        print("Manager Name:",cls.MANAGERNAME)
        print("Branch Code:",cls.BRANCHCODE)

    def updatemobile(self,monumber):
        self.MONUMBER=monumber

    def updateemail(self,email):
        self.EMAIL=email

    def updateaccountno(self,accountno):
        self.ACCOUNTNO=accountno

    @classmethod
    def changebank(cls,bname):
        cls.BNAME=bname

    @classmethod
    def changemanager(cls,managername):
        cls.MANAGERNAME=managername

    @classmethod
    def changebranch(cls,branchcode):
        cls.BRANCHCODE=branchcode


class Updated_Bank(Bank):
    CASHIER="Mr Dinga"
    def __init__(self,name,monumber,email,accountno,adhaar):
        #? self.NAME=name
        #? self.MONUMBER=monumber
        #? self.EMAIL=email
        #? self.ACCOUNTNO=accountno
        super().__init__(name,monumber,email,accountno)
        self.ADHAAR=adhaar

    def display(self): 
        super().display()
        print("Adhaar Number:",self.ADHAAR)

    def displaycls(cls):
        super().displaycls()
        print("Cashier Name",cls.CASHIER)
        

    def updateadhaar(self,adhaar):
        self.ADHAAR=adhaar

    @classmethod
    def displaybank(cls):
        super().displaycls()
        print("Cashier Name",cls.CASHIER)
    
    @classmethod
    def changecashier(cls,cname):
        cls.CASHIER=cname
    

    

c1=Updated_Bank("Rahul",1234567890,"rahul@gmail.com",1234567890123456,123456789012)
c2=Updated_Bank("Preksha",1234567890,"preksha@gmail.com",1234567890123456,123456789012)
c1.display()
# c1=Bank("Rahul",1234567890,"rahul@gmail.com",1234567890123456)
# c2=Bank("Preksha",1234567890,"preksha@gmail.com",1234567890123456)




""" 

# c1.display()
# print("--------------------------------------------------------------------")
# print("--------------------------------------------------------------------")
# c1.displaycls()

 """

""" 

c1.display()
print("--------------------------------------------------------------------")
print("--------------------------------------------------------------------")
c2.display()
print("--------------------------------------------------------------------")
print("--------------------------------------------------------------------")
c1.display()
print("--------------------------------------------------------------------")
print("--------------------------------------------------------------------")
c1.updateadhaar(123456789012)
c1.display()

c1.displaybank()
c2.displaybank()

c1.updatemobile(1234567890)
c1.updateemail("rahul@gmail.com")
c1.updateaccountno(1234567890123456)
c1.display()
c1.displaybank()
    
 """


