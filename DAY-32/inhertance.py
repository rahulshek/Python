
#& Create a class bank which consist of 3 class  members 4 object (name,monumber,email, accountno) members 3 class member 4 object member and also create 2 class method and object method 

class Bank:
    bname="Axis"
    managername="Rahul"
    branchcode="IC001"
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
    def displaybank(cls):
        print("Bank Name:",cls.bname)
        print("Manager Name:",cls.managername)
        print("Branch Code:",cls.branchcode)
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


c1=Bank("Rahul",1234567890,"rahul@gmail.com",1234567890123456)
c2=Bank("Preksha",1234567890,"preksha@gmail.com",1234567890123456)
c3=Bank("Rohan",1234567890,"rohan@gmail.com",1234567890123456)

c1.display()
c2.display()
c3.display()
c1.displaybank()
c2.displaybank()
c3.displaybank()
c1.updatemobile(1234567890)
c1.updateemail("rahul@gmail.com")
c1.updateaccountno(1234567890123456)
c1.display()
c1.displaybank()
    


