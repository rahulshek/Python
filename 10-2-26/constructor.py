# # class Qspiders:
    
# #     branch='Ahmedabad'
# #     no_of_classes='6'
# #     timing='10 to 8'
    

# #     def __init__ (self,name,degree,course):
# #         self.NAME=name
# #         self.DEGREE=degree
# #         self.COURSE=course


# #     def display(self):
# #         print(self.NAME,self.DEGREE,self.COURSE)


# #     def change_course(self,new_course):
# #         self.COURSE=new_course

# #     @classmethod  
# #     def displaycls(cls):
# #         print(cls.branch,cls.no_of_classes,cls.timing)


# #     @classmethod
# #     def change_timing(cls,new_timing):
# #         cls.timing=new_timing
# #     @classmethod
# #     def change_No_of_classes(cls,new_no_of_classes):
# #         cls.no_of_classes=new_no_of_classes

# #     @classmethod
# #     def details(cls):
# #         print("Details updates successfully")


# # # s1=Qspiders("Rohit","B.Tech","Python")
# # # s1.display()
# # # s2=Qspiders("Rahul","BTech","Java")
# # # s1.display()
# # Qspiders.displaycls()
# # Qspiders.change_timing("9 to 6")
# # Qspiders.change_No_of_classes("5")
# # Qspiders.displaycls()
# # Qspiders.details()


# # # A method which is nethir realated to cLass nor to object is called static method
# # # Passing @static method decorator is madatory in the case of static method


# #create a class  hospital which consists of 3 class member 4 object member and 3 class method and 3 object method along with that create 2 objects  

# class Hospital:
    
#     name='City Hospital'
#     location='Ahmedabad'
#     no_of_doctors=50
#     speciality='All'


#     def __init__(self,patient_name,age,disease):
#         self.patient_name=patient_name
#         self.age=age
#         self.disease=disease
#         self.doctor=self.speciality

#     def display(self):
#         print(self.patient_name,self.age,self.disease,self.doctor)

#     def change_disease(self,new_disease):
#         self.disease=new_disease

#     @classmethod
#     def displaycls(cls):
#         print(cls.name,cls.location,cls.no_of_doctors)

#     @classmethod
#     def change_location(cls,new_location):
#         cls.location=new_location
        
#     @classmethod
#     def change_no_of_doctors(cls,new_no_of_doctors):
#         cls.no_of_doctors=new_no_of_doctors
#     @classmethod
#     def details(cls):
#         print("Details updated successfully")


# p1=Hospital("Rohit",25,"Fever")
# p1.display()
# p2=Hospital("Rahul",26,"Cold")
# p2.display()
# p1.change_disease("Pain")
# p1.display()
# Hospital.displaycls()
# Hospital.change_location("Surat")
# Hospital.change_no_of_doctors(100)
# Hospital.displaycls()
# Hospital.details()


#Pillars of oops 
#1.inheritance
#2.polymorphism
#3.encapsulation
#4.abstraction
