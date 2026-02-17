
#&Create class A acting as a parent class for Class B and create a another class c which is acting as a child class for class B

# class A:
#     def __init__(self):
#         print("This is class A")

# class B(A):
#     # def __init__(self):
#     #     print("This is class B")
#     pass

# class C(B):
#     # def __init__(self):
#     #     print("This is class C")
#     pass

# c1=C()
# c2=B()
# c3=A()

#~-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

#& Create a class resume1 which consists of name , percentage and school name as object members and then create another class resume2 which inherit the properties from resume1 and along with that have 12th percentage and college name as object members and then create another class resume3 which inherit's from resume2 and consist of deg_college and deg_percentage as object members

class resume1:
    def __init__(self,name,percentage,schoolname):
        self.NAME=name
        self.PERCENTAGE=percentage
        self.SCHOOLNAME=schoolname
    def display(self):
        a=self.NAME,self.PERCENTAGE,self.SCHOOLNAME
        return print(a)

class resume2(resume1):
    def __init__(self,name,percentage,schoolname,percentage12,collegename):
        super().__init__(name,percentage,schoolname)
        self.PERCENTAGE12=percentage12
        self.COLLEGENAME=collegename
    def display(self):
        b=self.NAME,self.PERCENTAGE,self.SCHOOLNAME,self.PERCENTAGE12,self.COLLEGENAME
        return print(b)

class resume3(resume2):
    def __init__(self,name,percentage,schoolname,percentage12,collegename,deg_college,deg_percentage):
        super().__init__(name,percentage,schoolname,percentage12,collegename)
        self.DEG_COLLEGE=deg_college
        self.DEG_PERCENTAGE=deg_percentage
    def display(self):
        c=self.NAME,self.PERCENTAGE,self.SCHOOLNAME,self.PERCENTAGE12,self.COLLEGENAME,self.DEG_COLLEGE,self.DEG_PERCENTAGE
        return print(c)
    
c1=resume3("Rahul",90,"Bright",80,"Indus","BTech",90)
c2=resume3("Preksha",90,"Bright",80,"Indus","Btech",90)
c1.display()
c2.display()

#~-----------------------------------------------------------------------------------------------------------------------------------------------------------------------